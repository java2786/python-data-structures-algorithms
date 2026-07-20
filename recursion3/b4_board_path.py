def solution(row, col, cr, cc, path):

    if(cc >=board_col or cr>=board_row):
        return
    
    if(cr == board_row - 1 and cc == board_col - 1):
        print(path)
        return


    # path = path+"R"
    # cc = cc+1
    solution(row, col, cr, cc+1, path+"R")


    # path = path + "D"
    # cr = cr+1
    solution(row, col, cr+1, cc, path+"D")


board_row = 4
board_col = 3

solution(board_row, board_col, 0, 0, "")
