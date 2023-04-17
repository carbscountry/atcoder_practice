import time 

def sum_n(n):
    s = 0
    start = time.time()
    for i in range(n):
        s += i
    end = time.time()
    print(end-start)
    return s
