# 記録

## 5-2 全探索 メモリ制限,TLEに注意
- [097_B_Exponential](https://atcoder.jp/contests/abc097/tasks/abc097_b) 
    - べき数であり、平方根ではない。注意
- [098_B_Cut and Count](https://atcoder.jp/contests/abc098/tasks/abc098_b)   
    - set関数を使ってユニーク数を取ろう。共通するものという前提を忘れない
- [051_B_Sum of Three Integers](https://atcoder.jp/contests/abc051/tasks/abc051_b)
    - TLEに注意
    - 例題を見返そう
- [Minimum_Coins](https://atcoder.jp/contests/typical90/tasks/typical90_p)
    - python3だとTLEになるがpyplだとOKなコードがたくさんある。pyplで試してみよう
- [055 - Select 5](https://atcoder.jp/contests/typical90/tasks/typical90_bc)
    - コンビネーションを使うライブラリを調べて使おう
- [157 - Guess The Number](https://atcoder.jp/contests/abc157/tasks/abc157_c)
    - range(10**(N-1),10**(N))の全探索をしよう
- [195 - Many Oranges](https://atcoder.jp/contests/abc195/tasks/abc195_b)
    - 少し問題の解釈を変えよう。ピッタリにするのでつまり最大の数の時は最小グラム*最大の数がk以上、最小の数はその逆
- [079 - Train Ticket](https://atcoder.jp/contests/abc079/tasks/abc079_c)
    - パーミテーションを使う（数字の間に+か-が入ると考える）
    - from itertools import product
- [088 - C -Takahashi](https://atcoder.jp/contests/abc088/tasks/abc088_c)
    - 要素を引いて答えと一致するか比較
- [095 - Half and Half](https://atcoder.jp/contests/abc095/tasks/arc096_a)
    - X,Y大小を取る。
    - 買い方には３パターンある
- [108 - Trianguler Relationship](https://atcoder.jp/contests/abc108/tasks/arc102_a)
    -  a % K の値で全探索
        - a % K を決め打つと b % K, c % K のとるべき値が一意に決まることを利用します (a+b, a+c が K の倍数であることから)。そうして決まった b, c について b+c が K の倍数になっているかどうかを check します。
    - 周期性あり
    - [解説](https://drken1215.hatenablog.com/entry/2018/09/02/011000)

- [112 - Pyramid](https://atcoder.jp/contests/abc112/tasks/abc112_c)
    - 
## 5-3 バケット

-[]
