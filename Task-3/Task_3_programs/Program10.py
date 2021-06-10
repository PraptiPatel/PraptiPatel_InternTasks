# Python Program to Calculate Square of a Number

number = float(input(" Please Enter any numeric Value : "))

if(number<10):
    square = number * number
    print("The Square of a Given Number {0}  = {1}".format(number, square))
else:
    print(number,"is greater or equal to 10")