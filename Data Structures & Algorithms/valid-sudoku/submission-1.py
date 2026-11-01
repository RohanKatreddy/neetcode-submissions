class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def _check_valid(row_i, column_i):
            cell_value = board[row_i][column_i]
            if cell_value != '.':
                if is_value_read[int(cell_value)]: return False
                else: is_value_read[int(cell_value)] = True
            return True

        is_value_read = [0] * 10 # 0 - 9

        # Row Checks
        for row_i in range(9):
            for column_i in range(9):
                if not _check_valid(row_i, column_i): return False
            is_value_read = [0] * 10

        # Column Checks
        for column_i in range(9):
            for row_i in range(9):
                if not _check_valid(row_i, column_i): return False
            is_value_read = [0] * 10

        # 3x3 Block Checks
        for block in range(9):
            start_row = (block//3) * 3
            start_column = (block % 3) * 3
            for row_offset in range(3):
                for column_offset in range(3):
                    row_i = start_row + row_offset
                    column_i = start_column + column_offset
                    if not _check_valid(row_i, column_i): return False
            is_value_read = [0] * 10
        return True