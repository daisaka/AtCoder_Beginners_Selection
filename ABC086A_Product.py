#シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください。

a, b = map(int, input().split())
c = a * b

if c % 2 == 0:
    print('Even')
else:
    print('Odd')