
import random
list = []
for i in range(1,10):
    list.append(random.randint(-10,10))
print(list)
#1
print("\n")
sum_negative = 0
for num in list:
    if num < 0:
        sum_negative += num 
print('sum_negative',sum_negative)
#2
print("\n")
sum_of_even_numbers = 0 
for num in list:
    if num %2 ==0:
        sum_of_even_numbers += num
print('sum_of_even_numbers',sum_of_even_numbers)
#3
print("\n")
sum_of_odd_numbers = 0
for num in list:
    if num %2 !=0:
        sum_of_odd_numbers += num
print('sum_of_odd_numbers',sum_of_odd_numbers)
#4
print("\n")
product_of_elements = 1
for index,i in enumerate(list):
    if index %3 ==0:
        product_of_elements *= i
print('product_of_elements',product_of_elements)
#5
print("\n")
product_between_min_or_max = 1
min_ind = list.index(min(list))
max_ind = list.index(max(list))
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind
for num in list [min_ind+1:max_ind]:
    product_between_min_or_max *= num
print("The product of elements between the minimum and maximum element:", product_between_min_or_max)
#6
print("\n")
pos_ind = [num for num in range(len(list)) if list[num] > 0]
if len(pos_ind) > 1:
    first_pos_ind = pos_ind[0]
    last_pos_ind = pos_ind[-1]
    sum_between_pos = sum(list[first_pos_ind+1:last_pos_ind])
    print("The sum of the elements between the first and the last positive element:", sum_between_pos)
else:
    print("There are no two positive elements in the array.")