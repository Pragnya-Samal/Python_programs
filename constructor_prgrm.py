set1=set((10,20,30,40,50))
print("Set:", set1)
list1=list((1,2,3,4,5))
print("List:", list1)
tuple1=tuple((100,200,300,400,500))
print("Tuple:", tuple1)
dict1=dict(name="Pragnya", age=21, branch="CSE")
print("Dict:", dict1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Person("Pragnya", 21)
person1.display()
w=list((1,2,"hi",4.5,True))
print(w)
z=set((1,2,8,9,"hello"))
print(z)
y=tuple(("apple","banana",3,4.5))
print(y)
d=dict(name="Rohan",age=22,branch="ECE")
print(d)
