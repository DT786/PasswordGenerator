#Modules
import os

try:
    import random
except:
    os.system('pip install random')
    import random
    
try:
    import string
except:
    os.system('pip install string')
    import string

try:
    import pyperclip
except:
    os.system('pip install pyperclip')
    import pyperclip
    
try:
    import colorama
    from colorama import Fore, init
    colorama.init(convert = True)
except:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore, init
    colorama.init(convert = True)

os.system('cls')
os.system('title Password Generator')

def pass_gen(length):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation

    while True:
        try:         
            print("How many passwords do you want to generate?")
            numofpasswords = int(input())
            break
        except ValueError:
            pass

    copy = ''

    if numofpasswords == 1:        
        print("Do you want to copy the password to your clipboard? (y/n)")
        copy = input()

        while not copy.isalpha(): # This checks if the input only contains alphabetical characters.
            print("Do you want to copy the password to your clipboard? (y/n)")
            copy = input()

    for i in range(numofpasswords):
        for i in range(length):
            password += random.choice(chars)
            if len(str(password)) == length:
                print(password)
                if copy == "y":
                    pyperclip.copy(password)
                password = ''

    return password

while True:
    try:
        print(Fore.LIGHTBLUE_EX + "How long do you want the password to be?")
        length2 = int(input())
        break
    except ValueError:
        pass

print(pass_gen(length2))
input()