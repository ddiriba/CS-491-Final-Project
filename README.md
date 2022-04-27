# CS 491 Final Project

#Existing Project
The project I will be using is an open source roulette game. It currently does not have any unit tests so I wrote tests from scratch. In addition, the repository only has the game rules of roulette but I intend to integrate my players class from the black jack project we had. By doing so, the game will have player data being able to be tracked and stored. The github for the project is linked below.
https://github.com/cjekel/Python-Roulette
Unit Testing and Integration Testing
I was able to get an 80% coverage after writing some unit tests and integration tests. There was some changes from the initial goal due to time constraints in personal life. Listed below are the integrated tests.
Roulette Circle and Betting Integration
Betting and Player Integration
Player and Cocktail Waitress Integration

Module
statements
missing
excluded
coverage
BettingSystem.py
81
48
0
41%
Participants.py
15
2
0
87%
Player.py
43
17
0
60%
PythonRoulette.py
34
0
0
100%
roulette_unittest.py
160
0
0
100%
Total
333
67
80%



Centralizing Source Code and Automating the Build
Since I will be keeping all of my code updated on github, I utilized Github actions to automate my tests.
Automating Build and Deployment
Due to time constraints I was not able to accomplish automatic Build and Deployment

References
1. GitHub Repository for the Roulette game. https://github.com/cjekel/Python-Roulette
2. GitHub Actions Reference. https://github.com/features/actions
3. Docker Deployment Reference. https://docker-curriculum.com/
