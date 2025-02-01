#Junior code
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print(squared_numbers)


#Senior code
print([number**2 for number in range(1,6)])
