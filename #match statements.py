#match statements
print("Menu:")
print("1 for coffee")  
print("2 for tea")
print("3 for juice")
print("4 for water")
print("5 for soda")
choice=int(input("Enter a number between 1 and 5: "))
match choice:
    case 1:
        print("Your order is coffee.")
    case 2:
        print("Your order is tea.")
    case 3:
        print("Your order is juice.")       
    case 4:
        print("Your order is water.")
    case 5:
        print("Your order is soda.")
    case _:
        print("Invalid choice.")
#weekend program
day=input("Enter a day of the week: ").lower()
match day:
    case "saturday" :
        print("It's the weekend ")
    case "sunday" :
        print("It's the weekend ")
    case _:
        print("It's a weekday.")
#weekdays program
day=int(input("Enter a number for day of the week: "))
match day:
    case 1:
        print("It's Monday.")
    case 2:
        print("It's Tuesday.")
    case 3:
        print("It's Wednesday.")
    case 4:
        print("It's Thursday.") 
    case 5:
        print("It's Friday.")
    case 6:
        print("It's Saturday.")
    case 7:
        print("It's Sunday.")
    case _:
        print("Invalid day number.")
#trafic light program
colour=input("Enter a traffic light color (red, yellow, green): ").lower()
match colour:
    case "red":
        print("Stop.")
    case "yellow"|"orange":
        print("Get ready.")
    case "green":
        print("Go")
    case _:
        print("Invalid color.")
#vowel or consonant program
letter=input("Enter a letter: ").lower()
match letter:
    case "a" | "e" | "i" | "o" | "u":
        print(" It is a vowel.")
    case _ if letter.isalpha() and len(letter) == 1:
        print("It is a consonant.")
    case _:
        print("Invalid input. Please enter a single letter.")
#positive negative program
num=int(input("Enter a number: "))
match num:
    case 0:
        print("The number is zero.")
    case _ if num > 0:
        print("The number is positive.")
    case _ if num < 0:
        print("The number is negative.")
    case _:
        print("The number is invalid.")
#calculator program
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")
match operation:
    case "+":
        print("Addition",num1+num2)
    case "-":
        print("Subtraction",num1-num2)
    case "*":
        print("Multiplication",num1*num2)
    case "/":
        if num2 != 0:
            print("Division:",num1/num2)
        else:
            print("Error: Division by zero.")
    case _:
        print("Invalid operation.")
#even odd program
num=int(input("Enter a number: "))
match num%2==0:
    case 0:
        print("The number is even.")
    case 1:
        print("The number is odd.")
    case _:
        print("Invalid input.")
        
        
#login credentials program
username=input("Enter username: ")
password=input("Enter password: ")
match (username, password):
    case ("admin", "1234"):
        print("Login successful.")
    case ("sneha", "ren34"):
        print("Login successful.")
    case _:
        print("Invalid credentials.")

    