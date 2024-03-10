import random
import string

def generate_password(length=12):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    num_passwords = int(input("How many password do you want to generate: "))
    print("Generating "+str(num_passwords)+" passwords")
    print("Minimum length of password should be 3")
    passwordlength = []
    for i in range(num_passwords):
        password_length = int(input("Enter the length of password " + str(i+1) + ": "))
        if password_length<3:
            password_length = 3
        passwordlength.append(password_length)

    for i in range(num_passwords):
        password = generate_password(length=passwordlength[i])
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
