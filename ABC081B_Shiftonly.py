#黒板に N 個の正の整数 A 1,...,A Nが書かれています．
# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
# 黒板に書かれている整数すべてを，2 で割ったものに置き換える．
# すぬけ君は最大で何回操作を行うことができるかを求めてください．

N = int(input())
A_list = list(map(int, input().split()))
counter = 0
while all(A%2 == 0 for A in A_list):
    A_list = [A/2 for A in A_list]
    counter += 1

print(counter)

    








