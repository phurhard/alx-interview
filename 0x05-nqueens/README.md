## NQueens

What does the nqueens problem postulate??

The nqueens problem postulates a chess game problem where by N number of Queens are placed on a NxN board without any of the queens attacking each other

## Important Notes

* N number of Queens
* NxN board
* No two Queen should be able to attack each other

In chess, a Queen can move along any path on the chessboard as she is the most powerful piece of the game
She can move verticaly, horizontally, positive diagonally(bottom left to top right) or negative diagonally(top left to bottom right)
Hence a way to achieve the NQueens factor is to ensure that

    Each Queen is on it's own row and column and also ensure it is also on it's own positive diagonal and negative diagonal.

For the row and column it's quite easier with a for loop but the diagonals are a little bit tricky.
The formula to use for the diagonal are given below

    for the negative diagonal r-c = constant {from top left to bottom right}
    for the positive diagonal r+c = constant {bottom left to top right}

after these the board is transversed and the cells position values are returned


