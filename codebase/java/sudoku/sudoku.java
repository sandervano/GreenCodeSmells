/*Source: https://rafal.io/posts/project-euler-96-sudoku.html*/
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class sudoku {

    public boolean solve(int[][] board, int ind){
      if(ind == 81){
        return true; // solved
      }
      int row = ind / 9;
      int col = ind % 9;

      // Advance forward on cells that are prefilled
      if(board[row][col] != 0) return solve(board, ind+1);

      else{
            // we are positioned on something we need to fill in.
            // Try all possibilities

            for(int i = 1; i <= 9; i++){
                if(consistent(board, row, col, i)){
                    board[row][col] = i;
                  if(solve(board, ind+1)) return true;
                  board[row][col] = 0; // unmake move
                }
            }
      }

      // no solution
      return false;
    }


    // Check whether putting "c" into index "ind" leaves the board in a consistent state
    public boolean consistent(int[][] board, int row, int col, int c) {
        // check columns/rows
        for(int i = 0; i < 9; i++){
            if(board[row][i] == c) return false;
            if(board[i][col] == c) return false;
        }

        int rowStart = row - row % 3;
        int colStart = col - col % 3;

        for(int m = 0; m < 3; m++){
            for(int k = 0; k < 3; k++){
                if(board[rowStart + k][colStart + m] == c) return false;
            }
        }

        return true;
    }


  public static void main(String[] args) {
    sudoku e = new sudoku();
    int[][] result3 = { { 3, 0, 6, 5, 0, 8, 4, 0, 0 },
        { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
        { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
        { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
        { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
        { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
        { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
        { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
        { 0, 0, 5, 2, 0, 6, 3, 0, 0 }
    };

    int[][] result2 = {
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

    int[][] result = { {8, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 0, 3, 6, 0, 0, 0, 0, 0},
        {0, 7, 0, 0, 9, 0, 2, 0, 0},
        {0, 5, 0, 0, 0, 7, 0, 0, 0},
        {0, 0, 0, 0, 4, 5, 7, 0, 0},
        {0, 0, 0, 1, 0, 0, 0, 3, 0},
        {0, 0, 1, 0, 0, 0, 0, 6, 8},
        {0, 0, 8, 5, 0, 0, 0, 1, 0},
        {0, 9, 0, 0, 0, 0, 4, 0, 0}
    };
    e.solve(result, 0);
    e.solve(result2, 0);
    e.solve(result3, 0);
  }
}
