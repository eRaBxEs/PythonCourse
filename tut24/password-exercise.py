"""

Write a program that asks user to enter a password and tries to compare it 
to a hard-coded password.

If the password is correct, the program prints "Greetings Professor 
Falcon" and exits.

If the password is incorrect, the program prints "Access Denied!" and then
asks for the password again.

The program will ask for the password three times if necessary.

After that it exits.


"""

# Hard-coded password
PASSWORD = "prof123"

for i in range(3):

    user_pass = input("Enter your password:")

    if user_pass == PASSWORD:
        print("Greetings Professor Falcon")
        break
    else:
        print("Access Denied!")



