def combine(N, A):
    ans = 0
    # 初期値
    i = 0
    while i < N:
        j = i + 1
        ans += 1
        while (j < N and A[j - 1] <= A[j]):
            j += 1
        if A[i] >= A[j-1]:
            while (j < N and A[j - 1] >= A[j]):
                j += 1
        i = j

    return ans


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(combine(n, a))


if __name__ == '__main__':
    main()
