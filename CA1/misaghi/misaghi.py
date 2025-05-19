def misaghiSub(subsequence):
    for end_a in range(0,len(subsequence)):
        for end_b in range(end_a+1,len(subsequence)):
            i = end_a
            j = end_b
            start_a = 0
            while(True):
                if(subsequence[start_a] == '0' or subsequence[i+1] == '0'):
                    break
                a = int(subsequence[start_a:i+1])
                b = int (subsequence[i+1:j+1])
                c = a + b
                if( j + len(str(c)) + 1 > len(subsequence)):
                    break
                else:
                    eindex_c = j + len(str(c))
                if(subsequence[j+1] == '0'):
                    break
                if int(subsequence[j+1:eindex_c+1]) == c:
                    if j+ len(str(c)) == len(subsequence) - 1 :
                        return "YES"
                    start_a = i + 1
                    i += len(str(b))
                    j += len(str(c))
                    pass
                else:
                    break
    return "NO"
subsequence = input()
print(misaghiSub(subsequence))
            