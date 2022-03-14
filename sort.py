import math 


def selection_sort(A):

	n = len(A)
	for i in range(n):
		mini = i
		for j in range(i+1,n):
			if A[j] < A[mini]: mini = j

		tmp = A[i]
		A[i] = A[mini]
		A[mini] = tmp
		
	return A


def bubble_sort(A):
	n = len(A)

	for i in range(n-1):
		for j in range(n-1-i):
			if A[j]>A[j+1]:
				tmp = A[j]
				A[j]=A[j+1]
				A[j+1]=tmp
	return A


def insertion_sort(A):
	n = len(A)

	for i in range(n):
		tmp = A[i]
		j= i-1

		while j>=0 and tmp < A[j]:
			A[j+1]=A[j]
			j-=1

	return A


def merge_sort(A):

	if len(A) > 1:
		mid = math.floor(len(A))
		S1=A[:mid]
		S2=A[mid:]
		merge_sort(S1)
		merge_sort(S2)
		merge(S1,S2,A)

	return A


def merge(S1,S2,A):
	i=j=k=0
	p=len(S1)
	q=len(S2)

	while i<p and j<q:
		if S1[i] <= S2[i]:
			A[k]=S1[i]
			i+=1

		else:
			A[k]=S2[j]
			j+=1
		k+=1
	if i==p:
		A[k:]=S2[j:]
	else:
		A[k:]=S1[i:]
	return A

A=[2,3,5,1,7,3]

# A.sort()

print(selection_sort(A))
print(bubble_sort(A))
print(insertion_sort(A))
print(merge_sort(A))







