# print("Hello, Deepseed")

# # why we need variables
# name="Tayuh"

# print("I am Deoum, I love this name Deoum, it was given to me by my father, Peter Deoum and I really love the name Deoum")
# print("My name is " + name + ", I love " + name + ". It was given to me by my Father, " + name + " Peter" )

# # VARIABLES
# # strings
# NAME= "Deoum"
# # integer
# age= 21
# # float
# height= 1.5
# # boolean
# isMarried= False

# # PRACTICE
# whole_number = 42              # Integer (int)
# decimal_number = 3.14159       # Float
# complex_number = 2 + 3j        # Complex

# # Text
# greeting = "Hello, World!"     # String (str)
# single_char = 'A'             # Also a string

# # Boolean (True/False)
# is_sunny = True               # Boolean (bool)
# is_raining = False

# # Check the type of any variable
# print(type(whole_number))     # <class 'int'>
# print(type(greeting))         # <class 'str'>


# # Personal information
# first_name = "Emma"
# last_name = "Watson"
# full_name = first_name + " " + last_name
# age = 33
# birth_year = 2025 - age

# print(f"Hello, {full_name}!")
# print(f"You were born in {birth_year}")

# # Shopping cart
# item_price = 29.99
# quantity = 3
# total_cost = item_price * quantity
# tax_rate = 0.08
# final_cost = total_cost + (total_cost * tax_rate)

# print(f"Total cost with tax: ${final_cost:.2f}")


# # BASIC EXANPLES
# first_name= "Ngwa"
# second_name="Desly"
# print(first_name + " " + second_name)

# combine_name= first_name + " "+ second_name
# print("My name is " + combine_name)
# print(f"My name is {combine_name}")


# # BAND NAME GENERATOR
# # name, Age, Fav meal, school, department, bestfrnd print a story from this 
# name= input("What is your name? ")
# age= input("How old are you? " )
# fav_meal= input("What is your fav meal? ")
# school= input("what school do you attend? ")
# department=input("What department please? ")
# best_friend= input("Who is your best friend? ")

# print(f"My name is {name}, I am {age} years old. I love eating {fav_meal}. I attend {school} school, in the department of {department}. To conclude, my bestfriend is {best_friend}")




# CALCULATION
length = input("enter ur length ")
width = input("enter ur width ")
area = int(length) * int(width)
perimetre = 2 * (int(length) + int(width))
print(f"The area of the rectangle is {area} square units.")
print(f"The perimeter of the rectangle is {perimetre} units.")
print(f"The area of the rectangle is {area} square units and the perimeter is {perimetre} units.")
print(f"The area of the rectangle is {area} square units and the perimeter is {perimetre} units. The length is {length} and the width is {width}.")


# CONVERT CELCUSIUS TO FAHRENHEIT
celsius = input("Enter temperature in Celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")