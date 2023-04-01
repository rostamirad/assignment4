number = int(input("please enter the number you want: "))

factorial = counter = 1


if number <0:
     print("Sorry, Factorial dose not exist for negative numbers. ")

elif number == 0:
        print("The Factorial of 0 is 1. ")

while True:
        counter += 1
        factorial *= counter
        if factorial == number:
            print("yes")
            print(number, " = ", counter, "!")
            break
        elif factorial > number:
            print("no")
            break