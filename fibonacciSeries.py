print("     welcome to fibonacci series")
number1 = 0
number2 = 1
next_number = 0
for number in range(0, 11):
    print(next_number, end=" ")
    number1, number2 = number2, next_number
    next_number = number1 + number2 