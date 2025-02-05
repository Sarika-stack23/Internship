import random
import string

# Base username
base_username = "HyperShyamiGoddess"

# Function to generate a modified username
def generate_username(include_numbers=True, include_special_chars=True, length=8):
    username = base_username
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username[:length]

# Function to save usernames to a file
def save_usernames(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}")

# Interactive user input
def main():
    print("Welcome to the HyperShyamiGoddess Username Generator! 🚀")
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    length = int(input("Enter maximum length for the usernames: "))
    
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(num_usernames)]
    
    print("Generated Usernames:")
    for username in usernames:
        print(username)
    
    save_option = input("Would you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        save_usernames(usernames)

if __name__ == "__main__":
    main()
