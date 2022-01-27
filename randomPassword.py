import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate():
    
    while True:
        length = int(input("Enter the length of your desired password:"))

        random.shuffle(characters)

        password = []

        for i in range(length):
            n = random.choice(characters)
            password.append(n)

        random.shuffle(password)

        password = "".join(password)

        print(f'Your new password is: {password}')
        again = input("Would you like to generate another password?")

        if not again.lower() in {'y', 'yes'}:
            print("Goodbye!")
            return

generate()