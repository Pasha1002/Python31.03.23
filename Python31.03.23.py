
import random
list = []
for i in range(1,10):
    list.append(random.randint(-10,10))
print(list)
#1
print('\n')
even_numbers = 0
odd_numbers = 0 
for i in list:
    if i %2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print('Number of even numbers:',even_numbers)
print('Number of odd numbers:',odd_numbers)