number=int(input("Enter your number "))

flag=0
if number >1:
    for i in range(2,number):
        if(number%i)==0:
            flag=1
            break

if flag==1:
    print("Number is not prime number")
else:
    print("Number is prime number")
