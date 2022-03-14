import math

def sequential_search(A,k):
	n = len(A)
	i=0
	while i <= n and A[i]!=k:
		i+=1

	if i<n : return i
	else: return -1

def binary_search(A,k):
	#A is sorted in ascending order
	l = 0
	r = len(A)
	while l<=r:
		mid = math.floor((l+r)/2)
		if k==A[mid]: return mid
		else :
			if k < A[mid] : r=mid-1
			else:l=mid+1
	return -1

def binary_search_rec(A,k):
	#A is sorted in ascending order
	l = 0
	r = len(A)
	while l<=r:
		mid = math.floor((l+r)/2)
		if k==A[mid]: return mid
		else :
			if k < A[mid] : binary_search_rec(A[:mid-1]) 
			else: binary_search_rec(A[mid-1:])
	return -1


A=[1,2,2,3,4,5]

print(sequential_search(A,3))
print(binary_search(A,3))
print(binary_search_rec(A,3))

