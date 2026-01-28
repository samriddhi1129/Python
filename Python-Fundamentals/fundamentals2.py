# age = int(input("Enter age: "))

# #  conditional statements
# # #####################  if ###################
# # if age >= 18:
# #     print("you can vote")
# #     print("you can drive")

# ######################   if elif ############33

# # traffic lights

# color = input("enter color:")

# if color == "red":
#     print("stop")
# elif color == "green":
#     print("GO")
# elif color == "yellow":
#     print("look")

# ###################  if elif else ################33

# if color == "red":
#     print("stop")
# elif color == "green":
#     print("GO")
# elif color == "yellow":
#     print("look")
# else:
#     print("wrong color")



# check if child, teenage , adult

# age = int(input("enter age:"))

# if(age <13):
#     print("child")
# elif(age >=13 and age <18):
#     print("teenage")
# else:
#     print("Adult")


################  nested if ################3


#####################  math case ############

color = input("emter color:")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case _: #default case
        print("Stop")


##############  loops #######################3

# 1. while 
# 2. for loop  (used for sequential traversal)
# 3. do while loop
# 4. infinite loop

for var in "hello":         #to check presence character in string 
    print(var)   

for i in range(0,10):        # for sequence of numbers
    print(i)



# Ques: Multiplication table of any num n
# ques: count no of i's in artificial intelligence
#  ques: count no of vowels in "AI"
# ques: sum of  n numbers
# ques: calculate average of 3 numbers






#######   Break and  continue keyword ##########




##########################  functions in python ###################################

# function definition
# function call(invoke)
# types of function: built in fn, user defined fn


def function_name():
    print("function definition")
function_name()

def sum(a,b):
    s = a+b
    return s
print(sum(3,4))


######################  lambda function ###########################

# function definition

# syntax: lambda (parameters): (expression)

'''
This above line give output of the expression  as an example given below
'''

sum = lambda a,b,c: a+b+c
print(sum(4,5,6))

# lambda function is used in higher order function


# higher order function
'''
It is a function which accepts function as parameter or return function as in return statement

'''


# Factorial of number n using functions
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact
n = int(input("enter number:"))
ans = factorial(5)
print(ans)


   







