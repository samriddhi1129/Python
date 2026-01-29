# string concatenation

# a = "1"+1   error
# print(a)

word1 = "python"
word2 = "easy"
print(word1+word2)
print(word1 + " " + word2)

# we can do indexing in python strings  (negative indexing is also possible)

for i in range(0, len(word1)):
    print(word1[i])

# strings are immutable
# word1[0] = 'j'  ---> not possible to change in existing string

# string slicing

'''
Syntax

word1[starting index : ending index]

'''

################################   String formatting ##########################

'''
1. format() ---> old way
2. f-strings ----> modern way

'''

# format()

# 1. normal formatting
# 2. index based formatting
# 3. value based formatting

a = 5
b = 10
print("The sum of {} & {} is {}".format(a,b,a+b))  # normal formatting
print("The sum of {1} & {0} is {2}".format(a,b,a+b)) # index based formatting
print("The values of {a} & {b} is".format(a=20, b=30)) # value based formatting --> for reusing variable

#############################  fstring ##########################
#1. literal string interpolation
#2. expression or what u want to evaluate should be given in curly braces

print(f"The average of {a} and {b} is {(a+b)/2}")


# lists

# mutable sequence of values


# list slicing

#list methods

'''
1. list_name.append(value)
2. list_name.insert(index, value)
3. list_name.sort()
4. list_name.reverse()
5. list_name.sort(reverse = true)


'''
l = [1,2,3,10,4]
flag = True
for val in l:
    if(val == 10):
        print("found")
        flag = False
if(flag == True):
    print("Not found")



############################## Tuples ##########################3

'''
1. immutable
2. indexing is possible
3. for single value tuple creation: (1,)
4. (1)---> is mathematical expression
5. tuple slicing is possible



'''

tup = (1,2,"sam")
print(tup[:])


# Tuple methods

'''
1. tuple_name.index(val)
2. tuplle_name.count(val)
'''

#################### dictionary ################################3

'''
1. key : value variable
2. list, tuple are ordered but dictionary is unordered

'''

dict = {
    "name":"sam",
    "roll":32,
    3.14:"PI"
}
print(type(dict))


# dictionary methods

'''
1. dict.keys()
2. dict.values()
3. dict.items()
4. dict.get(key)
5. dict.update({key:value}) ---> to add new data item in dictionary

'''

# if we have square notation to access vaue through keys like d[key] = val then why .get() method is used?

'''
.get() method did not give error but [] notation give error if key does not exist

get() methods return None value and code execution did not stop

'''
list(dict.keys())

############################ Sets ############################3

'''
1. collection of unique elements
2. set is mutable but elements inside set is immutable
3. unordered
4. to add new ele: set.add(val)
5. to create empty set : s = set() ---> constructor function

'''
set_ = {1,2,2,2}
print(len(set_))
s = set()
print(s)

# set methods

'''
1. s.remove(element)
2. s.add(element)
3. s.clear()
4. s.pop()
5. s.union(set2)
6. s.intersection(set2)  # return new union for 5th point and new intersection for 6th point
'''