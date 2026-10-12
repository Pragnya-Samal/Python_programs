student={"name":"Pragnya","age":21,"branch":"CSE","marks":(20,50,40,78,99)}
print("Student Dictionary:",student)
print("Student Name:",student["name"])
print("Student Age:",student["age"])
print("Student Branch:",student["branch"])
print(type(student))

student["age"]=22
print("Updated Student Age:",student["age"])

dict1=dict(name="Pragnya",age=21,branch="CSE",marks=(20,50,40,78,99))
print("Student Dictionary:",dict1)

x = student["name"]
print(x)
y=student.get("branch")
print(y)
z=student.keys()
print(z)
w=student.values()
print(w)
l=student.items()
print(l)
student["branch"]="ECE"
print(student)
student.update({"age":23})
print(student)
student["city"]="Bangalore"
print(student)
student.pop("marks")
print(student)
student.popitem()
print(student)
del student["age"]
print(student)

s=dict(fruit="apple",color="red",quantity=5)
print(s)
print(s.keys())
print(s.values())
print(s.items())
print(s.get("color"))
fruit={"banana":10,"orange":15,"grape":20,"mango":25,"kiwi":30}
print(sum(fruit.values()))
Marks={"Maths":85,"Physics":90,"Chemistry":78,"Biology":88}
print("total marks",sum(Marks.values()))
print("max marks",max(Marks.values()))
print("min marks",min(Marks.values()))
student1=dict(Name="Pragnya",Age=21,Branch="CSE")
student2=dict(Name="Rohan",Age=22,Branch="ECE") 
student3=dict(Name="Anita",Age=20,Branch="ME")
student4=dict(Name="Suresh",Age=23,Branch="CE")
college={"Student 1":student1,"Student 2":student2,"Student 3":student3,"Student 4":student4}
print(college)

