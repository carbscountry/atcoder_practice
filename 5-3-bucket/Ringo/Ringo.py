from collections import *
N = int(input())
S = list(map(int,input().split()))
ans = 0
def mods(nums):
    nums = nums % 200
    return nums

_mods = Counter(list(map(mods,S)))

for i in _mods.values():
    ans += i*(i-1) // 2

print(ans)
