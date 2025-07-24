# # old style
# age= 20
# if (age > 18):{
#     print("you can vote")
# }
# else:{
#     print("Not Eligable")
# }
    
# # Modern
# if-else pair

# age= int(input("Enter your age "))

# if age > 18:
#     print("Yes you can vote")
# else:
#     print("Not eligable. Try next session")

# # EXERCISE: Take a person's age, check if they are morethan 16, if yes, they can play in the basket ball team
# age=int(input("Please Enter Age "))
# if age >=16:
#     print("Welcome to the team ")
# else:
#     print("Grow up🤣")


# # if-else-elif chain
# # Knowlege
# command = input("Enter 'exit' to end the program and 'continue' to keep going ")
# if command=="exit":
#     print("exiting cmd")
# elif command=="continue":
#     print("continue enjoying...")
# else:
#     print("Wrong command")

# # EXERCISE
# Grade= float(input("Enter your grade "))
# if Grade>=80:
#     print("A Grade🍾")
# elif Grade>=70:
#     print("B+ Grade🎀")
# elif Grade>=60:
#     print("B Grade💐")
# elif Grade>=50:
#     print("C Grade✨")
# elif Grade>=40:
#     print("D Grade😂")
# else:
#     print("Very pooooooor😒🤣🤣🤣🤣🤣")



# # A SIMPLE CALCULATION
# first_number = float(input("Enter first numer: "))
# second_number = float(input("Enter second numer: "))
# operator = input("Enter operator: ")
# results =0

# if operator=="+":
#     results=first_number + second_number
#     print(results)
# elif operator=="-":
#     results=first_number - second_number
#     print(results)
# elif operator=="*":
#     results=first_number * second_number
#     print(results)
# elif operator=="/":
#     if second_number != 0:
#         results=first_number / second_number
#         print(results)
#     else:
#         print("Division by 0 is not allowed")
# else:
#     print("Please check your operator")



# LEAP YEAR CALCULATION
# Year= int(input("Enter year: "))
# if Year % 4 == 0:
#     if Year % 100 == 0:
#         if Year % 400 == 0:
#             print(f"{Year} is a leap year.")
#         else:
#             print(f"{Year} is not a leap year.")
#     else:
#         print(f"{Year} is a leap year.")
# else:
#     print(f"{Year} is not a leap year.")

# OR
Year= int(input("Enter year: "))
if Year % 4 == 0:
    if Year % 400 ==0:
        print(f"{Year} is not a leap year")
    else:
        print(f"{Year} is a leap year")

else:
    if Year % 100 == 0:
        print(f"{Year} Is a leap year")
    else:
        print(f"{Year} Is not a leap year")