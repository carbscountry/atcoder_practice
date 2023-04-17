from collections import Counter
from functools import reduce
 
def com(a: Counter, b: Counter):
  return a & b
 
def solve(n, S):
  cnt = [Counter(x) for x in S]
  common = reduce(com, cnt)
  common = common.most_common()
  common.sort()
  ans = "".join([x * i for x, i in common])
  return ans
 
n = int(input())
S = [input() for _ in range(n)]
 
print(solve(n, S))