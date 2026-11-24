
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


if __name__ == "__main__":

    n = int(input("Enter n: "))

    solution = Solution()

    print("Total Solutions:", solution.totalNQueens(n))
