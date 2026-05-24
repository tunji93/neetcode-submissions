class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}

        squares = {i:set() for i in range(9)}


        for row in range(9):
            for col in range(9):


                cell = board[row][col]

                if cell == ".":
                    continue

                if cell in rows[row]:
                    return False
                rows[row].add(cell)
                
                if cell in cols[col]:
                    return False
                cols[col].add(cell)

                idx = ((row//3) * 3 ) + col//3

                if cell in squares[idx]:
                    return False
                
                squares[idx].add(cell)
        return True
        