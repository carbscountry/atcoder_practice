S = str(input())

words = []

i = 0

while i < len(S):
    #S[i] != S[j]
    j = i + 1
    while j < len(S) and S[i] == S[j]:
        j += 1
    
    #単語の切り出し
    words.append(S[i:j])
    i = j

#文字列を指定の形に変換する関数
def change_str(_str):
    _str =  _str[0] + str(len(_str)) 
    return _str

print("".join(list(map(change_str,words))))