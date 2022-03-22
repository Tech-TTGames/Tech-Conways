from sys import argv
import os.path
import board_io
import game_engine

def main(gens):
    board = board_io.import_board('gen_0.txt')
    for generation in range(gens):
        board = game_engine.emulate_generation(board)
        board_io.export_board(board,generation)
    print("Finished generating.")
    kte = input("Press any key to exit...\n")
    del(kte) 

if __name__ == '__main__':
    try:
        gens = int(argv[1])
    except IndexError:
        raise Exception("Missing generations argument!")
    except ValueError:
        raise Exception("Generation argument is not an int!")
    if not os.path.exists('gen_0.txt'):
        raise Exception("Generation 0 file (gen_0.txt) missing!")
    main(gens)