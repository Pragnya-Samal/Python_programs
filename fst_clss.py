#even_odd
num=int(input("enter a number: "))
if num%2==0:
    print("even number ")
else:
    print("odd number ")
#palindrome number
n=int(input("enter a number: "))
temp=n
rem=0
sum=0
while n>0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
if temp==sum:
    print("palindrome number")
else:
    print("not a palindrome number")
#fibbonacci series
m=int(input("enter a number: "))
a=0
b=1
for i in range(0,m):
    print(a)
    c=a+b
    a=b
    b=c
    
#prime number
n=int(input("enter number: "))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
if count==1:
    print("prime number")
else:
    print("not a prime number")
#factorial of number
m=int(input("enter a number "))
fact=1
for i in range(1,m+1):
    fact=fact*i
print("factorial of number is ",fact)


#find largest ele in list
l=[17,92,23,48,95,60]
k=l.sort()
print("largest element",l[-1])


#find  2nd largest ele in list
l=[13,24,58,67,98,70]
p=l.sort()
print("second largest element",l[-2])

#remove duplicate from list using set
l=[14,59,35,71,94,3,57,61]
s=set(l)
l=list(s)
print("list after removing duplicate",s)

#count vowels in a string
s=input("enter a string and give space between words  ")
count=0
for i in s:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' or i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
print("number of vowels in string is ",count)


#find reverse a string
s=input("enter a string ")
reverse=s[::-1]
print("reverse of string is ",reverse)

#frequency of a character
s=input("enter a string  ")
char=input("enter a character  ")
f=0
for i in s:
    if i==char:
        f+=1
    else:
        pass
print("frequency of character",char, " is ",f)

#move zero to end
l3=[0,1,0,3,12]
l4=[]
l5=[]
for i in l3:
    if i==0:
        l4.append(i)
    else:
        l5.append(i)
l_final=l5+l4
print("final list ",l_final)


#reverse the words in string (position is same of words)
wrd=input("enter a string ")
l=wrd.split()
for i in l:
    print(i[::-1],end="  ")


#merge two sorted list
l1=[90,2,29,35,19,49,79]
l2=[17,92,23,48,95,60]
l1.sort()
l2.sort()
l3=l1+l2
print("merged list ",l3)        
#linear search
lii=[17,92,23,48,95,60,45,78,12,34]
key=int(input("enter a number to search "))
for i in range(len(lii)):
    if lii[i]==key:
        print("element found at index ",i)
        break
else:
    print("element not found")
