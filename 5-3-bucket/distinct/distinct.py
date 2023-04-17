from collections import *
import sys
N = int(input())
S = list(map(int,input().split()))

#度数表の作成
num = Counter(S)

#もし重複がなければすべての値が1ならばSの要素数と一致する
for i in num.values():
    if(i > 1):
        print('NO')
        sys.exit()
print('YES')