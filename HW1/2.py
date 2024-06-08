def partition(arr,l,r):
	q = arr[l]
	i = l+1
	j = r
	
	while True:
		while arr[i] <= q and i < r:
			i = i + 1
			
		while arr[j] > q and j >= l:
			j = j - 1
			
		if i < j:
			arr[i],arr[j] = arr[j],arr[i]
		else:
			break
		
	arr[l],arr[j] = arr[j],arr[l]
        
	return j

def quicksort(arr,l,r):
	if l < r:
		p = partition(arr,l,r)
		quicksort(arr,l,p-1)
		quicksort(arr,p+1,r)


q_list = list(map(int,input().split()))
q_len = len(q_list)
	
quicksort(q_list,0,q_len-1)

print(q_list)

