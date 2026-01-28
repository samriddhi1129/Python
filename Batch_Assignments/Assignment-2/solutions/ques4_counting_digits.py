n = int(input("enter number:"))
count = 0
while(n>0):
    count+=1
    n//=10
print(count)