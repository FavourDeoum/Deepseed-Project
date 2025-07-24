
# first_name="Ngalah"
# last_name="Desire"

# # Concatenation
# full_name= first_name + " " + last_name

# # Interpolation
# print(f"my full name is {full_name}")

# # PRACTICALS
# name= "Alice"
# age = 30
# score = 95.5

# # Method 1: f-strings (recommended - like fill-in-the-blank)
# print(f"Hello, {name}! You are {age} years old.")
# print(f"your score is {score:.1f}%")

# # Method 2: .format() method
# print("Hello, {}! You are {} years old.".format(name, age))

# # Method 3: % formatting (older style)
# print("Hello, %s! You are %d years old." %(name, age))



# Email validator (basic)
# email = "user@example.com"
# if "@" in email and "." in email:
#     username = email.split("@")[0]
#     domain = email.split("@")[1]
#     print(f"Username: {username}")
#     print(f"Domain: {domain}")
# else:
#     print("Invalid email format")

# # Text analyzer
# text = "The quick brown fox jumps over the lazy dog"
# print(f"Text: {text}")
# print(f"Length: {len(text)} characters")
# print(f"Words: {len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Title case: {text.title()}")
# print(f"Contains 'fox': {'fox' in text}")

full_name = "Tahyu Favour"

# EXERCISES


# STRING METHODS
message = "Good Monrning"
# convert lowercase to uppercase and vice versa

# message_lower = message.lower()
# message_upper = message.upper()
# print(f"The lower case conversion is: {message_lower} and the uppercase conversion is: {message_upper}")

# SLICING
greetings = "welcome back"
how_python_sees_it = list(greetings)
print(f"Python view: {how_python_sees_it}")

extract_text= greetings[0:3]
print(f"Extracted Text: {extract_text}")


# text = "  Hello, Python World!  "

# # Case changes
# print(text.upper())        # "  HELLO, PYTHON WORLD!  "
# print(text.lower())        # "  hello, python world!  "
# print(text.title())        # "  Hello, Python World!  "

# # Cleaning up
# print(text.strip())        # "Hello, Python World!"
# print(text.replace("Python", "Amazing Python"))

# # Checking content
# print(text.startswith("Hello"))    # False (because of spaces)
# print(text.strip().startswith("Hello"))  # True
# print("Python" in text)           # True

# # Splitting and joining
# words = "apple,banana,cherry".split(",")
# print(words)               # ['apple', 'banana', 'cherry']
# joined = "-".join(words)
# print(joined)

# EXERCISE 1
full_name = "jOhN dOe"
adjusted_name = full_name.title()
print(f"Adjusted name is: {adjusted_name}")

# OR
j= full_name[0].upper()
n= full_name[3].lower()
d= full_name[5].upper()
name= full_name[1:4].lower()
complete = full_name[6:8].lower()
print(f"My full name is: {j}{name} {d}{complete}")