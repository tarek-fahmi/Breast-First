import sys
from src.data_structures import Tree
import src.search_algorithms as s_obj


def broken_printer(char, filename):
    tree  = setup_input(filename)
    
    match char: # Check which search the user has requested.
        case 'B':
            s_obj.breadth_first_search(tree)
        case 'D':
            s_obj.depth_first_search(tree)
        case 'G':
            s_obj.greedy_search(tree)
        case 'I':
            s_obj.iterative_deepening_search(tree)
        case 'A':
            s_obj.a_star_search(tree)
        case 'H':
            s_obj.hill_climbing(tree)
        case _:
            print("Did not pick valid search strategy... Try running script again :)")
        
        
            

def setup_input(filename):
    f_obj = open(filename, 'r')
    
    start_code = f_obj.readline().split(',')
    goal_codes = f_obj.readline().split(',')
    unsafe_codes = f_obj.readline().split(',')
    
    return Tree(start_code, goal_codes, unsafe_codes)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        # You can modify these values to test your code
        char = 'B'
        filename = 'example1.txt'
    else:
        char = sys.argv[1]
        filename = sys.argv[2]
    print(broken_printer(char, filename))
    