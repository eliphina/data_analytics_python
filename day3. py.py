  ## for loop

# print("good morning!!")
# for i in range(1, 11):
#     user_name = input("please enter your name: ")
#     print(i)
#     print(user_name)

# user_name = input("enter your name: ")
# number_times = int(input("enter the number of time to display: "))


# for i in range(1, number_times+1):
#     print(user_name , '=>', i)

# print("goodbye")

# user_name = input("enter your name: ")
# number_times = int(input("enter the number of time of display: "))

# for i in range(1, number_times+1):
#     print(user_name , '=>' , i*12 )



# user_password = input("enter your password")

# correct_password = 'password'

# while (user_password != correct_password):
#     user_password = input("enter a new password: ")

# print('password is correct')


# users_age = int(input("enter your age"))

# while (users_age != 20):
#     users_age = int(input('ask for the next persons age'))


# accept two numbers from a user
def accept_input():
     user_input1 = int(input("enter first number"))
     user_input2 = int(input("enter second number"))
     return user_input1, user_input2 

# ## adds two numbers
def addition(num_1, num_2):
    result = num_1 + num_2
    return result


# ## subtract two numbers
# def substraction(num_1, num_2):
#     result = num_1 - num_2
#     return result


# ## multiply two numbers
def multiplication(num_1, num_2):
     result = num_1 * num_2
     return result


# ## divide two numbers
# def division(num_1, num_2):
#      result = num_1 / num_2
#      return result

 ## function call
def main():
    print("enter '+' for addition")
    print("enter '*' for multiplication")
    operation_type = input("what operation do you want to perform: ")
    input_1, input_2 =accept_input()

    if (operation_type == '+'): 
        final_answer = addition(input_1, input_2)
        print('The addition result is: ', final_answer)
    elif (operation_type == '*'):
        final_answer = multiplication(input_1, input_2) 
        print('The multiplication result is: ', final_answer) 
    else:
        print('selected option not available.')
        print('wait for version 2')  


main()





