#PROBLEM 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallestDiv = 0
n = 20

def checkDiv(n):
    for i in range(1, 21):
        if n % i != 0:
            break
    else:
        smallestDiv = n
        return


while smallestDiv == 0:
    print(n)
    n += 20
    checkDiv(n)


print(smallestDiv)
