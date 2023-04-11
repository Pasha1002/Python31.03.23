
numbers = input("Enter numbers separated by a space: ").split()
numbers = [int(num) for num in numbers]

arithmetic_mean = sum(numbers) / len(numbers)

count = 0
for num in numbers:
    if num > average:
        count += 1

print("The number of numbers greater than the arithmetic mean:", count)