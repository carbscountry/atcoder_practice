# n = int(input())
# S = list(map(int, input().split()))
 
# ans = S[0]

# for i in range(len(S)-1):
#     if S[i] < S[i+1]:
#         ans += S[i+1]-S[i]

# print(ans)

# #Chamao
n = int(input())
h = list(map(int, input().split()))
ans = 0
while True:
    left = 0
    if all(map(lambda x : x == 0, h)):
        exit(print(ans))
    
    while left < n:
        if h[left] == 0:
            left += 1
        else:
            ans += 1
            while left < n and h[left] > 0:
                h[left] -= 1
                left += 1