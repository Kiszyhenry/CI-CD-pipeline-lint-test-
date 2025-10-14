import re

def check_password_strength(password):
    # Initialize strength points
    strength = 0

    # Check the length
    if len(password) >= 8:
        strength += 1
    else:
        print("❌ Password too short (minimum 8 characters).")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        print("❌ Add at least one number.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("❌ Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print("❌ Add at least one lowercase letter.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("❌ Add at least one special character (!, @, #, $, etc).")

    # Evaluate strength
    if strength == 5:
        print("✅ Strong password! 🔥")
    elif strength >= 3:
        print("⚠️ Moderate password. Consider improving it.")
    else:
        print("❌ Weak password. Please try again.")

# Run the program
password = input("Enter your password to check strength: ")
check_password_strength(password)
