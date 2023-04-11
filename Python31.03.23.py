
numbers = input("Enter numbers with different signs separated by a space: ").split()
numbers = [int(num) for num in numbers]

positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)

print("Positive numbers that were in the list: ", positive_numbers)