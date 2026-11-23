# LeetCode 51 - N-Queens (Python & Python3)

## # Intuition

The idea is to place `n` queens on an `n x n` chessboard so that no two queens can attack each other.

A queen can attack horizontally, vertically, and diagonally. Therefore, every queen must be placed in a safe position.

We place one queen in each row and try different columns until we find all valid board configurations.

## # Approach

We use **Backtracking** to solve this problem.

1. Create an `n x n` chessboard filled with `.` (empty cells).
2. Start placing queens from the first row.
3. Use the `isSafe()` function to check whether a queen can be placed in a particular column.
4. Check the upper column, upper-left diagonal, and upper-right diagonal.
5. If the position is safe, place the queen (`Q`) and move to the next row.
6. If all queens are placed successfully, save the current board in the answer.
7. Remove the queen (`.`) and try another column. This process is called backtracking.
8. Convert each board row into a string using `"".join()` and return all valid configurations.

## # Complexity

- **Time complexity:** `O(N! × N)` — We explore possible queen placements and check whether each position is safe.

- **Space complexity:** `O(N²)` — To store the chessboard and recursion-related space, excluding the output.

## # Code

### Python

```python
class Solution(object):

    def solveNQueens(self, n):
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(row, col):

            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):

            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return ans
```

### Python3

```python
class Solution:

    def solveNQueens(self, n: int) -> list[list[str]]:

        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isSafe(row: int, col: int) -> bool:

            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            i, j = row - 1, col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = row - 1, col + 1

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row: int) -> None:

            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for col in range(n):

                if isSafe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row + 1)
                    board[row][col] = '.'

        backtrack(0)
        return ans
```
