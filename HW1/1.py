b_list = []

b_list = list(map(int,input().split()))
key = int(input())

m = 0
l = 0
u = len(b_list)
	
while u >= l:
	m = int((l + u) / 2)
		
	if key < b_list[m]:
		u = m - 1
	elif key > b_list[m]:
		l = m + 1
	else:
		print(m+1)
		break
		
if(u < l):
	print('None')
