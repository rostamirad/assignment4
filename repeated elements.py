print("If you don't want to enter a number, write 00")

array = []
new_array = []

while True:
    item = int(input("enter a number: "))

    if item == 00:
        print("finish")
        break

    else:
        array.append(item)

for i in array:
    if i not in new_array:
        new_array.append(i)
print("input list: ", array, "output: ", new_array)