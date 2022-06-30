import random

"""
in the start of each function call for guess_integer(), the function will pick a random
integer as a target number and will ask a user inputs until the user guess the target number.
Because we don't know how many times the user will need to guess until they guess the target number
we will use a while loop that will loop until the user answer is correct. In each iteration
it will ask for the user input (guess) and compare it with the target number, 
each time it will fall into three categories such as the user guess the right number,
the user guess is lower than target, and user guess is higher than target and an 
appropriate message feedback will be given to the user.
"""

def guess_integer():
    user_answer = False # set the user answer to FALSE
    random_num = random.randint(1, 100) # get a random number as target
    while user_answer is False: # loop until user answer the correct number
        user_num = get_user_input() # get the input from the user
        user_answer = check_user_input(user_num, random_num)    # check if user answer is correct / not

def get_user_input():
    user_num = int(input("Guess a number from 1 to 100: ")) # get user input in integer format
    return user_num # return user input

def check_user_input(user_num, random_num):
    user_answer = False # set a flag variable user answer to FALSE
    if user_num == random_num:  # check if the user guess's number is equal to the target
        print("Correct! you guessed the right number")  # print correct guess message to the user
        user_answer = True  # set user answer flag to TRUE since user answer the right number
    elif user_num < random_num: # check if the user guess's number is less than the target
        print("Wrong! your number is lower than the target number") # print the wrong message that the user guess is lower message
    else:   # check if the user guess's number is higher than the target
        print("Wrong! your number is higher than the target number")    # print the wrong message that the user guess is higher message
    return user_answer  # return the variable that determine the user answer is right / wrong

guess_integer()