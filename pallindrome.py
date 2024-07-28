# 12321
num=int(input("Enter your number"))
number=num
reverse=0
while(number>0):
    rem=number%10
    reverse=(reverse*10)+rem
    number=number//10

if num==reverse:
    print("The number is pallindrome number")

else:
    print ("The number is not pallindrome number")
