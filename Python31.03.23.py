
numbers = input("Enter the numbers through the space: ").split()
numbers = [int(num) for num in numbers]

squaeres_of_numbers = []
for num in numbers:
    if num > 0:
        squaeres_of_numbers.append(num**2)

print("Squares of the numbers in the list: ", squaeres_of_numbers)