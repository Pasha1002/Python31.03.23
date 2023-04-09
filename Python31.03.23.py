
import random
list = []
for i in range(1,10):
    list.append(random.randint(-10,10))
print(list)
print("\n")
sum_negative = 0
for num in list:
    if num < 0:
        sum_negative += num 
print('sum_negative',sum_negative)
print("\n")
sum_of_even_numbers = 0 
for num in list:
    if num %2 ==0:
        sum_of_even_numbers += num
print('sum_of_even_numbers',sum_of_even_numbers)
print("\n")
sum_of_odd_numbers = 0
for num in list:
    if num %2 !=0:
        sum_of_odd_numbers += num
print('sum_of_odd_numbers',sum_of_odd_numbers)
print("\n")
product_of_elements = 1
for index,i in enumerate(list):
    if index %3 ==0:
        product_of_elements *= i
print('product_of_elements',product_of_elements)
print("\n")
#for i in list:
#    if max < i:
#        max = i
#    if min > i:
#        min = i
#    print(i)
#print()
#print('max ',max)
#print('min ',min)
print("\n")
summa = 0
for num in list:
    if num > 0:
        summa += num 
print('summa',summa)