import math

password = input("Password: ")

length = len(password)

charset = 0
if any(c.islower() for c in password):
    charset += 26
if any(c.isupper() for c in password):
    charset += 26
if any(c.isdigit() for c in password):
    charset += 10
if any(not c.isalnum() for c in password):
    charset += 32

entropy = round(length * math.log2(charset)) if charset > 0 else 0

if entropy < 40:
    complexity = "Weak"
elif entropy < 60:
    complexity = "Medium"
else:
    complexity = "Strong"

print("\nLength:", length)
print("Complexity:", complexity)
print("Entropy:", entropy, "bits")

if "password" in password.lower():
    print("\nWeakness:")
    print("Contains dictionary word")

print("\nRecommendation:")
print("Use passphrase with symbols.")
