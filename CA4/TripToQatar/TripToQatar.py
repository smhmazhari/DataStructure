def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return []
    for node in graph[start]:
        if node not in path:
            current_way = find_path(graph, node, end, path)
            if current_way: 
                return current_way
    return []


num_of_cities =int(input())
leaves = []
result = []
to_print = ""
cities = dict()
for _ in range(num_of_cities-1):
    u, v = map(int, input().split())
    leaves.append((u, v))
wanted = [1] + list(map(int, input().split())) + [1] 
all_paths = 0 

for leaf in leaves:
    if leaf[0] in cities.keys():
        cities[leaf[0]].append(leaf[1])
        if(leaf[1] not in cities.keys()):
            cities[leaf[1]] =[leaf[0]]
        else:
            cities[leaf[1]].append(leaf[0])
    else:
        cities[leaf[0]] = [leaf[1]]
        if(leaf[1] not in cities.keys()):
            cities[leaf[1]] =[leaf[0]]
        else:
            cities[leaf[1]].append(leaf[0])
            all_paths += 1 


for i in range(len(wanted)-1):
    current_way = find_path(cities,wanted[i],wanted[i+1])
    if(i!=0):
        result = result + current_way[1:]
    else:
        result = result + current_way
        
if (len(result) - 1) <= (2 * num_of_cities) - 2 :
    for i in result:
        to_print += str(i) +" "
    print(to_print[:-2])
else:
    print(-1)
    
