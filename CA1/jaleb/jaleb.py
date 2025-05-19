let_dic ={'a' :0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
my_list = [0]* 2**10
my_list[0] = 1
bitmap = 0
word = input()
jalebs = 0
for x in word :
    bitmap = bitmap ^ (2 ** let_dic[x])
    jalebs += my_list[bitmap] 
    for i in range(10):
        temp = bitmap ^ (2**i)
        jalebs += my_list[temp]
    my_list[bitmap] += 1
print(jalebs)