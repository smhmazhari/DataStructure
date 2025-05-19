from collections import deque
Infinity = 10000000000000

def zeroOneBFS(graph,N,M):  
    V = len(graph)
    distance = dict()
    for u in range(V): 
        distance[10 * graph[u][0][0][0] + graph[u][0][0][1]] = Infinity 

    all_cells = deque() 
    distance[11] = 0
    all_cells.append(graph[0]) 

    while all_cells: 
        v = all_cells[0] 
        all_cells.popleft() 
        for i in range(1,len(v)): 
            a = 10*v[i][0][0] + v[i][0][1]
            b = 10*v[0][0][0] + v[0][0][1]
            if (distance[a] >  distance[b] + v[i][1]): 
                distance[a] = distance[b] + v[i][1]     
                if v[i][1] == 0: 
                    all_cells.appendleft(child_expense[v[i][2]]) 
                else: 
                    all_cells.append(child_expense[v[i][2]])

    if(distance[10*N + M] == Infinity):
        print(-1)
    else:
        print(distance[10*N + M])

line1 = input().split()
num_of_rows = int(line1[0])
num_of_columns = int(line1[1])
num_of_bright_cells = int(line1[2])
bright_cells = list()
child_expense = [[]]*(num_of_bright_cells + 1)

for i in range(num_of_bright_cells):
    x_border, y_border = input().split()
    bright_cells.append([int(x_border), int(y_border)])
    child_expense[i] = child_expense[i] + [[bright_cells[i], 0,i]]

bright_cells.append([num_of_rows, num_of_columns])
bs_count = len(bright_cells) - 1 
child_expense[bs_count] = child_expense[bs_count] + [[bright_cells[bs_count], 0,bs_count]]
current_expense = 0
for p in range(len(bright_cells)):
    for j in range(p+1, len(bright_cells)):
        cost = 0
        current_expense = current_expense + 1 
        distance = (bright_cells[p][0]-bright_cells[j][0])**2 + (bright_cells[p][1]-bright_cells[j][1])**2
        if (distance == 1):
            cost = 0
            child_expense[p] = child_expense[p] + [[bright_cells[j], cost,j]]
            child_expense[j] = child_expense[j] + [[bright_cells[p], cost,p]]
        else:
            if (bright_cells[p][0] - bright_cells[j][0] < 3 and bright_cells[p][0] - bright_cells[j][0] > -3
               or bright_cells[p][1] - bright_cells[j][1] < 3 and bright_cells[p][1] - bright_cells[j][1] > -3):
                cost = 1
                child_expense[p] = child_expense[p] + [[bright_cells[j], cost,j]]
                child_expense[j] = child_expense[j] + [[bright_cells[p], cost,p]]
zeroOneBFS(child_expense, num_of_rows , num_of_columns)