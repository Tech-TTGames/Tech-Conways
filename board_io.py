def import_board(f_name):
    board = []
    len_errors = []
    sym_errors = []
    board_len = 0
    line_id = 1
    first_loop = True
    #Data import to list with data verification checks
    with open(f_name,"r") as f:
        for line in f:
            stripped_line = line.strip()
            line_list = list(stripped_line)
            line_list_interpreted = []
            #DV: Lenght Check
            if first_loop:
                board_len = len(line_list)
                first_loop = False
            elif board_len != len(line_list):
                sym_errors.append(str(line_id))
            #DV: Invalid Symbol Check + Symbol Interpretation
            for symbol in line_list:
                if symbol == ".":
                    line_list_interpreted.append(False)
                elif symbol == "#":
                    line_list_interpreted.append(True)
                else:
                    sym_errors.append(str(line_id))
                    break
            board.append(line_list_interpreted)
            line_id += 1

    #Throwing Errors found in DV!
    if len_errors and sym_errors:
        len_errs = ",".join(len_errors)
        sym_errs = ",".join(sym_errors)
        raise Exception(f"Line(s) {len_errs} are of incorrect length.\nFurthermore, Invalid symbol(s) in line(s) {sym_errs}.")
    elif len_errors:
        len_errs = ",".join(len_errors)
        raise Exception(f"Line(s) {len_errs} are of incorrect length.")
    elif sym_errors:
        sym_errs = ",".join(sym_errors)
        raise Exception(f"Invalid symbol(s) in line(s) {sym_errs}.")
    
    return board

def export_board(board,gen_id):
    board_translated = [[] for i in range(len(board))]
    line_id = 0
    for line in board:
        for cell in line:
            if cell:
                board_translated[line_id].append('#')
            else:
                board_translated[line_id].append('.')
        line_id += 1
    board_str = [line + '\n' for line in list(map(''.join, board_translated))]
    try:
        with open(f"gen_{gen_id+1}.txt",'x') as file:
            file.writelines(board_str)
    except FileExistsError:
        raise Exception(f"File gen_{gen_id+1}.txt already exists! Please remove it!")