n = int(input())

ans = 0
for i in range(1,n):
	ans += i * (i+1)
	
print(ans)