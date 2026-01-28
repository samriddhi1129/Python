salary =int(input("Enter salary: "))
if(salary < 30000):
    tax = 0.05*salary
elif(salary >= 30000 and salary <= 70000):
    tax = 0.15*salary
else:
    tax = 0.25* salary
print(tax)
