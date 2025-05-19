a = input()
res1 = ""
max_res = ""
new_word = ""
for i in range(0,len(a)):
    if(a[i] in res1):
        ind = a[:i].rindex(a[i])
        new_word = a[ind+1:i+1]
        if(len(new_word) >= len(res1)):
            res1 = new_word
            pass
        if(len(res1) >= len(max_res)):
                max_res = res1
        res1 = new_word
    else:
        res1 += a[i]
if(len(res1) >= len(max_res)):
        max_res = res1
print(len(max_res))