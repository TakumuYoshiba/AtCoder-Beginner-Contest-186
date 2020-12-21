N = int(input())

value_10 = N
value_8 = format(N, 'o')#8進数に変換
count = 0

for i in range(1,N+1):
  value_8 = format(i, 'o')
  str_i = str(i)
  str_i_8 = str(value_8)
  if str_i.find('7') == -1 and str_i_8.find('7') == -1:
    count += 1

print(count)

  
