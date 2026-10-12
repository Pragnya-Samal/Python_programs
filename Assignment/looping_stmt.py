#Qlooping statement assignment 
#Q1 numbers from 1 to 10 using a loop
num=1
while num <= 10:
    print(num)
    num += 1
#Q2 even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#Q3 the sum of first N natural numbers.
N = int(input("Enter a positive integer N: "))
sum = 0
for i in range(1, N + 1):
    sum += i
print("The sum of first", N, "natural numbers is:", sum)
#Q4 multiplication table of a given number.
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(num, "x" ,i," = ",(num * i))
#Q5 count the number of digits in a given number.
number = int(input("Enter a number to count its digits: "))
count = 0
while number != 0:
    number //= 10
    count += 1
print("The number of digits is:", count)
#Q6 reverse a number using a while loop.
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("The reversed number is:", reversed_number)
#Q7 Find the factorial of a number.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("The factorial of", number, "is:", factorial)
#Q8 Print all prime numbers between 1 and 50.
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
#Q9 Check whether a number is prime or not.
number = int(input("Enter a number to check if it is prime: "))
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
#Q10 Find the sum of digits of a number.
number = int(input("Enter a number to find the sum of its digits: "))
sum_of_digits = 0
while number != 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("The sum of the digits is:", sum_of_digits)
#Q11 Print Fibonacci series up to N terms.
N = int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
for _ in range(N):
    print(a)
    a, b = b, a + b 
#Q12 Print all Armstrong numbers between 100 and 1000.
for num in range(100, 1000):
    sum_of_cubes = 0
    temp = num
    while temp != 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == num:
        print(num)
#Q13 Find the product of digits of a number.
number = int(input("Enter a number to find the product of its digits: "))
product = 1
while number != 0:
    digit = number % 10
    product  *= digit
    number //= 10
print("The product of the digits is:", product)
#Q14 Print pattern right angle triangle
rows = int(input("Enter the number of rows for the pattern: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#Q15 Find the largest element in a list using loop.
numbers = [34, 67, 23, 89, 12, 90, 45]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest element in the list is:", largest)
#Q16 Count how many even and odd numbers are in a list.
numbers = [10, 23, 45, 66, 78, 91, 34, 57]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
#Q17 Print numbers from 1 to 100 skipping multiples of 5.
for num in range(1, 101):
    if num % 5 == 0:
        continue
    print(num)
#Q18 Calculate power of a number without using **.
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
result = 1
for _ in range(exponent):
    result *= base
print("base raised to the power of exponent is :", result)
#Q19 Find the GCD of two numbers using loop.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
while num2 != 0:
    num1, num2 = num2, num1 % num2
print("The GCD is:", num1)
#Q20 Print a number pyramid using loops.
rows = int(input("Enter the number of rows for the number pyramid: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
