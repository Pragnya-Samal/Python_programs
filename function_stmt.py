'''def add(a,b):
    return a+b
y=add(10,20)
print("Sum:",y)
print("return ",type(y))

def addition(c,d):
    print("Sum:",c+d)
x=addition(30,40)
print(" addition :",x)
print("return ",type(x))


def  greeting(name):
    print("Hello",name)
greeting("Rohan")
greeting("Pragnya")
greeting("Aaluu")


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print(add(10,50))
print(subtract(90,70))
print(multiply(5,6))
print(divide(100,20))

def student(name, rollno, age , section ='J'):  #default argument(section)
        print(f"Hello I am GIETU student, My name is {name},\nI recently joined GIETU college and  my rollno is {rollno}\nand I am in section {section}, \nand my age is {age} ")
student("Pragnya", 578, 21,"I") # positional arguments
student(name="soham", rollno=238, age=22)#keyword arguments
student("Aaluu", 590, 20) # default argument(section)

def fruit(name):
    for i in name:
        print(i)
X=["apple","orange","grapes","strawberry","cherry"]
fruit(X)

def flower(names):
    for i in names:
        print(i)
flowers=("rose","lily","jasmine","sunflower")
flower(flowers)

def stu(*name):
    for i in name:
        print("hi",i)
stu("pragnya","soham","aaluu","mohan","siya")

def stu(*name):
     print("name of student :",name)
     print("type of name :",type(name))
     print("number of students :",len(name))
     print("first student :",name[0])
     print("last student :",name[-1])
stu("pragnya","soham","aaluu","mohan","siya")
def kiddo(**info):
    print("type of info :",type(info))
'''    