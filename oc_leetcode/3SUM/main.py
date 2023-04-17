def solve(nums:list):
    nums.sort()
    ans = []
    for i in range(len(nums)-2):
        a = sums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            b = nums[start]
            c = nums[end]
            if a + b + c == 0 and [a,b,c] not in ans:
                ans.append([a,b,c])
                start += 1
                end -= 1
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1
                

    return ans




def main():
    A = list(map(int,input().split(',')))
    a = solve(A)
    print(a)

if __name__ == '__main__':
    main()