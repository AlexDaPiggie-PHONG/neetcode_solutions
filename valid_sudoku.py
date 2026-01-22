'''
Docstring for valid_sudoku
Check number in each row
    dictionary with key is row and value is set of number in that row
'''
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        size = len (board)

        row_lst = []
        col_lst = []
        box_lst = []

        for i in range (9):
            row_dict = {}
            col_dict = {}
            box_dict = {}
            for key in range (1, 10):
                row_dict[key] = 0
                col_dict[key] = 0
                box_dict[key] = 0

            row_lst.append (row_dict)
            col_lst.append (col_dict)
            box_lst.append (box_dict)
        

        for i in range (size):
            for j in range (size):

                num = board[i][j]
                if num.isnumeric():
                    num = int(num)

                    '''UPDATE ROW'''
                    if row_lst[i][num] == 0:
                        row_lst[i][num] = 1
                    else:
                        return False
                
                    '''UPDATE COL'''
                    if col_lst[j][num] == 0:
                        col_lst[j][num] = 1
                    else:
                        return False

                    '''UPDATE BOX'''
                    box_position = 3*(i // 3) + j // 3
                    if box_lst[box_position][num] == 0:
                        box_lst[box_position][num] = 1
                    else:
                        return False
        return True

solulu = Solution()
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print (solulu.isValidSudoku(board))