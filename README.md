# Rock-Paper-Scissors
This is a text-based version of _rock-paper-scissors_, played against the computer. The computer's choices are pseudo-random.

## Instructions

### Scoring the game
After the user enters their name, it is searched for in the rating.txt file. The user's score is then initialised with the corresponding value. If it is not present in the file, it is initialised to 0. For every victory the user's score is increased by 100, for every draw it is increased by 50 and for every loss nothing is added. The user can access their rating by typing the "!rating" command.

The information about each player stored in the file must be in the following format: name and score divided by a single space, each player on a new line. 

### Additional options of the game
Besides the standard options – rock, paper and scissors – the user can now specify the options they want to play, such as _rock, paper, scissors, lizard, spock_ or even _rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire_. Every option wins over one-half of the other options and gets defeated by another half. Which option beats which is calculated in the following way: for each element, the half of the elements that precedes it represents the options weaker than it. For example, in the _rock, paper, scissors, lizard, spock_ case, lizard wins over paper and scissors and gets defeated by spock and rock. 

The options must be separated by a single comma and no spaces (e. g.: "rock,paper,scissors"). In this stage, if the user enters a blank line, the game continues with the standard options.

### Game
The user enters their choice. Based on the pseudo-random choice of the computer, they can either win, lose or draw.

The game ends when the user types "!exit".

## Good luck!
