# PRODIGY_CS_03
A Python tool to assess password strength based on length, case, digits, and symbols.

# Password Complexity Checker - Python Tool

## Description

This is a Python-based password strength checker designed to evaluate the complexity of user-entered passwords. It checks for key security criteria such as length, presence of uppercase and lowercase letters, digits, and special characters. Based on these factors, it classifies the password as Very Weak, Weak, Moderate, Strong, or Very Strong. This project is aimed at developing practical awareness of password security policies and validation logic using Python.

---

## Objective

- To evaluate password strength using multiple security criteria.
- To offer real-time feedback to users on their password's weaknesses.
- To promote secure password practices through programmatic validation.

---

## Requirements

- Python 3.x

No external libraries required (uses built-in `re` for regex).

---

## How to Use

1. Clone or download this repository.
2. Run the script using Python:

```bash
python password_checker.py
```

3. Enter a password when prompted.
4. The tool will assess and display the strength and validation feedback.

---

## Example

```bash
==== Password Complexity Checker ====
Enter a password to check its strength: Cyber@123

Password Strength: Very Strong

Password Criteria Feedback:
✔ Minimum 8 characters: ✅
✔ Contains uppercase letter: ✅
✔ Contains lowercase letter: ✅
✔ Contains digit: ✅
✔ Contains special character: ✅
```

---

## Files

- `password_checker.py` – Main Python script
- `README.md` – Project documentation

## Note

This tool is built to demonstrate password validation logic. It does not store passwords or provide secure authentication. Always follow secure password storage best practices (e.g., hashing + salting) in real-world systems.

---
