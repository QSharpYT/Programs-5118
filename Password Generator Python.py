import random
import string

def generate_password(strength):
    if strength == "very weak":
        characters = string.ascii_lowercase
        length = 4
    elif strength == "weak":
        characters = string.ascii_lowercase
        length = 6
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
        length = 10
    elif strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
        length = 16
    elif strength == "very strong":
        characters = string.ascii_letters + string.digits + string.punctuation
        length = 32
    elif strength == "galactic":
        characters = string.ascii_letters + string.digits + string.punctuation
        length = 48
    elif strength == "impossible":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
        length = 64
    elif strength == "universe":
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
        length = 128
    else:
        return "Invalid strength level. Choose very weak, weak, medium, strong, very strong, galactic, universe, or impossible."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    strength = input("Enter password strength (very weak, weak, medium, strong, very strong, galactic, impossible, universe): ").lower()
    print("Generated Password:", generate_password(strength))
