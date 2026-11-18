
# 37. Sudoku Solver

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/sudoku-solver/

## Intuition

We need to fill all empty cells ('.') in a 9x9 Sudoku board while following three rules:

- Each number from 1 to 9 must appear exactly once in every row.
- Each number from 1 to 9 must appear exactly once in every column.
- Each number from 1 to 9 must appear exactly once in every 3x3 box.

We can use Backtracking with Sets to efficiently check whether a number can be placed in an empty cell.

## Approach

1. Create three lists of sets to track numbers used in each row, column, and 3x3 box.
2. Traverse the board and store all empty cell positions in a list.
3. For each empty cell, calculate its corresponding 3x3 box.
4. Try numbers from '1' to '9'.
5. Check whether the number already exists in the current row, column, or box.
6. If the number is valid, place it in the board and update the corresponding sets.
7. Recursively solve the next empty cell.
8. If recursion returns true, the Sudoku is solved.
9. If the number does not lead to a solution, remove it from the board and all three sets. This process is called Backtracking.
10. If all empty cells are filled successfully, return true.

## Complexity

- Time complexity: O(9^m), where m is the number of empty cells (upper bound).
- Space complexity: O(m), where m is the number of empty cells for the recursion stack. The row, column, and box sets use O(1) auxiliary space because the board size is fixed at 9x9.

## Code

```python
class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                if num == '.':
                    empty.append((row, col))

                else:
                    box = (row // 3) * 3 + (col // 3)

                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

        def backtrack(index: int) -> bool:

            if index == len(empty):
                return True

            row, col = empty[index]

            box = (row // 3) * 3 + (col // 3)

            for num in '123456789':

                if (num not in rows[row] and
                    num not in cols[col] and
                    num not in boxes[box]):

                    board[row][col] = num

                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)

                    if backtrack(index + 1):
                        return True

                    board[row][col] = '.'

                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)
```
