from collections import *

N = int(input())
S = list(map(int,input().split()))
num = defaultdict(int)
for i in S:
    num[i] += 1

ans = N*(N-1) // 2
for val in num.values():
    ans -= val*(val-1) // 2
print(ans)