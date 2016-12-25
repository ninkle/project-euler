#PROBLEM 2: By considering the terms in the Fibonacci sequence
#whose values do not exceed four million, find the sum of the even-valued terms.

first = 1
second = 2
total = 2

while second < 4000000:
    third = first + second
    if (third % 2 == 0):
        total += third
    first = second
    second = third

print(total)
        
