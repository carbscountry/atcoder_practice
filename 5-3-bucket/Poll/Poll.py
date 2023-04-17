from collections import *
N = int(input())

S = [input() for i in range(N)]

num = Counter(S)
max_num_vote = max(num.values())

max_keys = [k for k, v in num.items() if v == max_num_vote]
max_keys.sort()
for i in range(len(max_keys)):
    print(max_keys[i])
