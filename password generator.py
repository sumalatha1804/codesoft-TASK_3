import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function
def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    if length < 1:
        print("Password length should be at least 1.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

# Start the program
if __name__ == "__main__":
    main()