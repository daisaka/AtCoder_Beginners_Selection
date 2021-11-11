#すぬけ君は 1,2,3 の番号がついた 3 つのマスからなるマス目を持っています。 
#各マスには 0 か 1 が書かれており、マス i には s iが書かれています。
#すぬけ君は 1 が書かれたマスにビー玉を置きます。
#ビー玉が置かれるマスがいくつあるか求めてください。

val = input()
s = [int(x) for x in list(str(val))]
count = 0
for i in range(len(s)):
    if s[i] == 1:
        count += 1
    else:
        continue

print(count)
