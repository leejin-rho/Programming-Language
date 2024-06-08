def merge(l,r):
	i = 0
	j = 0
	l_l = len(l)
	r_l = len(r)
	buffer = []

	while (i < l_l) and (j < r_l):
		if l[i] < r[j]:
			buffer.append(l[i])
			i+=1
		else:
			buffer.append(r[j])
			j+=1
	while(i < l_l): #위의 while문에서 탈출했지만 아직 left의 데이터가 남았을 경우
		buffer.append(l[i])
		i+=1
	while(j < r_l):
		buffer.append(r[j])
		j+=1
	return buffer

	
def merge_sort(arr):
	if len(arr)>1:
		m = len(arr)//2
		left = arr[:m]
		right = arr[m:]
		
		left_s = merge_sort(left)
		right_s = merge_sort(right)
	
		return merge(left_s,right_s)
	else:
		return arr


m_list = list(map(int,input().split()))
m_len = len(m_list)
	
print(merge_sort(m_list))
