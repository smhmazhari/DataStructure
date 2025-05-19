class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.group = None
def make_first_team(enemies):
    result = list()
    for i in enemies.keys():
        if enemies[i]["self"].group == 1:
            result.append(enemies[i]["self"].value)
    return result

def make_team(enemies):
    for i in enemies.keys():
        if enemies[i]["self"].group == None:
            make_team_for_none(i, enemies)
        else:
            flag = make_team_for_other(i, enemies)
            if flag:
                print(enemies[i]["self"].value)
                return False
        
    return True

def make_team_for_other(i, enemies):
    '''if not ok return true'''
    opposite_group = {1:2,2:1}
    result = True
    for enemy in enemies[i]["n"].keys():
        if enemies[i]["n"][enemy].group == None:
            enemies[i]["n"][enemy].group = opposite_group[enemies[i]["self"].group]
            return False
        elif enemies[i]["n"][enemy].group == opposite_group[enemies[i]["self"].group]:
            result = False
    return result
        
def make_team_for_none(i, enemies):
    opposite_group = {1:2,2:1}
    for j in enemies[i]["n"].keys():
        if enemies[i]["n"][j].group != None:
            enemies[i]["self"].group = opposite_group[enemies[i]["n"][j].group]
            return
    enemies[i]["self"].group = 1
    if len(enemies[i]["n"]) != 0:
        first_neighbor = list(enemies[i]["n"].keys())[0]
        enemies[i]["n"][first_neighbor].group = 2


students_and_relations = dict()
students_and_relations["V_count"], students_and_relations["E_count"] = map(int, input().split())
students_and_relations["E"] = list()
for _ in range(students_and_relations["E_count"]):
    new_e = list(map(int, input().split()))
    students_and_relations["E"].append(new_e)


enemies = {i+1:{"self":Node(i+1) ,"n":dict()} for i in range(students_and_relations["V_count"])}
for edge in students_and_relations["E"]:
    enemies[edge[0]]["n"][edge[1]] = enemies[edge[1]]["self"]
    enemies[edge[1]]["n"][edge[0]] = enemies[edge[0]]["self"]


is_possible = make_team(enemies)
result = {"is_possible":is_possible ,"enemies": enemies}
if not result["is_possible"]:
    print(-1)
else:
    team1 = make_first_team(result["enemies"])
    print(len(team1))
    print(*team1)

