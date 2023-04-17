from collections import *
N = int(input())

S = list(map(int,input().split()))
ans = 0
num = Counter(S)

for key,val in num.items():
    if(val < key):
        ans += val
    elif(val > key):
        ans += val - key
print(ans)