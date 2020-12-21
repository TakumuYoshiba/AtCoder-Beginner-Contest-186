import numpy as np

H, W = map(int,input().split()) 

lst = [list(map(int, input().split())) for l in range(H)]
ans = 0

min_num = np.amin(lst)

for i in range(H):
  for j in range(W):
    diff = lst[i][j] - min_num
    ans += diff
print(ans)


'''
2 2
1 2 
3 4
[[1, 2], [3, 4]]
'''