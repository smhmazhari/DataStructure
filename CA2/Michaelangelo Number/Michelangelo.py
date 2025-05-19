n = int(input())
guesses = list(input().split(sep=' '))
all_guesses = list()

result = 0
current_bozkoos = set()
second_stack = list()

all_locations = [None]*(n)
init_index = 0

all_prevs = list()
first_stack = list()

for i  in guesses:
    all_guesses.append(int(i))

for i in all_guesses:
    all_locations[i-1] = init_index
    init_index += 1

for x in range(n,0,-1):
    if(len(first_stack) == 0):
        all_prevs.append(-1)
        first_stack.append(all_locations[x-1])
    else:
        while(first_stack[-1]>all_locations[x-1]):
            first_stack.pop()
            if(len(first_stack) == 0):
                break
        if(len(first_stack) != 0):
            all_prevs.append(first_stack[-1])
        else:
            all_prevs.append(-1)
        first_stack.append(all_locations[x-1])

all_prevs.reverse()
print('0')

for x in range(1,n+1,1):
    posx = all_locations[x-1]

    while(len(second_stack)!= 0):
        if(posx < second_stack[-1]):
                popvalue = second_stack.pop()
                if(popvalue in current_bozkoos):
                    result -= 1
                    current_bozkoos.remove(popvalue)
        else:
            break

    if(all_prevs[x-1]!=(-1)):
        if(len(second_stack)== 0):
            result += 1
            current_bozkoos.add(posx)
        elif(all_prevs[all_guesses[second_stack[-1]]-1]!= all_prevs[x-1]):
            result += 1
            current_bozkoos.add(posx)
    
    second_stack.append(posx)

    print(result)
    
