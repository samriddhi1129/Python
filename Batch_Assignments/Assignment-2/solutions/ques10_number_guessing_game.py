num = 25  # already decided by me
n = int(input("enter ur guess no:"))
if(num == n):
    print("correct guess")
elif(n>num):
    print("Too high")
else:
    print("Too low")