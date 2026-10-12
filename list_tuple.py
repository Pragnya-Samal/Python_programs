#list functions
l1=[1,2,3,4,5]
l2=["apple","banana","cherry"]
l3=[1,"apple",3.14,True]
print("Type of l1:",type(l1))
print("Type of l2:", type(l2))
print("Type of l3:", type(l3))
print("Length of l1:", len(l1))
print("Append function", l1.append(6) or l1)
print("Remove 2 from list", l1.remove(2) or l1)
print("Insert 10 at index 1 in l1:", l1.insert(1,10) or l1)
print("Pop element", l1.pop() or l1)
print("Sort l1:", l1.sort() or l1)
print("Reverse l1:", l1.reverse() or l1)
print("Index of 3 in l1:", l1.index(3) or l1)
print("Count occurrences of 4 in l1:", l1.count(4))
print("Extend l1 with [7,8,9]:", l1.extend([7,8,9]) or l1)
print("Clear l2:", l2.clear())
print("remove function", l3.remove(3.14) or l3)
print("discaard function", l3.clear() or l3)
#adding function
l4=[32,55,12,78,4,90,29]
print("Sum of l4:", sum(l4))
print("Max of l4:", max(l4)) 
print("Min of l4:", min(l4))
print("Sorted l5:", sorted(l4))


#tuple functions
t1=(1,2,3,4,5)
print("Type of t1:", type(t1))
print("Length of t1:", len(t1))
print("Index of 3 in t1:", t1.index(3))
print("Count occurrences of 4 in t1:", t1.count(4))
t2=("apple","banana","cherry")
print("Type of t2:", type(t2))
print("Length of t2:", len(t2))
print("Index of 'banana' in t2:", t2.index("banana"))
print("Count occurrences of 'apple' in t2:", t2.count("apple"))
