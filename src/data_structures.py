


class Node:

    def __init__(self, rgb_v, depth: int = 0):

        self.mhd = None
        self.rgb_v = []
        self.depth = depth
        self.codes = []

        self.children = []  # Array of child nodes.

class Tree:
    """
    This tree will represent all possible index inversions up to a depth of k.
    
    The root node stores the start code, and the goal is to algorithmically search the tree
    for the given goal codes.
    
    Goal codes and start codes are stored as String arrays.
    
    Fringe and expanded nodes are stored in Node arrrays.
    """
    def  __init__(self, rgb_v: str):
        new_root = Node(rgb_v)
        self.root = self.build_tree_from_root(new_root)
        
        self.k = len(rgb_v) # K = max inversions, and thus also the maximum depth 
        self.check_k_within_range()
        
        
        self.goal_codes = [] # String array contains goal codes extracted from input file.
        self.unsafe_codes = [] # Disallowed states, extracted from input file.
        
        self.queue = [] # Special array based data-type (First In = First Out), stores fringe nodes.
        self.visited = [] # Standard array, stores already expanded/visited nodes.
        
        self.n_expanded = 0 # Tracks the number of nodes we have expanded thus far, avoids need to recalculate.
    
    
    
    def expand_node(self, node: Node):
        """
        Expands a node, adding the node's children to the fringe and
        the node itself to expanded nodes list.
        """
        if self.n_expanded >= 1000: # Check if max expansions hit.
            return -1
        
        self.expanded_nodes.add(node) # Add to list of expanded nodes
        
        self.n_expanded += 1 # Increment counter
        
        
        node.children = self.get_children(node.rgb_v) # Compute children of this node based on rgb_v
        
        if node.depth < self.k: # If we have yet to reach max depth, add children to fringe.
            self.queue.add(node.children)
            self.nodes.add(node.children)
            
        return 0
        

    def build_tree_from_root(self, node: Node):
        """
        Based on rgb_v, returns a list of child nodes which will be added to the tree.
        
        Nodes are in ascending order in terms of the index of inversion.
        
        Will return None if depth exceeds k or k is invalid.
        """
        temp = node.rgb_v
        kids = []
    
        # Create k inversions, at each index.
        for i in range(len(temp)):
            if temp[i] == '1':
                temp[i] = '0'
            else:
                temp[i] = '1'
            
            # Check if node is legal and unique.
            if self.check_safe(temp) and temp not in self.codes:
                new_kid += Node(temp)
            else:
                return -1
            
            self.queue += new_kid
            kids += new_kid
            if depth >= self.k:
                return -1
            else:
                return self.get_children(rgb_v, depth + 1)
    
        return kids

        
    def get_goal(self, node: Node): 
        "Check if current node is a goal node. Return boolean"
        if node.rgb_v in self.goal_codes: # If this
            return True
        return False
    
    def get_safe(self, node: Node):
        "Check if current node is outside of disallowed nodes sublist."
        if rgb_v in self.unsafe_codes:
            return True
        return False
    
    def get_expanded(self, node: Node):
        "Check if current node has been visited yet."
        if node in self.expanded_nodes:
            return True
        return False
    
    def get_k_within_range(self):
        if self.k < 3 or self.k > 12:
            print("SEARCH FAILED")
            exit(-1)
    
    
