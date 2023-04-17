from collections import *
N = int(input())
S = [int(input()) for i in range(N)]

num = Counter(S)

exist_num = [k for k,v in num.items() if v % 2 != 0]

print(len(exist_num))