import math
def fibbo(n):
	phi, psi  = (1 + math.sqrt(5))/2, (1 - math.sqrt(5))/2
	return  (phi**n - psi**n)/math.sqrt(5)
val = input("Enter a number: ")
print fibbo(val)









