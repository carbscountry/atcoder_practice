N = int(input())
S = str(input())
ans = 0

i = 0
while i < len(S):
    #S[i] != S[i+1]となるiを見つける
    j = i + 1
    while j < len(S) and S[i] == S[j]:
        j += 1
    i = j
    ans += 1
print(ans)