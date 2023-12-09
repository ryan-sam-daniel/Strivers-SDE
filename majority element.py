def findMajorityElement(arr, n):
	# Write your code here.
	floor=n/2
	num={}
	for element in arr:
		if element in num:
			num[element]+=1
		else:
			num[element]=1
	max_count=0
	majority_element=-1
	for element,count in num.items():
		if count>max_count:
			max_count=count
			majority_element=element

	if max_count>floor:
		return majority_element
	else:
		return -1
