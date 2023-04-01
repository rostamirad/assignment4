import qrcode
name = input("please enter your first and last name: ")
phone_number = int(input("please enter your phone number: "))
total_information = [name, phone_number]

qr_code = qrcode.make(total_information)
qr_code.save("assignment2.png")