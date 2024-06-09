import os
import traceback
from pathlib import Path

import utils.config_manager as cm
import whisperx
from models.transcription import Transcription


class WhisperXHandler:
    def __init__(self):
        self._whisperx_result = None

    async def transcribe_file(self, transcription: Transcription) -> str:
        """
        Transcribe audio from a file using the WhisperX library.

        :param transcription: An instance of Transcription containing information about
                              the audio file.
        :type transcription: Transcription
        :return: The transcribed text or an error message if transcription fails.
        :rtype: str
        """
        config_whisperx = cm.ConfigManager.get_config_whisperx()

        device = "cpu" if config_whisperx.use_cpu else "cuda"
        task = "translate" if transcription.should_translate else "transcribe"

        try:
            model = whisperx.load_model(
                config_whisperx.model_size,
                device,
                compute_type=config_whisperx.compute_type,
                task=task,
                language=transcription.language_code,
            )

            audio_path = str(transcription.source_path)
            audio = whisperx.load_audio(audio_path)
            self._whisperx_result = model.transcribe(
                audio, batch_size=config_whisperx.batch_size
            )

            text_combined = " ".join(
                segment["text"].strip() for segment in self._whisperx_result["segments"]
            )

            # Align output if should subtitle
            if (
                "srt" in transcription.output_file_types
                or "vtt" in transcription.output_file_types
            ):
                model_aligned, metadata = whisperx.load_align_model(
                    language_code=transcription.language_code, device=device
                )
                self._whisperx_result = whisperx.align(
                    self._whisperx_result["segments"],
                    model_aligned,
                    metadata,
                    audio,
                    device,
                    return_char_alignments=False,
                )

            return text_combined

        except Exception:
            return traceback.format_exc()

    def generate_subtitles(
        self, file_path: Path, output_file_types: list[str], should_overwrite: bool
    ):
        """
        Generate subtitles for a video or audio file.

        :param file_path: The path to the video or audio file for which subtitles are
                          to be generated.
        :type file_path: Path
        :param output_file_types: A list of strings representing the desired output
                                    file types for the generated subtitles. Subtitles
                                    will be generated in each of the specified formats.
        :type output_file_types: list[str]
        :param should_overwrite: Indicates whether existing subtitle files should be
                                overwritten if they exist. If False, subtitles will
                                only be generated if no subtitle file exists for
                                the given format.
        :type should_overwrite: bool
        """
        config_subtitles = cm.ConfigManager.get_config_subtitles()
        output_dir = file_path.parent

        for output_type in output_file_types:
            path_to_check = file_path.parent / f"{file_path.stem}.{output_type}"

            if should_overwrite or not os.path.exists(path_to_check):
                writer = whisperx.transcribe.get_writer(output_type, str(output_dir))
                writer_args = {
                    "highlight_words": config_subtitles.highlight_words,
                    "max_line_count": config_subtitles.max_line_count,
                    "max_line_width": config_subtitles.max_line_width,
                }

                # https://github.com/m-bain/whisperX/issues/455#issuecomment-1707547704
                self._whisperx_result["language"] = "en"

                writer(self._whisperx_result, file_path, writer_args)
