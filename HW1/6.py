import re
import string

n = int(input())

result = []

for i in range(n):
	arr = []
	found_list = []
	arr = input()
	len_arr = len(arr)
	found = re.fullmatch('((100+1+)|(01))+',arr)
	if found != None:
		result.append(1)
	else:
		result.append(0)
		
for k in range(n):
	if result[k] == 1:
		print("DANGER")
	else:
		print("PASS")
