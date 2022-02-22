# Knight's-Tour

![Playfield](https://upload.wikimedia.org/wikipedia/commons/c/ca/Knights-Tour-Animation.gif)

This application gives the user an interface to interact with and play the [Knight's Tour](https://en.wikipedia.org/wiki/Knight%27s_tour) puzzle using user input. The user decides a playing field of arbitrary size. If a user inserts a grid that cannot be won, the computer will alert the user to this. The user can also ask the computer for a solution which will be given using [backtracking](https://en.wikipedia.org/wiki/Backtracking) and [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)), finding the computationally optimal solution via [Warnsdorff's rule](https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorff's_rule)

## How to play

In simple terms, the user is meant to use a Knight Chess piece to touch every square on the board one time and one time only. Meaning, the Knight cannot come back into contact with a square that has already been touched, and every square on the board must be touched. By the end of the game a winning solution should look similar to this:

![Knight's Puzzle solved](https://upload.wikimedia.org/wikipedia/commons/f/f4/Knight%27s_Tour_of_130x130_Square_Board.png)

### Example Gameplay

Squares needed to be traversed will be marked with an underscore _ and squares already traversed an astrisk *
