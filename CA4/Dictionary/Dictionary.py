from itertools import permutations
graph_root = "abcdefghiklmnopqrstuvwxyz"
class shelf:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.shelf = []
    def insert(self , val):
        self.shelf.append(val)
        self.end = self.end + 1
    def delete(self):
        self.start = self.start + 1
        return self.shelf.pop(0)
#make it easier to solve    
def preProcces(num_of_books):
    global graph_root
    dictElements = permutations(graph_root[0:num_of_books])
    perms = dict()
    for item in dictElements : perms[''.join(list(item))] = -5000
    return perms
   
num_of_books = int(input())
perms = preProcces(num_of_books)
voojaks_shelf = shelf()
level = 0
graph_root = graph_root[0:num_of_books]
voojaks_shelf.insert(graph_root)
voojaks_shelf.insert(level)
values = dict()
while voojaks_shelf:
    current_book = voojaks_shelf.delete()
    if type(current_book) == str:
        if perms.get(current_book , -1) != -5000:
            pass
        else :
            perms[current_book] = level
            for k in range(num_of_books) : 
                for p in range(k+1 , num_of_books) :
                    voojaks_shelf.insert(current_book[0:k] + current_book[k:p+1][::-1] + current_book[p+1:]) 
    else :
        if voojaks_shelf.shelf:
            voojaks_shelf.insert(current_book+1)
            level = level + 1
            pass
        else:
            break
num_of_scenarios = int(input())
for m in range(num_of_scenarios):
    current_perm = input().split()
    ans = ""
    for k in range(num_of_books):
        values[current_perm[1][k]] = graph_root[k]
    for p in range(num_of_books):
        ans = ans + values[current_perm[0][p]]
    print(perms[ans])