
// A Backtracking program in
// C++ to solve Sudoku problem

// source: https://www.geeksforgeeks.org/sudoku-backtracking-7/
// Modified by Sander van Oostveen
#include <bits/stdc++.h>
using namespace std;

// UNASSIGNED is used for empty
// cells in sudoku grid
#define UNASSIGNED 0

// N is used for the size of Sudoku grid.
// Size will be NxN
#define N 9

// Checks whether it will be legal
// to assign num to the given row, col
bool isSafe(int grid[N][N], int row,
            int col, int num);

/* Takes a partially filled-in grid and attempts
to assign values to all unassigned locations in
such a way to meet the requirements for
Sudoku solution (non-duplication across rows,
columns, and boxes) */
bool SolveSudoku(int grid[N][N], int ind)
{
    int row = ind / 9;
    int col = ind % 9;

    // If there is no unassigned location,
    // we are done
    if (ind == 81)
        // success!
        return true;

    // Consider digits 1 to 9
    for (int num = 1; num <= 9; num++) {
         bool consistent = grid[row][col] == UNASSIGNED;

        for (int col1 = 0; col1 < N; col1++)
            if (grid[row][col1] == num)
                consistent = false;

        for (int row1 = 0; row1 < N; row1++)
            if (grid[row1][col] == num)
                consistent = false;

        int boxStartRow = row - row % 3;
        int boxStartCol = col - col % 3;
        for (int row1 = 0; row1 < 3; row1++)
            for (int col1 = 0; col1 < 3; col1++)
                if (grid[row1 + boxStartRow][col1 + boxStartCol] == num)
                    consistent = false;

        // if looks promising
        if (consistent) {
            // make tentative assignment
            grid[row][col] = num;

            // return, if success, yay!
            if (SolveSudoku(grid, ind++))
                return true;

            // failure, unmake & try again
            grid[row][col] = UNASSIGNED;
        }
    }
    // this triggers backtracking
    return false;
}

/* Returns a boolean which indicates whether
it will be legal to assign num to the given
row, col location. */
bool isSafe(int grid[N][N], int row,
            int col, int num)
{
    /* Check if 'num' is not already placed in
    current row, current column and current 3x3 box */
    for (int col1 = 0; col1 < N; col1++)
        if (grid[row][col1] == num)
            return false;

    for (int row1 = 0; row1 < N; row1++)
        if (grid[row1][col] == num)
            return false;

    int boxStartRow = row - row % 3;
    int boxStartCol = col - col % 3;
    for (int row1 = 0; row1 < 3; row1++)
        for (int col1 = 0; col1 < 3; col1++)
            if (grid[row1 + boxStartRow][col1 + boxStartCol] == num)
                return false;

    return grid[row][col] == UNASSIGNED;

    // return !UsedInRow(grid, row, num)
    //        && !UsedInCol(grid, col, num)
    //        && !UsedInBox(grid, row - row % 3,
    //                      col - col % 3, num)
    //        && grid[row][col] == UNASSIGNED;
}

/* A utility function to print grid */
void printGrid(int grid[N][N])
{
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++)
            cout << grid[row][col] << " ";
        cout << endl;
    }
}

// Driver Code
int main()
{
    // 0 means unassigned cells
    int grid3[N][N] = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                       { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                       { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                       { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                       { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                       { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                       { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                       { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                       { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };

    int grid2[N][N] = {
        {0,2,0,0,0,0,0,0,0},
        {0,0,0,6,0,0,0,0,3},
        {0,7,4,0,8,0,0,0,0},
        {0,0,0,0,0,3,0,0,2},
        {0,8,0,0,4,0,0,1,0},
        {6,0,0,5,0,0,0,0,0},
        {0,0,0,0,1,0,7,8,0},
        {5,0,0,0,0,9,0,0,0},
        {0,0,0,0,0,0,0,4,0}
    };

    int grid[N][N] = { {8, 0, 0, 0, 0, 0, 0, 0, 0},
                       {0, 0, 3, 6, 0, 0, 0, 0, 0},
                       {0, 7, 0, 0, 9, 0, 2, 0, 0},
                       {0, 5, 0, 0, 0, 7, 0, 0, 0},
                       {0, 0, 0, 0, 4, 5, 7, 0, 0},
                       {0, 0, 0, 1, 0, 0, 0, 3, 0},
                       {0, 0, 1, 0, 0, 0, 0, 6, 8},
                       {0, 0, 8, 5, 0, 0, 0, 1, 0},
                       {0, 9, 0, 0, 0, 0, 4, 0, 0} };
    SolveSudoku(grid, 0);
    SolveSudoku(grid2, 0);
    SolveSudoku(grid3, 0);

    return 0;
}

// This is code is contributed by rathbhupendra
