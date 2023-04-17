from collections import *
N = int(input())
S = [0]*N
ans = ''

count = defaultdict(list)
val_dict = defaultdict(int)
for _ in range(N):
    S[_] = (list(map(str,''.join(input()))))
    S[_] = Counter(S[_])

val_list = S[0].copy()
for i in S:
    _l = []
    for key,val in i.items():
        count[key].append(val)

for key in list(count.keys()):
    # if(len(count[key]) != N):
    #     del count[key]
    if(len(count[key]) == N):
        val_dict[key] = min(count[key])

for i,j in val_dict.items():
    ans += i*j
# num = Counter(S)
print("".join(sorted(ans)))

