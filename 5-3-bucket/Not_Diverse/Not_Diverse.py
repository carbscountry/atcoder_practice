from collections import *
#get input num
N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

num = Counter(A)
num = sorted(num.items(), key=lambda x:x[1])
change_num = len(set(A)) - K

for i in range(change_num):
    ans += num[i][1]

print(ans)

