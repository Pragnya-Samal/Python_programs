#match statements
#Q1 Use match to print day name based on day number (1-7)
day = int(input("Enter a day number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number. Please enter a number between 1 and 7.")
#Q2 Match a number and print whether it is 10, 20, or 30.
num = int(input("Enter a number: "))
match num:
    case 10:
        print("The number is 10.")
    case 20:
        print("The number is 20.")
    case 30:
        print("The number is 30.")
    case _:
        print("The number is not 10, 20, or 30.")

#Q3 Create a menu-driven calculator using match-case.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
match operator:
    case '+':
        result = num1 + num2
        print("sum",result)
    case '-':
        result = num1 - num2
        print("sub",result)
    case '*':
        result = num1 * num2
        print("mul",result)
    case '/':
        if num2 != 0:
            result = num1 / num2
            print("div",result)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please enter one of +, -, *, /.")
           

#Q4 Match a character and check vowel or consonant.
char = input("Enter a single alphabet character: ").lower()
match char:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(char," is a vowel.")
    case _ if char.isalpha():
        print(char," is a consonant.")
    case _:
        print("Invalid input. Please enter a single alphabet character.")
        
#Q5 Use match to display month name based on month number.
month = int(input("Enter a month number (1-12): "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number. Please enter a number between 1 and 12.")
        

#Q6 Match arithmetic operator (+,-,*,/) and perform operation.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /): ")
match operator:
    case '+':
        result = num1 + num2
        print("sum",result)
    case '-':
        result = num1 - num2
        print("sub",result)
    case '*':
        result = num1 * num2
        print("mul",result)
    case '/':
        if num2 != 0:
            result = num1 / num2
            print("div",result)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please enter one of +, -, *, /.")

#Q7 Match user role (admin, user, guest) and print permissions.
role = input("Enter user role (admin, user, guest): ").lower()
match role:
    case 'admin':
        print("Admin permissions: Full access to all resources.")
    case 'user':
        print("User permissions: Limited access to resources.")
    case 'guest':
        print("Guest permissions: Read-only access to public resources.")
    case _:
        print("Invalid role. Please enter 'admin', 'user', or 'guest'.")

#Q8 Match HTTP status codes (200, 404, 500)
status = int(input("Enter an HTTP status code (200, 404, 500): "))
match status:
    case 200:
        print("200 OK: The request has succeeded.")
    case 404:
        print("404 Not Found: The requested resource could not be found.")
    case 500:
        print("500 Internal Server Error: The server encountered an unexpected condition.")
    case _:
        print("Unknown status code. Please enter 200, 404, or 500.")

#Q9 Match grade (A, B, C) and print remark
grade = input("Enter a grade (A, B, C): ").upper()
match grade:
    case 'A':
        print("Grade A: Excellent work!")
    case 'B':
        print("Grade B: Good job!")
    case 'C':
        print("Grade C: Needs improvement.")
    case _:
        print("Invalid grade. Please enter A, B, or C.")
        
#Q10 Match traffic signal colors and print action
signal = input("Enter traffic signal color (red, yellow, green): ").lower()
match signal:
    case 'red':
        print("Red signal: Stop.")
    case 'yellow':
        print("Yellow signal: Prepare to stop.")
    case 'green':
        print("Green signal: Go.")
    case _:
        print("Invalid signal color. Please enter 'red', 'yellow', or 'green'.")

#Q11 Match a tuple (x, y) and identify quadrant.
point = input("Enter a point (x, y) as comma-separated values: ")
try:
    x_str, y_str = point.split(',')
    x = float(x_str.strip())
    y = float(y_str.strip())
    match (x, y):
        case (x, y) if x > 0 and y > 0:
            print("The point is in the first quadrant.")
        case (x, y) if x < 0 and y > 0:
            print("The point is in the second quadrant.")
        case (x, y) if x < 0 and y < 0:
            print("The point is in the third quadrant.")
        case (x, y) if x > 0 and y < 0:
            print("The point is in the fourth quadrant.")
        case _:
            print("The point is on the origin or on an axis.")
except ValueError:
    print("Invalid input. Please enter the point in the format x,y.")
    

#Q12 Match list length and print custom message.
my_list = list(input("Enter a list of items separated by commas: "))
match len(my_list):
    case 0:
        print("The list is empty.")
    case 1:
        print("The list has one item.")
    case 2:
        print("The list has two items.")
    case _:
        print("The list has", len(my_list), "items.")
        

#Q13 Match dictionary keys and display values.
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
key = input("Enter a key to look up (name, age, city): ").lower()
match key:
    case 'name':
        print("Name:", my_dict['name'])
    case 'age':
        print("Age:", my_dict['age'])
    case 'city':
        print("City:", my_dict['city'])
    case _:
        print("Key not found. Please enter 'name', 'age', or 'city'.")
    

#Q14 Match multiple values using operator.
color = input("Enter a color (red, green, blue): ").lower()
match color:
    case 'red' | 'green' | 'blue':
        print("You chose a primary color:", color)
    case _:
        print("Invalid color. Please enter 'red', 'green', or 'blue'.")

#Q15 Match string commands like "start", "stop", "exit".
command = input("Enter a command (start, stop, exit): ").lower()
match command:
    case 'start':
        print("Command 'start' received. Starting the process.")
    case 'stop':
        print("Command 'stop' received. Stopping the process.")
    case 'exit':
        print("Command 'exit' received. Exiting the program.")
    case _:
        print("Invalid command. Please enter 'start', 'stop', or 'exit'.")


#Q16 Match number ranges using guards (if).
number = int(input("Enter a number: "))
match number:
    case n if n < 0:
        print("The number is negative.")
    case n if n == 0:
        print("The number is zero.")
    case n if n > 0:
        print("The number is positive.")
    

#Q17 Create a simple ATM menu using match.
atm_command = input("Enter an ATM command (withdraw, deposit, balance): ").lower()
match atm_command:
    case 'withdraw':
        amount = float(input("Enter the amount to withdraw: "))
        print(f"Withdrawing ${amount:.2f} from your account.")
    case 'deposit':
        amount = float(input("Enter the amount to deposit: "))
        print(f"Depositing ${amount:.2f} into your account.")
    case 'balance':
        print("Your current balance is $1000.00")  # Example balance
    case _:
        print("Invalid command. Please enter 'withdraw', 'deposit', or 'balance'.")
        

#Q18 Match shape name and calculate area.
shape = input("Enter a shape (circle, square, rectangle): ").lower()
match shape:
    case 'circle':
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * radius ** 2
        print(f"The area of the circle is: {area:.2f}")
    case 'square':
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        print(f"The area of the square is: {area:.2f}")
    case 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area:.2f}")
    case _:
        print("Invalid shape. Please enter 'circle', 'square', or 'rectangle'.")

#19 Match weekday/weekend and print working status.
day_type = input("Enter a day type (weekday, weekend): ").lower()
match day_type:
    case 'weekday':
        print("It's a weekday. Time to work!")
    case 'weekend':
        print("It's the weekend. Time to relax!")
    case _:
        print("Invalid input. Please enter 'weekday' or 'weekend'.")
        
#Q20 Rewrite an if-elif ladder program using match-case.(eg:- find largest of three numbers)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
match (a, b, c):
    case (a, b, c) if a >= b and a >= c:
        largest = a
    case (a, b, c) if b >= a and b >= c:
        largest = b
    case (a, b, c) if c >= a and c >= b:
        largest = c
print("The largest number is:", largest)

