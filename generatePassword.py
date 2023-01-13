'''
3 Types of Password:
Weak    - 5-7 chars, pure letters
Medium  - 8-12 chars, letters, numbers
Strong  - 12-20 chars, letters, numbers, symbols
'''
import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = r"!@#$%^&*()[]{};'\:|,./<>?"

def generateWeak():
    masterlist = upper + lower
    generated_pass = ""
    length = random.randint(5, 7)

    for i in range(length):
        generated_pass += random.choice(masterlist)

    return generated_pass

def generateMedium():
    masterlist = upper + lower + numbers
    generated_pass = ""
    length = random.randint(8, 12)

    for i in range(length):
        generated_pass += random.choice(masterlist)

    return generated_pass

def generateStrong():
    masterlist = upper + lower + numbers + symbols
    generated_pass = ""
    length = random.randint(12, 20)

    for i in range(length):
        generated_pass += random.choice(masterlist)

    return generated_pass
