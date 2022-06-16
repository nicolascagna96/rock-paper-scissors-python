# Rock paper scissors

![picture alt](/images/responsive.PNG "rock-paper-scissors")

## Table of Content

1. [Introduction](#introduction)
2. [UX](#ux)
3. [Logic](#logic) 
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [ Deployment](#deployment)
8. [Credits](#credits)
   

## Introduction

In this project I replicated the famous rock, paper and scissors game.  It is a game originated from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".

A deployed link of the project can be found: [here](https://rock-paper-scissors-p3.herokuapp.com/ "Python")

## UX
### User Stories
- The user will be asked to provide his/her name.
- The user will be informed about the rules of the game.
- The user will have to follow the rules and win the game.
### User Goals
The outcome of the game is determined by 3 simple rules: 
- Rock wins against scissors.
- Scissors win against paper.
- Paper wins against rock.
The user needs to win the game against the computer.

## Logic
I created a flowchart of the game.

![picture alt](/images/project-flowchart.PNG "Flowchart")

## Features
### Existing features:
- Landing Page.
- Game Screen.
- End game alert.
#### Landing Page
![picture alt](/images/Landing-page.PNG "rock-paper-scissors")

#### Game Screen
![picture alt](/images/game-screen.PNG "rock-paper-scissors")

#### End game screen
![picture alt](/images/end-game-screen.PNG "rock-paper-scissors")

### Features Left to Implement
- I plan to add 3 rounds for the game and the user and computer scores.

## Technologies Used
### Main Language Used
- [Python](https://en.wikipedia.org/wiki/Python"Python")
### Python Modules
- [Random](https://docs.python.org/3/library/random.html"Random")
### Libraries, Framework & Tools
- [Heroku](https://dashboard.heroku.com/apps"Heroku")
- [PEP8](https://pep8.org/"PEP8")
- [Github](https://github.com"Github")
- [Diagram.net](https://app.diagrams.net/"Diagram")
- [Gitpod](https://www.gitpod.io/"Gitpod") 

## Testing
- I validate the code through the PEP8 Linter.
- Tried to give invalid inputs to test my validation of the input.
### PEP8 Online
[PEP8](https://pep8.org/"PEP8") was used yto validate the Python code to ensure that there is no error.

![picture alt](/images/Pep8-Testing.PNG "PEP8 Testing")

### Further Testing
- I tested the all the screens works in different browsers: Chrome, Safari, Firefox and Edge.
- I confirmed that this project is responsive, looks good and works on all standard screens using the devtools device toolbar.

### Unfixed Bugs 
- When adding a string in the user_action input we get an error. I'm planning to fix it as soon as possible.

## Deployment
The program was deployed to Heroku. These are the steps:
- Log in to Heroku.
- Click on "create a new app".
- Click on settings.
- Added these build packs: Python and nodejs.
- go to the Gitpod terminal:
- type heroku login -i
- enter your email
- enter your password
- type heroku apps
- heroku git:remote -a rock-paper-scissors-p3
- git add .
- git commit -m "Deploy to heroku CLI"
- git push origin main
- git push heroku main

## Credit
- [W3schools](https://www.w3schools.com/s"W3schools") Great source of information and inspiration
- [Udemy](https://www.udemy.com/course/100-days-of-code) 100 Days of Code: The Complete Python Pro Bootcamp for  2022
- [Devdojo](https://devdojo.com/"Devdojo.com") I found inspiration for my project
 
### Acknowledgements
- I want to thank all the Code Institute's tutors for the great support, and Martina Terlevic for reviewing my project and for giving me a lot of useful feedback.