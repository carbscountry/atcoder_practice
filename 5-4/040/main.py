S = str(input())
ans = 0
r = [0]*(len(S)+1)
l = [0]*(len(S)+1)

for i in range(len(S)):
    if S[i] == '<':
        r[i+1] += r[i] + 1
            
    if S[len(S)-i-1] == '>':
        l[len(S)-i-1] = l[len(S)-i ] + 1

for i in range(len(S)+1):
    ans += max(r[i],l[i])
print(ans)
# for i in range(len(S) - 1, -1, -1):
#     print(print(i))

# i = 0 

# while i < len(S):
#     j = i
#     while j < len(S) and S[j] == S[i]:
#         j += 1
#     if(S[i] == '<'):
#         for len_num,input_num in enumerate(reversed(range(i,j+1))):
#             num[len_num] = input_num
#     if(S[i] == '>'):
#         for 
#     i = j