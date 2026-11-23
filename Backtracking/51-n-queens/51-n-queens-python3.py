
class Solution:

    def isSafe(self, board: list[list[str]], row: int, col: int, n: int) -> bool:

        # Check upper column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False

            i -= 1
            j -= 1

        # Check upper-right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True

    def backtrack(self, board: list[list[str]], row: int, n: int, ans: list[list[str]]) -> None:

        # All queens placed successfully
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        # Try every column
        for col in range(n):

            if self.isSafe(board, row, col, n):

                # Place queen
                board[row][col] = 'Q'

                # Move to next row
                self.backtrack(board, row + 1, n, ans)

                # Backtrack: remove queen
                board[row][col] = '.'

    def solveNQueens(self, n: int) -> list[list[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]

        ans = []

        self.backtrack(board, 0, n, ans)

        return ans


# Main function
if __name__ == "__main__":

    n = 4

    solution = Solution()

    result = solution.solveNQueens(n)

    print("Total Solutions:", len(result))

    for i, board in enumerate(result, start=1):

        print("\nSolution", i)

        for row in board:
            print(row)
