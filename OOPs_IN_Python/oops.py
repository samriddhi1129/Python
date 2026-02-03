'''
1. classes are the blueprints for creating objects. 
2. object is the instance of class
3. object takes memory but classses did not
4.  class Student: 
                >> features
5. classes contain the properties or attributes of object and behaviour or function of object
6. In context of oops, functions are called as methods.

'''

# creating class

class Student:
    subject = "Python",
    year = 2,
    college = "GLA"

# creating object

# a = 10
stud1 = Student()
print(stud1)   # output :  <__main__.Student object at 0x00000269593786E0>

stud2 = Student()
print(stud2)

# how to access properties of object using dot notation

print(stud1.subject, stud2.year, stud1.college)   # op: ('Python',) (2,) GLA 
'''
Our output comes in tuple because of comma i give in student class real class structure did not contain comma , see next example

'''
class Faculty:
    department = "CSE"
    experience = 10
fac1 = Faculty()
print(fac1.department, fac1.experience)


# How to create methods in classes

########################################  _init_ method  OR the "Constructor" ##########################

'''
1. constructor is a function which is used to create objects in python
2. __init__ method is always called whenever we create object
3. constructor is used for assigning a single property like name but each student have different name so to tackle this we create __init__
4. By default :  stud1 = Student().............. here parentheses automatically make __init__ function or method if we did not defined in student class


'''


# how to create __init__ method manually?

class Patient:
    def __init__(self):
        print("this is constructor")
'''
1. self is by default parameter in this method and named can be change like we give self as "variable_name"

2. self is basically a "current instance of class"
3. self is compulsory paramenter and all things are called through self only

'''
# how to pass different name to different objects

class Hospital:
    def __init__(self, name,location):
        self.name = name
        self.location = location
hos1 = Hospital("Niyati", "Mathura")
hos2 = Hospital("City hospital", "Delhi")
print(hos1)
print(hos2)
print(hos1.location, hos1.name)

