'''
入力をソートして A1≤…≤ANとして良いです。このとき i<jに対して |Ai−Aj|=Aj−Aiとなります。

各iについて ∑Nj=i+1|Ai−Aj|=(∑Nj=i+1Aj)−(N−i)Aiとなり、これは予め Aの累積和を計算しておくことでそれぞれ O(1)で求めることができます。よって O(N)でこの問題が解けました。
 '''

def main():
  from collections import deque
  N = int(input()) 
  lst = list(map(int, input().split()))

  ans = 0
  count = 0

  copylst = deque(lst.copy())
  my_pop = copylst.popleft

  for i in lst:
    count += 1
    my_pop()
    for j in copylst:
      ans += abs(i - j)
  
  print(ans)


main()