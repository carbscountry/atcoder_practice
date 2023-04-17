from collections import *
N,M = map(int,input().split())

ans = 0
#連想配列を作る
num = defaultdict(int)

for i in range(N):
    K = list(map(int,input().split()))
    for a in K[1:]:
        num[a] += 1

for j in num.values():
    if(N == j):
        ans += 1
print(ans)
    