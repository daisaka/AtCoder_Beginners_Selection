#あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。 これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
#同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for a in range(a+1):
    for b in range(b+1):
        for c in range(c+1):
            if a*500 + b*100 + c*50 == x:
                count += 1
            else:
                continue
print(count)



