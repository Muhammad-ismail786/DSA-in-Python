
# 52. N-Queens II

**Difficulty:** Hard

**Topics:** Backtracking, Recursion, Sets

**Languages:** Python, Python3

## # Intuition

The main idea is to place `n` queens on an `n x n` chessboard so that no two queens attack each other.

We place one queen in each row and check whether its column and both diagonals are already occupied.

If a safe position is found, we place the queen and move to the next row using recursion.

Whenever all `n` rows have a queen, we increase the count by 1.

## # Approach

1. Create three sets:
   - `cols` to track occupied columns.
   - `diag1` to track occupied diagonals using `row - col`.
   - `diag2` to track occupied diagonals using `row + col`.

2. Start placing queens from row 0.

3. Check every column to find a safe position.

4. If the position is safe:
   - Add the column and both diagonals to their sets.
   - Recursively move to the next row.
   - Backtrack by removing the column and diagonals from their sets.

5. If `row == n`, all queens are successfully placed, so increment `count`.

6. Finally, return the total count.

## # Complexity

- Time complexity: O(N!) approximately, due to backtracking and trying different queen placements.

- Space complexity: O(N) auxiliary space for the three sets, excluding the recursion stack.

## # Code

### Python

```python
class Solution(object):

    def totalNQueens(self, n):

        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def solve(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                d1 = row - col
                d2 = row + col

                if col in cols or d1 in diag1 or d2 in diag2:
                    continue

                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                solve(row + 1)

                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        solve(0)
        return count
```

### Python3

```python
class Solution:

    def totalNQueens(self, n: int) -> int:

        count = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def solve(row: int):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                d1 = row - col
                d2 = row + col

                if col in cols or d1 in diag1 or d2 in diag2:
                    continue

                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)

                solve(row + 1)

                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        solve(0)
        return count
```

## # Example

**Input:**
```text
n = 4
```

**Output:**
```text
2
```

**Explanation:**

There are two distinct ways to place four queens on a 4 x 4 chessboard so that no two queens attack each other.

## # Tags

- Backtracking
- Recursion
- Sets
- LeetCode
