hash_value = input("Enter hash: ")

length = len(hash_value)

if length == 32:
    algo = "MD5"
elif length == 40:
    algo = "SHA1"
elif length == 64:
    algo = "SHA256"
elif length == 128:
    algo = "SHA512"
else:
    algo = "Unknown"

print("\nHash Length:", length)
print("Probable Algorithm:", algo)
