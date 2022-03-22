def sum_neighbours(board,cell):
    neighbour_var = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)] #all variations of neigbours
    alive_neighbours = 0
    len_board = len(board)-1
    len_line = len(board[0])-1
    for neighbour in neighbour_var:
        neighbour_cell = (cell[0]+neighbour[0],cell[1]+neighbour[1])
        if not any(coord < 0 for coord in neighbour_cell) and not neighbour_cell[0]>len_board and not neighbour_cell[1]>len_line:
            if board[neighbour_cell[0]][neighbour_cell[1]]:
                alive_neighbours += 1
    return alive_neighbours
    
def emulate_generation(board):
    next_board = [[] for i in range(len(board))]
    line_id = 0
    for line in board:
        cell_id = 0
        for cell in line:
            neighbour_sum = sum_neighbours(board,(line_id,cell_id))
            if cell:
                #Check if cell survives
                if 2 <= neighbour_sum <= 3:
                    next_board[line_id].append(True)
                else:
                    next_board[line_id].append(False)
            #Check if cell is born
            elif neighbour_sum == 3:
                next_board[line_id].append(True)
            else:
                next_board[line_id].append(False)
            cell_id +=1
        line_id += 1
    return(next_board)
