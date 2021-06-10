# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder=0.
# If the remainder is 1, then it is an odd number.

num = int(input("Enter a number: "))

if (num % 2) == 0:
   print(num," is Even")
else:
   print(num," is Odd")
   