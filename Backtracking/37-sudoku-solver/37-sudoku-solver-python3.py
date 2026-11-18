
class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

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


def main():

    board = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']
    ]

    obj = Solution()

    obj.solveSudoku(board)

    print("Solved Sudoku:\n")

    for row in board:
        print(" ".join(row))


if __name__ == "__main__":
    main()
