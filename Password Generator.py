import random
import string
import pyperclip
import colorama
from colorama import Fore, init
colorama.init(convert = True)


def pass_gen(length):
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation

    print("How many passwords do you want to generate?")
    numofpasswords = int(input())
    copy = ''

    if (numofpasswords == 1):
        print(Fore.LIGHTBLUE_EX + "Do you want to copy the password to your clipboard?")
        copy = input()

    for i in range(numofpasswords):
        for i in range(length):
            password += random.choice(chars)
            if (len(str(password)) == length):
                print(password)
                if (copy.lower() == "yes"):
                    pyperclip.copy(password)
                password = ''


    return password

while True:
    try:
        print(Fore.LIGHTBLUE_EX + "How long do you want the password to be?")
        length2 = input()
        length2 = int(length2)
        break
    except ValueError:
        pass

print(pass_gen(length2))
input()
