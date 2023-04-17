from collections import *

def combine(n,A):
    ans = 0
    #初期値
    i = 0 
    while i < len(A):
        j = i + 1
        if(j < len(A)):
            while (A[i] < A[j] and A[j-1] <= A[j]) or (a[i] > a[j] and a[j-1] >= a[j]):
                j += 1
        ans += 1
        i = j
         

        


    return ans





def main():
    n = int(input())
    A = int(map(int,input().split()))
    a = combine(n,A)
    print(a)

if __name__ == '__main__':
    main()