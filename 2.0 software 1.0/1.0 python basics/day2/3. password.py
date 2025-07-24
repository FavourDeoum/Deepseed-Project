
passsword= input("Enter your password: ")
l= False
u= False
d= False

for letter in passsword:
    if letter.islower():
        l= True
    elif letter.isupper():
        u= True
    elif letter.isdigit():
        d= True

if u and l and d:
    print("Strong password")
else:
    print("weak password")


# # OR
# # Password validation script
# # This script checks if a password meets certain criteria:
# passsword = input("Enter your password: ")
# if len(passsword) < 8:
#     print("Password must be at least 8 characters long.")
# elif not any(char.isdigit() for char in passsword):
#     print("Password must contain at least one digit.")
# elif not any(char.isupper() for char in passsword):
#     print("Password must contain at least one uppercase letter.")
# elif not any(char.islower() for char in passsword):
#     print("Password must contain at least one lowercase letter.")
# elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in passsword):
#     print("Password must contain at least one special character.")
# else:
#     print("Password is valid.")