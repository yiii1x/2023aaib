a = [1, 3, 5, 7, 9, 11, 13, 15, 17]
for i in range(4):
  print('第i個數字是', a[i])
print('上面迴圈不好，下面迴圈才會伸縮自如')
N = len(a) #要先知道有幾個數字 a陣列的長度
for i in range(N): #才能在for迴圈裡得到正確的range
  print('第i個數字是', a[i])