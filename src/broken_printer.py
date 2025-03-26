import sys
from src.data_structures import Tree
import src.search_algorithms as s_obj


def broken_printer(char, filename):
    tree  = setup_input(filename)
    
    path = []
    expanded = []
    
    
    match char: # Check which search the user has requested.
        case 'B':
            (path, expanded) = s_obj.breadth_first_search(tree)
        case 'D':
            (path, expanded) = s_obj.depth_first_search(tree)
        case 'G':
            (path, expanded) = s_obj.greedy_search(tree)
        case 'I':
            (path, expanded) = s_obj.iterative_deepening_search(tree)
        case 'A':
            (path, expanded) = s_obj.a_star_search(tree)
        case 'H':
            (path, expanded) = s_obj.hill_climbing(tree)
        case _:
            print("Did not pick valid search strategy... Try running script again :)")
        
    clean_print(path)
    clean_print(expanded)

def clean_print(list):
    
    for code in list[:-1]:
        print(code + ',')
    
    print(code)

    return 
            

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
    