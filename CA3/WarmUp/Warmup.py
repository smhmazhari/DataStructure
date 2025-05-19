import sys
import re

INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'

class MinHeap:
    def __init__(self):
        self.heap_list = list()

    class Node:
        def __init__(self,key):
            self.key = key

    def evaluate_index(self,index):
        try:
            index = int(index)
        except:
            raise Exception(INVALID_INDEX)
        if index >= len(self.heap_list) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        return index
    
    def bubble_up(self, index):
        index = self.evaluate_index(index)
        while (index > 0):
            parent = (index - 1) // 2
            if (self.heap_list[parent].key > self.heap_list[index].key):
                self.heap_list[index], self.heap_list[parent] =  self.heap_list[parent], self.heap_list[index]
                index = parent
            else:
                break

    def bubble_down(self, index):
        index = self.evaluate_index(index)
        while True:
            last_child = index
            right_child = 2*index + 2
            left_child = 2*index + 1

            if (left_child < len(self.heap_list)):
                if (self.heap_list[last_child].key > self.heap_list[left_child].key):
                    last_child = left_child

            if (right_child < len(self.heap_list)):
                if (self.heap_list[last_child].key > self.heap_list[right_child].key):
                    last_child = right_child

            if  (index != last_child):
                self.heap_list[index], self.heap_list[last_child] = self.heap_list[last_child], self.heap_list[index]
                index = last_child
            else:
                break

    def heap_push(self, key):
        self.heap_list.append(self.Node(key))
        self.bubble_up(len(self.heap_list) - 1)

    def heap_push_node(self, node):
        self.heap_list.append(node)
        self.bubble_up(len(self.heap_list) - 1)

    def heap_pop(self):
        if (len(self.heap_list) == 0):
            raise Exception(EMPTY)
        elif (len(self.heap_list) == 1):
            res = self.heap_list.pop()
            return res.key
        
        res = self.heap_list[0]
        last_child = self.heap_list.pop()
        self.heap_list[0] = last_child
        self.bubble_down(0)
        return res.key
    
    def heap_pop_node(self):
        if (len(self.heap_list) == 0):
            raise Exception(EMPTY)
        elif (len(self.heap_list) == 1):
            res = self.heap_list.pop()
            return res
        
        res = self.heap_list[0]
        last_child = self.heap_list.pop()
        self.heap_list[0] = last_child
        self.bubble_down(0)
        return res

    def find_min_child(self, index):
        index = self.evaluate_index(index)
        left_child = 2*(index + 1) -1
        right_child = 2*(index + 1)

        if (left_child >= len(self.heap_list)):
            raise Exception(EMPTY)
        elif (right_child >= len(self.heap_list)):
            return left_child
        else:
            if (self.heap_list[left_child].key >= self.heap_list[right_child].key):
                return right_child
            else:
                return left_child

    def heapify(self, *args):
        for i in args:
            self.heap_push(i)

class Bst:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        if (self.root == None):
            self.root = self.Node(key)
        else: 
            self._insert_(self.root, key)

    def _insert_(self, node, key):
        if (key >= node.key):
            if (node.right != None):
                self._insert_(node.right, key)
            else:
                node.right = self.Node(key)
        else:
            if (node.left != None):
                self._insert_(node.left, key)
            else:
                node.left = self.Node(key)

    def inorder(self):
       self._inorder_(self.root)

    def _inorder_(self, node):
        if (node != None):
            self._inorder_(node.left)
            print(node.key, end= " ")
            self._inorder_(node.right)

class HuffmanTree:
    class Node:
        def __init__(self, char, repetition):
            self.char = char
            self.key = repetition
            self.code = ""
            self.left = None
            self.right = None

    def __init__(self):
        self.all_chars = []
        self.tree = MinHeap()
        self.root = None

    def set_letters(self, *args):
        for char in args:
            self.all_chars.append(self.Node(char, 1))

    def set_repetitions(self, *args):
        for i in range(len(args)):
            self.all_chars[i].key = args[i]
        for char in self.all_chars:
            self.tree.heap_push_node(char)



    def build_codes(self, node, current_code):
        if (node is None):
            return
        elif (node.char is not None):
            node.code = current_code
            return

        self.build_codes(node.left, current_code + "0")
        self.build_codes(node.right, current_code + "1")
    def build_huffman_tree(self):
        while (len(self.tree.heap_list) != 1):
            node1 = self.tree.heap_pop_node()
            node2 = self.tree.heap_pop_node()

            merged_node = self.Node(None, node1.key + node2.key)
            merged_node.left = node1
            merged_node.right = node2

            self.tree.heap_push_node(merged_node)

        self.root = self.tree.heap_pop_node()
        current_code = ""
        self.build_codes(self.root, current_code)

    def get_huffman_code_cost(self):
        return self.calculate_cost(self.root)

    def calculate_cost(self,node):
        if node is None:
            return 0
        if node.char is not None:
            return len(node.code)*node.key + self.calculate_cost(node.left) + self.calculate_cost(node.right)
        else:
            return self.calculate_cost(node.left) + self.calculate_cost(node.right)

    def text_encoding(self, text):
        all_chars_repetition = dict()
        for word in text:
            all_chars_repetition[word] = 0
        for word in text:
            all_chars_repetition[word] += 1
        for x in list(all_chars_repetition.keys()):
            self.tree.heap_push_node(self.Node(x,all_chars_repetition[x]))
        self.build_huffman_tree()


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
