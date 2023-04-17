from collections import Counter
N = int(input())
input_list = [] #for get input list
ans = 0



for i in range(3):
    _list = list(map(int,input().split()))
    _list = [i % 46 for i in _list]
    input_list.append((Counter(_list)))


for x,x_val in input_list[0].items():
    for y,y_val in input_list[1].items():
        for z,z_val in input_list[2].items():
            if((x+y+z) % 46 == 0):
                ans += x_val*y_val*z_val
        
print(ans)
