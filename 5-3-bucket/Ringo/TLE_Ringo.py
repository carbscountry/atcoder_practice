from collections import *
N = int(input())
S = list(map(int,input().split()))
ans = 0
def mods(nums):
    nums = nums % 200
    return nums

S_mods = list(map(mods,S))

list = 123*6
for i in range(N-1):
    target = S[i+1:]
    num_mods = S_mods[i]
    count_list = [i for i in target if (i - num_mods) % 200 == 0]
    ans += len(count_list)

print(ans)