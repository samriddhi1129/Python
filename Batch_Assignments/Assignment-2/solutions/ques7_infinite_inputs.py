while(True):
    n = input("enter a number or write 'quits' if you want to quit")
    if(n=="quits"):
        break
    elif(int(n) >= 0):
        print("positive")
    else:
        print("negative")
    