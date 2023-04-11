
numbers = input("Enter numbers separated by a space: ").split()
numbers = [int(num) for num in numbers]

min_ind = numbers.index(min(numbers))
max_ind = numbers.index(max(numbers))

numbers[min_ind], numbers[max_ind] = numbers[max_ind], numbers[min_ind]

print("A list with changed places of the minimum and maximum elements: ")
print(numbers)