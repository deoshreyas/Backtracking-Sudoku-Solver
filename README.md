# Backtracking-Sudoku-Solver

## :zap: About
Backtracking is an approach used to solve problems exactly like Sudoku. This repository contains some code I wrote to try and make sense of backtracking. The reason we use backtracking is because the naive approach to solving the game by trying all possible combinations is too time consuming. Here is a brief explanation of backtracking:-
- Check whether a number is safe to assign before assigning (not present in same row, grid or column).
- Assign the number and recursively call the function to check for a new number in the next empty spot. Again check if safe and repeat.
- If we don't encounter a solution, go back to step 1 and try a different number.
- If no number results in a solution, then no solution exists. 
As you can see, this is quite similar to how our own brains handle the game of Sudoku!

**NOTE:** There might be multiple solutions to a single board. The program may not recognize and handle that. 

## :desktop_computer: How to run locally
Just clone the repository on your machine, and run `main.py`. You might need to install a few packages, like `pygame`. Please make sure you have the font `comicsans` installed on your machine (or change the font in the source).