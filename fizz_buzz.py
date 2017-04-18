def fizzBuzz(num):
	if num > 0:
		if num % 3 == 0 and num % 5 == 0:
			return 'FizzBuzz'
		elif num % 3 == 0:
			return 'Fizz'
		elif num % 5 == 0:
			return 'Buzz'
		else:
			return num

print(fizzBuzz(-4.5))