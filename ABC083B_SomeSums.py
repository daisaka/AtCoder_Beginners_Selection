#1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

n, a, b = (int(x) for x in input().split())

l = []
def sum_of_digit(num):
    ten4 = int(num//10000)
    ten3 = int(num//1000)
    ten2 = int(num//100)
    ten1 = int(num//10)
    ten0 = num%10
    return ten4 + ten3 + ten2 + ten1 + ten0

for num in range(n+1):
    if a <= sum_of_digit(num) and b >= sum_of_digit(num):
        l.append(num)

print(sum(l))

