from collections import *
N = int(input())
S = [input() for i in range(N)]

num = defaultdict(int)
for day,i in enumerate(S):
    if(num[i] == 0):
        print(day+1)
    num[i] += 1
