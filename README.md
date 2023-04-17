# 記録


## oj使い方
- [マニュアル](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)
- oj d url(ダウンロード)
- oj t -c "python3 main.py"(テスト)

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

- [164 - gacha](https://atcoder.jp/contests/abc164/tasks/abc164_c)

- [154 - Distinct or not](https://atcoder.jp/contests/abc154/tasks/abc154_c)

- [118 - Foods Loved by Everyone](https://atcoder.jp/contests/abc118/tasks/abc118_b)

- [081 - Not so Diverse](https://atcoder.jp/contests/abc081/tasks/arc086_a)

- [競プロ典型問題90問 027 Sign Up Requests](https://atcoder.jp/contests/typical90/tasks/typical90_aa)

- [155 Poll](https://atcoder.jp/contests/abc155/tasks/abc155_c)
    - 名前順にソートするのを忘れずに

- [073 Write and Erase](https://atcoder.jp/contests/abc073/tasks/abc073_c)

- [082 Good Sequence](https://atcoder.jp/contests/abc082/tasks/arc087_a)

- [058 怪文書](https://atcoder.jp/contests/abc058/tasks/arc071_a)
    - from functools import reduceを使うとgood
    - Counterは&(AND)で共通項を取れる
    - .most_common()でCounterの各要素の出現回数を取れる

- [206 Swappable](https://atcoder.jp/contests/abc206/tasks/abc206_c)
    - N(N-1) // 2から例外を引く。Ai = Aj

- [200 Ringo's Favorite Number](https://atcoder.jp/contests/abc200/tasks/abc200_c)
    - 200のmodの数を元に考える。
    - ちなみに200で割った数の余りは200未満なので考えるのはmodの差が0になるものだけ

- [046 - I love 46](https://atcoder.jp/contests/typical90/tasks/typical90_at)
    - Counterで集計して全探索でおk

## 5-4 連長圧縮、区分分割
- [143 - Slimes](https://atcoder.jp/contests/abc143/tasks/abc143_c)
    - S[i] != S[i+1]となるiを見つける

- [019 - 高橋くんと文字列圧縮](https://atcoder.jp/contests/abc019/tasks/abc019_2)

- [039 Lower](https://atcoder.jp/contests/abc139/tasks/abc139_c)
    - 前後の比較にはfor ループを使おう

- [116 Grand](https://atcoder.jp/contests/abc116/tasks/abc116_c)
    - あとでやる
    - 1.考え方としては次の数の方が多い時に回数が増えると考える
    - 2.一つの要素を１つずつ引いていき、0になるまで連長圧縮を使う

 - [AGC 026](https://atcoder.jp/contests/agc026/tasks/agc026_a)

 - [AGC 040 -><](https://atcoder.jp/contests/agc040/tasks/agc040_a)
    - 隣の数より大きいor小さくなればいい
    - 　> と　<　で別の配列で値を算出してそれぞれの大きい方を取ればいい

- [AGC Sorted Arrays](https://atcoder.jp/contests/agc013/tasks/agc013_a)
    - 




## ocコーディングテスト対策講座

- 