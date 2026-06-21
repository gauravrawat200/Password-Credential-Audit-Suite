username = input("Enter username:  ")
passwords =[]
passwords.append(username + "123")
passwords.append(username + "2024")
passwords.append(username + "1234")
leet = username.replace("a", "@").replace ("o","0")
passwords.append(leet + "123")
with open("wordlist.txt", "w")as f:
    for p in passwords:
        f.write(p+"\n")

print("\nGenerated Passwords :")
for p in passwords:
    print (p)

