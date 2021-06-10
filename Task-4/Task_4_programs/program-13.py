def addition(*number):
    sum = 0

    for n in number:
        sum = sum + n
        print("Addition: ",sum)

addition(65, 35, 40)
addition(60, 10)        