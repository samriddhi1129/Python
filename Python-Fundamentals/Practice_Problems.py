l=[
    ("Alice","Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "english"),
    ("Charlie","english")
]
############################## Ques 1 #######################3
s= set()

# first method

# for i in range(len(l)):
#     s.add(l[i][1])
# print(s)

#second method

for name, course in l:
    s.add(course)
print(s)
    
################## Ques 2 ####################33

for name, course in l:
    if(course == "english"):
        print(name)


##############33 Ques3 ###################

d = {}
for name, course in l:
    if(d.get(name) == None):
        d.update({name:set()} )
        d[name].add(course)
    else:
        d[name].add(course)
print(d)