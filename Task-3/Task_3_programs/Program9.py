# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder=0.
# If the remainder is 1, then it is an odd number.

num = int(input("Enter a number: "))
if(num<100):
    print(num,"is less than 100")

    if (num % 2) == 0:
        print (num," is Even")
    else:
        print (num," is Odd")
else:
    print(num,"is greater than or equal to 100")