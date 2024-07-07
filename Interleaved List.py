L1 = [1,3,5,7,9,11,13,15,17,19]
L2 = [2,4,6,8,10,12,14,16,18,20]
L3 = []

tam = max(len(L1),len(L2))

for i in range(tam):
    if i < len(L1):
        L3.append(L1[i])
    if i < len(L2):
        L3.append(L2[i])

print(L3)