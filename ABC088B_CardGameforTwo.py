#N 枚のカードがあります. i 枚目のカードには, a iという数が書かれています.
#Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.
#2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

n = int(input())
i = map(int, input().split())

i_list = [num for num in i]
i_list.sort(reverse=True)

alice_draws = i_list[0::2]
bob_draws = i_list[1::2]

ans = sum(alice_draws) - sum(bob_draws)
print(ans)