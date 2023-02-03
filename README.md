<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="docs/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Audiotext</h3>

  <p align="center">
    A program that transcribes audio from a file or microphone to text in any supported language by Google API.
    <br />
    <a href="https://github.com/HenestrosaConH/audiotext/issues">Report Bug</a> · <a href="https://github.com/HenestrosaConH/audiotext/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Main screenshot light][main-system]](https://github.com/HenestrosaConH/audiotext)

The project structure is as follows:
 
- `docs`: Contains files related to the documentation of the project.
- `res`: Contains all the static resources used by the app, which are the app icon (located in the `img` folder) and the i18n files (located in the `locales` folder).
- `src`:  Contains the source code files of the app.

Besides those directories, there are also these two files (apart from the .gitignore, README.md and LICENSE):

- `audiotext.spec`: Used to generate a .exe file with [PyInstaller](https://pyinstaller.org/en/stable/). Notice that, inside the file, there are some annotations, which are `ROOT DIRECTORY PATH`, `PATH TO CUSTOM TKINTER` and `PATH TO RES FOLDER`. You will have to replace them by the indicated path of your computer. For example, my `PATH TO CUSTOMTKINTER` is `c:\\users\\JC\\appdata\\local\\programs\\python\\python310\\lib\\site-packages\\customtkinter`.  
- `requirements.txt`: Lists the names and versions of each package used to build this project.
 
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- BUILT WITH -->

### Built With

- [pydub](https://github.com/jiaaro/pydub)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

**Important**: You need to install [FFmpeg](https://ffmpeg.org) to execute the program. Otherwise, it won't be able to process the audio files. You can download FFmpeg from the [official site](https://ffmpeg.org/download.html)

If you want to execute the program:
- Go to [releases](https://github.com/HenestrosaConH/audiotext/releases) and download the latest one. Once you download it and uncompress it, open the `audiotext` folder and open the `audiotext.exe` file. 

If you want to open the code:
- Clone the project with the `git clone https://github.com/HenestrosaConH/audiotext.git` command and then open it with your favourite IDE (mine is [PyCharm](https://www.jetbrains.com/pycharm/)).
- Please bear in mind that you cannot generate a single .exe file for this project with PyInstaller due to the dependency with the CustonTkinter package (reason [here](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing  

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag `enhancement`.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

<a href="mailto:henestrosaconh@gmail.com">Email</a> - [LinkedIn][linkedin-url]

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

I've made use of the following repositories to make this README:

-   [Best-README-Template](https://github.com/othneildrew/Best-README-Template/)
-   [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/HenestrosaConH/audiotext.svg?style=for-the-badge
[contributors-url]: https://github.com/HenestrosaConH/audiotext/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HenestrosaConH/audiotext.svg?style=for-the-badge
[forks-url]: https://github.com/HenestrosaConH/audiotext/network/members
[stars-shield]: https://img.shields.io/github/stars/HenestrosaConH/audiotext.svg?style=for-the-badge
[stars-url]: https://github.com/HenestrosaConH/audiotext/stargazers
[issues-shield]: https://img.shields.io/github/issues/HenestrosaConH/audiotext.svg?style=for-the-badge
[issues-url]: https://github.com/HenestrosaConH/audiotext/issues
[linkedin-url]: https://linkedin.com/in/henestrosaconh
[main-system]: docs/main-system.png
[icon]: docs/icon.png
