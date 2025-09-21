option = 0
while option != 0:
    message = input("nhap vao di ")
    encrypted = ''
    key = int(input("bac ky "))
    for i in message:
        encrypted += chr(ord(i) + key)
    print(encrypted)
    option = int(input('encrypted or decrypted (1 - 2). 0 to exit: '))

