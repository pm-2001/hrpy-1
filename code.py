n = int(input("enter your number\n"))
if n%2 != 0 :
    print("Weird")
elif (n%2 == 0) and 2<=n<=5 :
    print("Not Weird")
elif (n%2 == 0) and 6<=n<=20 :
    print("Weird")
elif (n%2 == 0) and 20<n<=100 :
    print("Not Weird")
else :
    print("out of range")