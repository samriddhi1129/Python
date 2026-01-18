# question1: Write a program that asks the user for their name and age,then prints sentence like: Hello (My name), you are (ur age) years old!

name = input("enter your name")
age = int(input("Enter your age:"))

print("Hello", name, "you are",age,"years old!")


# # q2: Take two numbers as input from the user and print their sum,difference,product,and quotient

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
sum = (n1+n2)
diff = n1-n2
product = n1*n2
q= n1/n2
print(sum, diff, product, q)

# q3: Ask the user to enter two integers and one float.Convert them all to float and print their average.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c = float(input("enter floating value:"))
print((float(a) + float(b) + c)/3)


''' The user enters a string containing a number(e.g."45").Convert it to:
a) integer
b) float
c) string again

Print all three values with their types

'''
s=input("enters a string containing a number(e.g.'45'): ")
print(int(s), type(int(s)))
print(float(s),type(float(s)))
print(str(s), type(str(s)))


'''
q5:
Evaluate and print the result of the following expression:
x =10+3*2**2
 Based on what you learnt in the lecture explain why the output is what it is.


'''
x =10+3*2**2
print(x)

'''
q6: WAP to swap two numbers
'''

x=int(input("enter first no: "))
y = int(input("enter second number: "))
temp = x
x= y
y=temp
print(x, y)


'''
 q7: Ask the user for a temperature in Celsius(stringinput).Convert it to, float then calculate and print temperature in Fahrenheit.Conversion formula:FahrenheitTemp=(CelsiusTemp∗(9/5))+32

'''
temp=input("enter temp in celsius:")

f = float(temp)*(9/5)+32
print(f)

'''
q8: print area of circle
'''
r = float(input("enter radius:"))
print(3.14*r*r)

#q9:  calculate simple interest

p = float(input("enter principal:"))
rate = float(input("enter rate:"))
time = float(input("enter time:"))
print((p*rate*time)/100)

'''
q10:
Take a decimal number as input(like = 45.78) and output its
•integerpart- 45
•fractionalpart- .78
'''
ans = float(input("enter decimal num: "))
print("its integer part:", int(ans))
print("its fractional part:", round(ans-int(ans),2))
