# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
print(n1 // n2)

#print(n1/n2)
# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
favorite_animal = input("What is your favorite animal?: ")
favorite_color = input("What is your favorite color?:" )
print("A", favorite_color, favorite_animal + " is amazing!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(11):
    if(i%2 == 0):
        print(i)
# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
number_of_pushups = int(input("How many pushups can you do?:"))
number_of_pushups_done_in_a_week = (number_of_pushups*7)
print("You can do", number_of_pushups_done_in_a_week , "pushups in a week!")

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range(1, 6):
    print(i**i)
