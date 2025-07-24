# database of people
# stressfull method
names = ["Will", "Leo", "Kate", "Kay", "Shushubom", "Turururubom", "Anibom", "Auablebom"]
# print(names[0])
# print(names[1])
# print(names[2])

# Real method
# for  name in names:
#     print(name)
    # if name.endswith("bom"):
    #     print(f"We don catch you: {name}")
    # else:
    #     print(f"Welcome to the party: {name}")

# count = 1
# for  name in names:
#     print(f"{count}. {name}")
#     count += 1


# my_names = "Turururubom"
# for letter in my_names:
#     print(f"letter: {letter}")


# RANGE METHOD IN LOOPING
# range(stop) - starts from 0
# for i in range(5):
#     print(i)

# range(start, stop)
# for i in range(2, 7):
#     print(i)

# range(start, stop, step)
# for i in range (0, 11, 2):
#     print(i)

# # Countdown
# for i in range(10, 0, -1):
#     print(f"Countdown: {i}")
# print("Blast off! 🚀")



# # Basic while loop
# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     count += 1  # Same as count = count + 1

# # User input loop
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input != "quit":
#         print(f"You entered: {user_input}")

# print("Goodbye!")



# # BREAK - exit the loop cpmpltely
# print("Findig the first even number:")
# for number in range(1, 10):
#     if number % 2 ==0:
#         print(f"Found even number: {number}")
#         break
#     print(f"{number} is odd")

# # CONTINUE - skip to next iteration
# print("\nPrinting only odd numbers:")
# for number in range(1,10):
#     if number % 2 == 0:
#         continue
#     print(f"Odd umber: {number}")


# Multiplication table
print("Multiplication Table:")
for i in range(1, 4):  # Rows
    for j in range(1, 4):  # Columns
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each row



# Pattern printing
print("Triangle pattern:")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()  # New line after each row