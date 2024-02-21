## for loop 

# print("Good morning!!")

# for i in range(1, 11):
#     user_name = input("Please enter your name: ")
#     print(i)
#     print(user_name)

# user_name = input("Enter your name: ")
# number_times = int(input("Enter the number of times to display: "))


# for i in range(1, number_times+1):
#     print(user_name , '=>', i)

# print("Goodbye")

# user_password = input("Enter your password: ")

# correct_password = 'password'

# while (user_password != correct_password):
#     user_password = input("Enter a new password: ")

# print('Password is Correct')


# users_age = int(input("Enter your age: "))

# while (users_age < 18):
#     users_age = int(input('Ask for the next persons age: '))

# print("Move to the next Stage")

# user_const = input("Place of vote: ")

# while (user_const != 'bolga central'):
#     print('Not allowed to vote here, next person')
#     user_const = input("place of vote: ")

# print("Please you can now vote")


## accept two numbers from user
def accept_input():
    user_input_1 = int(input("Enter first number: "))
    user_input_2 = int(input("Enter second number: "))
    return user_input_1, user_input_2

## adds two numbers 
def addition(num_1, num_2):
    result = num_1 + num_2
    return result
``

## function call 
def main():
    input_1, input_2 = accept_input()
    final_answer = addition(input_1, input_2)
    print('The addition result is: ', final_answer)

    input_1, input_2 = accept_input()
    final_answer = addition(input_1, input_2)
    print('The addition result is: ', final_answer)

main()









