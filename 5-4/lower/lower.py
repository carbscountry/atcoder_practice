N = int(input())
S = list(map(int,input().split()))

ans,count = 0,0

for i in range(len(S)-1):
    if(S[i] >= S[i+1]):
        count += 1
    else:
        count = 0
    ans = max(ans,count)

print(ans)
