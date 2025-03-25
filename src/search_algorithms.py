from src.data_structures import Tree, Node



def breadth_first_search(tree: Tree):
    """
    Starting from leftmost neighbor, explore all neighbors, before expanding.
    """
    current_node = tree.root
    fringe = tree.fringe_nodes
    
    tree.expand_node(current_node)
    
    
    
    while fringe:
        for node in tree.fringe_nodes:
            
            if tree.expand_node(node) == 1:
                print(tree.fringe_nodes)
        
        fringe = tree.fringe_nodes
            
        

def depth_first_search(tree: Tree, max_depth: int = 9e9):
    """
    Explore the deepest leftmost node before exploring parents and siblings (Step-Bros and slutty Step-Sis stuck under the water).
    """
    
    current_node = tree.root
    fringe = tree.fringe_nodes
    
    tree.expand_node(current_node)
    
    print(tree.expanded_nodes)
    print(tree.fringe_nodes)
    
      
def iterative_deepening_search(tree: Tree, max_depth):
    """
    Incremently conduct depth first search at increasing tree depths.
    """
    return
    
def greedy_search(tree: Tree):
    """
    Choose path of lowest heuristic value from fringe nodes (leftmost tiebreaking).
    """
    return

def a_star_search(tree: Tree):
    """
    
    """
    return

def hill_climbing_search(tree: Tree):
    """
    
    """
    return