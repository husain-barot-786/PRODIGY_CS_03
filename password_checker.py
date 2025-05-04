#Password Complexity Checker

import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count the number of satisfied criteria
    criteria_met = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    # Determine strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Return both score and detailed feedback
    feedback = {
        "length": not length_error,
        "uppercase": not uppercase_error,
        "lowercase": not lowercase_error,
        "digit": not digit_error,
        "special_char": not special_char_error
    }

    return strength, feedback

def print_feedback(feedback):
    print("\nPassword Criteria Feedback:")
    print(f"✔ Minimum 8 characters: {'✅' if feedback['length'] else '❌'}")
    print(f"✔ Contains uppercase letter: {'✅' if feedback['uppercase'] else '❌'}")
    print(f"✔ Contains lowercase letter: {'✅' if feedback['lowercase'] else '❌'}")
    print(f"✔ Contains digit: {'✅' if feedback['digit'] else '❌'}")
    print(f"✔ Contains special character: {'✅' if feedback['special_char'] else '❌'}")

def main():
    print("==== Password Complexity Checker ====")
    user_password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(user_password)

    print(f"\n🔒 Password Strength: {strength}")
    print_feedback(feedback)

if __name__ == "__main__":
    main()
  
