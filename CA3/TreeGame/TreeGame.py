class Node:
    def __init__(self) -> None:
        self.childs = 0
        self.index = 0
        self.color = -1
        self.parent = 0
n, questions = map(int,input().split())

nodes = [Node() for i in range(n)]
parents = list(map(int,input().split()))
current_node = 1

for parent in parents:
    nodes[current_node].parent = parent
    nodes[parent-1].childs += 1
    current_node += 1

tries = [0] * questions

for question in range(questions):
    heads = list(map(int,input().split()))
    heads = heads[1:]
    sum = 0
    reduce = 0
    for coin in heads:
        nodes[coin-1].color = question
    for coin in heads:
        base_node = nodes[coin-1]
        if (nodes[base_node.parent-1].color == question and coin > 1) :
            reduce += 2
        sum += base_node.childs + 1
    tries[question] = sum - reduce

for i in tries :
    print(i)