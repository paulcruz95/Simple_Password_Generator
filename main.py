from generatePassword import generateWeak, generateMedium, generateStrong
from databaseHandler import add_password, show_database, delete_password

# Additional module
import base64
import maskpass

'''
Welcome to Password Manager
what would you like to do:
1. Generate Password
2. Show Generated Passwords - Database SQLite3
3. Delete generated Password
4. Exit
'''

def encode_pw(password):
    encrypt = base64.b64encode(password.encode("utf-8"))
    return encrypt

while True:
    
    print("")
    print("Welcome to Password Manager")
    print("What would you like to do:")
    print("1. Generate Password")
    print("2. Show Generated Passwords")
    print("3. Delete generated Password")
    print("4. Exit")

    user_input = input(">>> ")
    if user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4":
        if user_input == "1":
            print("")
            print("For what application will you use your password?")
            application = input(">>> ").capitalize()
            
            print("")
            print("How strong do you want your password to be?")
            print("1. Weak     - 5-7 chars, pure letters")
            print("2. Medium   - 8-12 chars, letters, numbers")
            print("3. Strong   - 12-20 chars, letters, numbers, symbols")
            pwStrength = input(">>> ")

            if pwStrength == "1" or pwStrength == "2" or pwStrength == "3":
                if pwStrength == "1":
                    password = generateWeak()

                elif pwStrength == "2":
                    password = generateMedium()
                elif pwStrength == "3":
                    password = generateStrong()
            else:
                print("")
                print("ONLY 1,2,3 CAN BE USE")
                continue
            
            encpwd = encode_pw(password)
            add_password(application, encpwd)

            print("")
            print("Saved Password for", application)

        elif user_input == "2":
            print("Saved passwords:")
            show_database()

        elif user_input == "3":
            print("")
            print("Enter the application and the password you want to delete")
            appToDelete = input("Application: ")
            pwToDelete = maskpass.askpass(prompt="Password: ", mask="*")
            encpwd = encode_pw(pwToDelete)
            
            delete_password(appToDelete, encpwd)

            print("")
            print("Password Deleted for", appToDelete)

        elif user_input == "4":
            print("")
            print("Thank you for using this program!")
            break
    
    else:
        print("")
        print("ONLY 1-4 CAN BE USE")
