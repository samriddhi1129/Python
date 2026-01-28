def calculator(a, b, operation):
    if(operation == '+'):
        return a+b
    elif(operation == '-'):
        return a-b
    elif(operation == '*'):
        return a*b
    else:
        return a/b
print(calculator(30,5,'+'))