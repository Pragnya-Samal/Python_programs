'''set1=set()
set1.add(10)
set1.add(20)
set1.add(30)
print(type(set1))
print("Set after adding elements:", set1)
print("Set after removing 20:", set1.remove(20)) 
print("Set after discarding element:", set1)
set1.add(60)
set2={30,40,50}
set1.update(set2)
print("Set after updating with set2:", set1)
print("pop element from set1:", set1.pop())
print("Clear set1:", set1.clear())

#applying functions of dictionary on set
set3={10,20,30,40,50}
print("Length of set3:", len(set3))
print("Max of set3:", max(set3))
print("Min of set3:", min(set3))
print("Sum of set3:", sum(set3))

#set functions implementation
setA={1,2,3,4,5,6}
setB={5,6,7,8,9}
print("Union of setA and setB:", setA.union(setB))
print("Intersection of setA and setB:", setA.intersection(setB))
print("Difference of setA and setB:", setA.difference(setB))
print("Difference of setB and setA:", setB.difference(setA))
print("Symmetric difference of setA and setB:", setA.symmetric_difference(setB))
print("Is setA a subset of setB?:", setA.issubset(setB))
print("Is setA a superset of setB?:", setA.issuperset(setB))
print("Are setA and setB disjoint?:", setA.isdisjoint(setB))
print("symbolic representation of setA:", repr(setA))
print("symbolic representation of setB:", repr(setB))
print(setA|setB)
print(setA&setB)
print(setA-setB)
print(setB-setA)
print(setA^setB)
'''
registered=set()
n=int(input("Enter number of users to register in erp : "))
for i in range(n):
    user=input("Enter userrollno. (eg:- 23cse578) : ")
    if user.isalnum():
        registered.add(user)
print("Registered users:", registered)
present=set()
m=int(input("Enter number of users present today : "))
for j in range(m):
    user=input("Enter userrollno. (eg:- 23cse578) : ")
    if user in registered:
        present.add(user)
    else:
        registered.add(user)
        print(f"User {user} is not registered.")
print("Present users:", present)
absent_users=registered - present
print("Absent users:", absent_users)
print("Total registered users:", len(registered))
print(registered)
print("Total present users:", len(present))
print(present)
