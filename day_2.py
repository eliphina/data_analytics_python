# ## creating simple variable name 

# first_name = 'Moro Wahab' 

# firstName = "Moro Wahab"

# #first name = "Moro Wahab"

# age = '34'
# ## Type Checking 

# #print(type(first_name))

# print(type(age))

# print(age is int)

# ## changing the type of age 
# new_age = int(age)

# print(type(new_age))

## accept a users first Name
user_name = input("Enter your first Name: ")

## displayy the users name 
print(user_name)

# ## declare a variable 
# first_name = input("Enter your first Name: ")

# ## display the input

# print("Hello " + first_name)

# ## take two numbers from a user
# user_input_1 = input("Enter first number: ")

# user_input_2 = input("Enter second number: ")

# ## add the two inputs .. 
# answer = int(user_input_1) + int(user_input_2)


# ## display the result
# print("The total is: " , answer)


user_input = input("Enter first number: ")

new_input = int(user_input)
# if new_input > 10:
#     print("This over 10")

if new_input > 10:
    print("This over 10")
else:
    print("This is not over 10")
