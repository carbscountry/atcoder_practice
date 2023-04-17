def combine(n, A):
    ans = 0
    # 初期値
    i = 0
    while i < n:
        j = i + 1
        ans += 1
        if (j < n):
            if(A[i] == A[j]):
                j += 1
            while (A[i] < A[j] and A[j] - A[j-1] == 1 or 0) or (A[i] > A[j] and A[j-1] - A[j] == 1 or 0):
                j += 1
                if(j == n):
                    break

        # print(A[i:j])
        i = j

    return ans


def main():
    n = int(input())
    A = list(map(int, input().split()))
    a = combine(n, A)
    print(a)


if __name__ == '__main__':
    main()
