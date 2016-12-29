#PROBLEMS 4: find the largest palindrome made from the product of two 3-digit numbers

pal = 0

def checkPal(n):
	m = str(n)
	if m == m[::-1]:
		return True
	else:
		return False


for i in range(100, 1000):
    for j in range(100, 1000):
        k = i*j
        if checkPal(k) and k > pal:
            pal = k

print(pal)
