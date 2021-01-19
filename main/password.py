password_file = open('password.txt')
password = password_file.read()
typed_password = input("Enter password: ")
if typed_password == password:
    print("Access granted")
    if typed_password == '1234':
        print("That's a stupid password")
else:
    print("Access denied")
