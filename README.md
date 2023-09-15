# Rock-Paper-Scissors-project

## Description

The aim of this project is to build a rock-paper-scissors game using a deep learning model. The computer will choose its own sign (out of rock, paper and scissors) then detect the hand sign shown by the user using the camera.

## Gameplay

- Begin the game by running the program.
- At the start of each round, press enter to commence the running of the code.
- The program will prompt you to input a sign, either 'rock', 'paper' or 'scissors'.
- It will then automatically start a countdown. You have 5 seconds to show your chosen hand sign to your camera.
- The program will then either state the choices that you and the computer have made, or it will tell you that your sign was not recognised.
- The program will then tell you the result of the game, either 'You won!', 'You lost!', or 'It is a tie'.
- The next round will be announced, and you will have to press enter to start that round.
- The game will continue until either you or the computer have won three rounds. At this point, the program will announce the overall winner.


## Instalation instructions

The program uses the imported modules 'cv2', 'random', 'time' and 'numpy', as well as the function load_model from 'keras.models'. See the requirements.txt file for all installed dependencies.


## Github repository structure

The repository contains the python file for playing the game, called 'camera_rps.py'. It also contains the deep learning model 'keras_model.h5' and the labels 'labels.txt', which are loaded into the game. It also contains this readme file and the 'requirements.txt' file.

## Licence information

MIT licence.
