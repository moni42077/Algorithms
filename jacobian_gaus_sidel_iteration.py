import math 
import numpy as np 

def Jacobi(A,b,x,c):

	#A*x
	ax = np.dot(A,x)

	#Define D
	D = np.diag(np.diag(A))

	#Inverse of D
	d1 = np.linalg.inv(D) 
	#Calculations 
	diff = b - ax
	mult = np.dot(d1,diff)
	x1 = x + mult
	#coutner 
	c+=1
	print(x1)
	if c<2:
		Jacobi(A,b,x1,c)
	else : return x1 

def GaussSeidel(A,b,x,c):

	#Defibe L,U,D 
	L = np.tril(A)
	U = np.triu(A)
	D = np.diag(np.diag(A))

	#Calculations
	dl = D+L
	dl1 = np.linalg.inv(dl)
	ax = np.dot(A,x)
	diff = b - ax
	mult = np.dot(dl1,diff)
	x1  = x + mult

	c+=1 
	print(x1)
	if c<100:
		print(1)
		GaussSeidel(A,b,x1,c)
	else : return x1 


#initial values for x 
A=np.array([[2,-1,0],[-1,1,3],[1,0,1]])
u=np.array([[0],[0],[0]])
b=np.array([[1],[3],[2]])


x1 = np.array([[0],[0],[0]])
A1 = np.array([[2,1,0],[2,3,0],[0,1,2]])
b1 = np.array([[-1],[1],[0]])


print(GaussSeidel(A,b,u,0))

#GaussSeidel(A1,b1,x1,0)
