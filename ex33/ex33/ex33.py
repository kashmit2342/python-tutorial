i = 0
numbers = []

while i < 6:
	print(f"number appended is:{i}")
	numbers.append(i)
	i+=1
	print(f"i now is:{i}")

for number in numbers:

	print(number)

print(f"all numbers {numbers}")

print(numbers[2])

