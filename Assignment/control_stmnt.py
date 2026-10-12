#if else statement
#Q1check number positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#Q2check even or odd
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Q3find largest among three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
print("The largest number is:", largest)

#Q4check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year is:",year)
else:
    print("not a leap year:",year)
#Q5program to check grade based on marks
marks = float(input("Enter your marks (0-100): "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'
print("Your grade is:", grade)
#Q6check vowel or consonant
char = input("Enter a single alphabet character: ").lower()
if char in 'aeiou':
    print( " vowel.",char)
elif char.isalpha():
    print( " consonant.",char)
else:
    print("Invalid input. Please enter a single alphabet character.")
#Q7check if number is divisible by 5 and 11
num = int(input("Enter an integer: "))
if num % 5 == 0 and num % 11 == 0:
    print("The number  divisible by both 5 and 11:",num)
else:
    print("The number not divisible by both 5 and 11:",num)
#Q8check whether given number is 3 digit number or not
num = int(input("Enter an integer: "))
if num >= 100 and num <= 999:
    print("The number is a three-digit number:",num)
else:
    print("The number is not a three-digit number:",num)
#Q9check a triangle is valid based on three angles
angle1 = float(input("Enter first angle of triangle: "))
angle2 = float(input("Enter second angle of triangle: "))
angle3 = float(input("Enter third angle of triangle: "))
if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
#Q10 calculate electricity bills using slab rates.
#Q11palindrome number
num = int(input("Enter an integer: "))
num_copy=num
sum=0
while num > 0:
    digit = num % 10
    sum = sum * 10 + digit
    num = num // 10
if num_copy == sum:
    print(num_copy, "is a palindrome number.")
else:
    print(num_copy, "is not a palindrome number.")
#Q12find profit or loss based on cp and sp
cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
if sp > cp:
    profit = sp - cp
    print("Profit:", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss:", loss)
else:
    print("No profit, no loss.")
#Q13check if given character is uppercase,lowercase,digit or symbol
char = input("Enter a single character: ")
if char.isupper():
    print(char," is an uppercase letter.")
elif char.islower():
    print(char," is a lowercase letter.")
elif char.isdigit():
    print(char," is a digit.")
else:
    print(char," is a symbol.")
#Q14WAP to determine the type of triangle (equilateral, isosceles, scalene) based on the lengths of its sides.
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))
if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
#Q15Check whether a given number lies between 50 and 100.
num = float(input("Enter a number: "))
if 50 <= num <= 100:
    print("The number lies between 50 and 100.")
else:
    print("The number does not lie between 50 and 100.")
#Q16Write a program to find the second largest of three numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if (a >= b and a <= c) or (a <= b and a >= c):
    second_largest = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    second_largest = b
else:
    second_largest = c
print("The second largest number is:", second_largest)
#Q17 Check if a number is divisible by 3 or 7 but not both.
num = int(input("Enter an integer: "))
if (num % 3 == 0) ^ (num % 7 == 0):
    print("The number is divisible by 3 or 7 but not both:",num)
else:
    print("The number is either divisible by both 3 and 7 or by neither:",num)
#Q18 validate login credentials (username & password).
username = input("Enter username: ")
password = input("Enter password: ")
correct_username = "admin"
correct_password = "password123"
if username == correct_username and password == correct_password:
    print("Login successful.")
else:
    print("Invalid username or password.")
#Q19Check whether a number is a perfect square.
import math
num = int(input("Enter a non-negative integer: "))
sqrt_num = math.isqrt(num)
if sqrt_num * sqrt_num == num:
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")
#Q20 Write a program to calculate bonus: Salary > 50,000→10%, else 5%.
salary = float(input("Enter the salary amount: "))
if salary > 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05
print("The bonus amount is:", bonus)
