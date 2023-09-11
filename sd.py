easy1 = [5,10,15,2,4,6,8]
easy2 = [-2,-4,-6,2,4,6,0.1]

i=0
j=0
while i < len(easy1):
    while j < len(easy2):
        if easy1[i]==easy2[j]:
            easy1.insert(i+1,easy1[i])
            easy2.pop(j)
        j+=1
    i+=1
print(easy1)
print(easy2)