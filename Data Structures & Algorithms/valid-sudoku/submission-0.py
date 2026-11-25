class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_table = defaultdict(set)
        col_table = defaultdict(set)
        square_table = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[0])):
                square = (row // 3) * 3 + (col // 3)
                entry = board[row][col]
                if entry != ".":
                    if entry in row_table[row] or entry in col_table[col] or entry in square_table[square]:
                        return False
                    else:
                        row_table[row].add(entry)
                        col_table[col].add(entry)
                        square_table[square].add(entry)
        return True
                