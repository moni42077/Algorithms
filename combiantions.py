

def comb(n,k):

	if k==0 or n==k : return 1
	
	return comb(n-k,k-1)+comb(n-1,k)




print(comb(4,2))