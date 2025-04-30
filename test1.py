##Learn the Basics
##1. Hello, World!
##Write a Python program that prints "Hello, World!" to the console.
print("Hello World")
####2. Variables and Types
####Declare a variable x with the value 10. Assign another variable y with the string "Python". Print both values along with their types.
x=10
st='aadil'
print(f"X={x} and Type:{type(x)}\nName:{st} and Type:{type(st)}")
####3. Lists
####Create a list of five numbers. Write a Python program to find the sum and average of all numbers in the list.
print("Enter 5 numbers")
n=5
lst=[]
for i in range(5):
    num=int(input())
    lst.append(num)
print(f"Average:{sum(lst)/n}")
    
##4. Basic Operators
##Write a Python program that takes two numbers as input and prints their sum, difference, product, and quotient.
val1=int(input("enter an integer value X"))
val2=int(input("enter an integer value Y"))
print(f"Addition:{val1+val2},subtraction:{val1-val2},Multiplicatoion:{val1*val2},Quotient:{val1//val2}")
##
####5. String Formatting
####Given name = "Alice" and age = 25, use different string formatting techniques (%, .format(), and f-strings) to print "Alice is 25 years old."
name='Alice'
age=25
print("%s is %d years old" %(name,age))
print("{} is {} years old".format(name,age))
##6. Basic String Operations
##Write a Python program that takes a string as input and:
##Converts it to uppercase and lowercase.
##Counts the number of vowels in the string.
##Reverses the string.
st=str(input("enetr a string"))
print(st.upper(),st.lower())
count=0
for ch in st.lower():
    if ch in('a','i','o','u','e'):
        count+=1
print(f"Number of vowels are:{count}")
revers_st = "".join(reversed(st))
print(revers_st)

####7. Conditions
####Write a Python program that takes a number as input and checks whether it is even or odd.
num=int(input("enetr a number"))
if(num%2==0):
    print(f"This is even number:{num}")
else:
    print(f"This is odd number:{num}")
##8. Loops
##Write a Python program that prints all prime numbers between 1 and 50.
for i in range(2,51):
    for j in (2,i):
        if i%j==0:
            break
        else:
            print(f"{i}")
    
##9. Functions
##Write a function factorial(n) that returns the factorial of a given number n.
n=int(input("enter a number to find factorial"))
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))
##10. Classes and Objects
##Create a Car class with attributes brand, model, and year. Define a method display_info() that prints car details. Instantiate an object and call the method.
class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display_info(self):
        print(f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}")
car=Car('Toyota','city 100','2022')
car.display_info()
##11. Dictionaries
##Create a dictionary containing three students' names as keys and their scores as values. Write a program to:
##Print all keys and values.
##Find the highest score.
dic={}
for d in range(3):
    key=str(input("Enter student name as key"))
    val=int(input("enter marks of the student as Value"))
    dic[key]=val
for key in dic:
    print(f"Key=>{key}:Value=>{dic[key]}")
##12. Modules and Packages
##Write a Python program that imports the math module and calculates the square root and factorial of a given number.
import math as m
print(m.sqrt(25),m.factorial(5))
##13. Input and Output
##Write a Python program that asks the user for their name and age, then prints a message saying "Hello [name], you are [age] years old!".
name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
print(f"Hello! {name} you are {age} years old")
