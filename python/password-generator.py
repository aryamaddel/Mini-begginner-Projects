import random
import string
characters = ''
characters += string.ascii_letters + string.digits + string.punctuation

# to add your own characters
# characters += ''  

def pass_geneator():
    password = ''
    for i in range(16):
        password += random.choice(characters)
    return password

while True:
    nav_input = input("To generate password type 'y'\nto exit type 'n'\n:")
    if nav_input == 'y':
        print("-----------------------------------\n")
        print(pass_geneator() + '\n')  
        print("-----------------------------------\n")
    elif nav_input == 'n':
        quit()
    else:
        print('invalid entry')