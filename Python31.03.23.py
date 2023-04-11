
import random
list = []
for i in range(1,10):
    list.append(random.randint(-10,10))
print(list)
#1
print("\n")
for i in list:
    if i %2 ==0:
        print('Even numbers from the first list:',i)
#2
print("\n")
for i in list:
    if i %2 !=0:
        print('Odd numbers from the first list:',i)
#3
print("\n")
for i in list:
    if i < 0:
        print('Negative numbers from the first list:',i)
#4
print("\n")
for i in list:
    if i > 0:
        print('Positive numbers from the first list:',i)
