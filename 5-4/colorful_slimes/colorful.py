N = int(input())
A = list(map(int,input().split()))

i = 0
cnt = 1
ans = 0
while i < N:
    j = i + 1
    while j < N and A[j] == A[i]:
            cnt += 1
            j += 1
    ans += cnt // 2
    cnt = 1
    i = j

print(ans)



# N = int(input())
# A = list(map(int,input().split()))

# i = 0
# cnt = 0
# for i in range(N-1):
#     if(A[i] == A[i+1]):
#         A[i+1] = '0'
#         cnt += 1

# print(cnt)