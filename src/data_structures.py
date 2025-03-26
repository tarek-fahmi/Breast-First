class Node:

    def __init__(self, rgb_v, depth: int = 0):

        self.mhd = None
        self.rgb_v = []
        self.depth = depth
        self.codes = []

        self.parent: Node = None
        self.children = []  # Array of child nodes.
        
        
    

class Tree:
    """
    This tree will represent all possible index inversions up to a depth of k.
    
    The root node stores the start code, and the goal is to algorithmically
    search the tree
    for the given goal codes.
    
    Goal codes and start codes are stored as String arrays.
    
    Fringe and expanded nodes are stored in Node arrrays.
    """
    def  __init__(self, rgb_v: str, goal_codes, unsafe_codes):
        
        new_root = Node(rgb_v)
        self.root = self.build_tree_from_root(new_root)
        
        self.k = len(rgb_v) # K = max inversions, and thus also the maximum depth 
        self.check_k_within_range()
        
        
        self.goal_codes = goal_codes # String array contains goal codes extracted from input file.
        self.unsafe_codes = unsafe_codes # Disallowed states, extracted from input file.
        
        self.queue = [] # Special array based data-type (First In = First Out), stores fringe nodes.
        self.visited = [] # Standard array, stores already expanded/visited nodes.
        self.stack = [] # Stack array...
        
        self.n_expanded = 0 # Tracks the number of nodes we have expanded thus far, avoids need to recalculate.
    
    
    
    def visit_node(self, node: Node, is_dfs: bool = False):
        """
        Expands a node, adding the node's children to the fringe and
        the node itself to expanded nodes list.
        """
        if self.n_expanded >= 1000: # Check if max expansions hit.
            return -1
        
        self.expanded.add(node) # Add to list of expanded nodes
        
        self.n_expanded += 1 # Increment counter
                
        if node.depth < self.k: # If we have yet to reach max depth, add children to fringe.
            self.queue.remove(0)
            if is_dfs:
                self.queue = node.children + self.queue
            else:
                self.queue.add(node.children)
                self.nodes.add(node.children)
            
        return 0
        
    def set_hamming_value(self, node):
        """
        Returns the minimum hamming values for a node based on possible goal nodes.
        """
        hamming_distances = [] # For each goal state, compute MHD relative to that goal state.
        
        for code in self.goal_codes:
            current_hamming_distance = 0
            
            for char in len(range(code)):
                if code[i] == node.rgb_v:
                    current_hamming_distance += 1
                    
            hamming_distances += current_hamming_distance
            
        node.mhd = min(hamming_distances)
        return 
            
        

    def build_tree(self, node: Node):
        """
        Based on rgb_v, returns a list of child nodes which will be added
        to the tree.
        
        Nodes are in ascending order in terms of the index of inversion.
        
        Will return None if depth exceeds k or k is invalid.
        """
        current_rgb_inversion = node.rgb_v
        kids = []
        
    
        while True:
            # Create k inversions, at each index.
            for i in range(len(current_rgb_inversion)):
                if current_rgb_inversion[i] == '1':
                    current_rgb_inversion[i] = '0'
                else:
                    current_rgb_inversion[i] = '1'
                
                # Check if node is legal.
                if self.check_safe(current_rgb_inversion):
                    new_kid = Node(current_rgb_inversion)
                    self.set_hamming_value(new_kid)
                    
                else:
                    return -1
                
                self.queue += new_kid

                # TODO: complete building function.
        
        return kids

        
    def get_goal(self, node: Node): 
        "Check if current node is a goal node. Return boolean"
        if node.rgb_v in self.goal_codes: # If this
            return True
        return False
    
    def get_safe(self, node: Node):
        "Check if current node is outside of disallowed nodes sublist."
        if node.rgb_v in self.unsafe_codes:
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
    
    @staticmethod
    def get_path(node: Node, arr: list = []):
        list.push(node.rgb_v)
        
        if node.parent == None: # Base case (final step of recursion)
            return list
        else:
            return get_path(node.parent, arr) # Recursive case (the condition where you continue to work on subproblems)

    @staticmethod
    def failed_search():
        """
        Report a failed search and exit with error code...
        """
        
        print("SEARCH FAILED")
        exit(-1)
        
    
    @staticmethod
    def breadth_first_search(self):
        """
        Starting from leftmost neighbor, explore all neighbors, before expanding.
        """
        self.visit_node(self.root)
        
        path = []
        
        while self.queue: #so long as the queue is not empty
            for node in self.queue:
                
                self.visit_node(node)

                if self.check_goal(node):
                    break 
            
        if self.check_goal(node): # If we have ended on a goal node...
            path = self.get_path(node)
            return (path, self.visited)
        else: # If we have not ended on a goal node...
            self.failed_search()
        
        
    def depth_first_search(self, max_depth: int = 9e9):
        """
        Explore the deepest leftmost node before exploring parents and siblings 
        """
        
        self.visit_node(self.root)
        
        while self.queue: # While there are still nodes to visit:
            
            for node in self.queue: # Continue visiting nodes....
                self.visit_node(node, True) 

                if node.depth < max_depth: # If the current node's children are in the depth limited subtree.
                    self.visit_node()
                    
                if self.check_goal(node): # If we have found a goal node, end the search.
                    break
        
        if self.check_goal(node): # If the search ended on a goal node, then return the paths.
            path = self.get_path(node)
            return (path, self.visited)
        
        else: # If we have not ended on a goal node, throw error.
            return -1
            
        
    def iterative_deepening_search(self):
        """
        Incremently conduct depth first search at increasing tree depths.
        """
        self.visit_node(self.root)
    
        
        for i in range(self.k): #Iterate through integers up to max depth.
            
            result = self.depth_first_search(i): # Run DFS with current max depth.
                
            if result is not -1:
                break
            else:
                continue
        
        return result
                
            
        
    def greedy_search(self):
        """
        Choose path of lowest heuristic value from fringe nodes 
        (leftmost tiebreaking).
        """
        self.visit_node(self.root)
        
        path = []
        
        while self.queue: #so long as the queue is not empty
            for node in self.queue:
                
                if self.queue > 1:
                    min_node_mhd
    
    def a_star_search(self):
        """
        
        """
        return

    def hill_climbing_search(self):
        """
        
        """
        return
srt = 'srt'