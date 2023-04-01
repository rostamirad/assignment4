print("If you don't want to enter a number, write 00")

array = []

while True:
    item = int(input("enter a number: "))

    if item == 00:
        print("finish")
        break

    else:
        array.append(item)

print("your list of numbers is: ", array, "and the revers list is: ", array[::-1])
