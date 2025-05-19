class Bst:
    class Node:
        def __init__(self, key, index):
            self.index = index
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key, index):
        if (self.root == None):
            self.root = self.Node(key, index)
            return self.root
        else: 
            return self._insert_(self.root, key, index)

    def _insert_(self, node, key, index):
        if (key >= node.key):
            if (node.right != None):
                return self._insert_(node.right, key, index)
            else:
                node.right = self.Node(key, index)
                node.right.parent = node
                print(node.key, end=" ")
                return node.right
        else:
            if (node.left != None):
                return self._insert_(node.left, key, index)
            else:
                node.left = self.Node(key, index)
                node.left.parent = node
                print(node.key, end=" ")
                return node.left

    def nearest_anc(self, first_node, second_node):
        if (self.root == None):
            return None
        else:
            return self._nearest_anc_(self.root, first_node, second_node)
        
    def _nearest_anc_(self,root, first_node, second_node):
        if (root == None):
            return None
        elif (root == first_node or root == second_node):
            return root
        
        left_found = self._nearest_anc_(root.left, first_node, second_node)
        right_found = self._nearest_anc_(root.right, first_node, second_node)

        if (left_found != None and right_found != None):
            return root
        elif (left_found != None):
            return left_found  
        else:
            return right_found
    def inorder(self):
       self._inorder_(self.root)

    def _inorder_(self, node):
        if (node != None):
            self._inorder_(node.left)
            print(node.key, end= " ")
            self._inorder_(node.right)

num_of_nodes = input()
nodes = list(map(int,input().split()))
a, b = list(map(int,input().split()))


first_node = 0
second_node = 0
x = 1
current_node_ind = 0 
bts_bst = Bst()


while current_node_ind < int(num_of_nodes) :  
    if current_node_ind+x == b:
        second_node = bts_bst.insert(nodes[current_node_ind],current_node_ind+x)
    elif current_node_ind+x == a:
        first_node = bts_bst.insert(nodes[current_node_ind],current_node_ind+x)
    else:
        _ = bts_bst.insert(nodes[current_node_ind],current_node_ind+x)
    current_node_ind += 1

print()

nearest_common_anc = bts_bst.nearest_anc(first_node,second_node)
print(nearest_common_anc.index)


