import os

#Pre-Defined
def check_int(num):
    try:
        num = int(num)
        return True
    except:
        return False

def multi_input():
    nums = []
    while True: #Wait for x input
        number_in = input('')
        if number_in.lower() == "x": #Break if num = 0
            break
        while check_int(number_in) != True: #Check Int
            print('Number not registered, please type a valid number!')
            number_in = input('')
        number_in = int(number_in)
        nums.append(number_in)
    return nums

#Class
class User:
    def __init__(self, username) -> None:
        self.name = username
        Calculator.main_page(username)

class Calculator:
    def __init__(self) -> None:
        pass

    def main_page(username):
        print(f'Welcome to The Python Calculator {username}!')
        print('')
        print('Please type the number of the operation you wish to do:')
        print('1 -> Addition')
        print('2 -> Substraction')
        print('3 -> Multiplication')
        #Operation Selection
        user_input = input('')
        while check_int(user_input) != True:
            print('Error! Please give a valid response!')
            user_input = input('')
        user_input = int(user_input)

        #Interfaces       
        if user_input == 1: #ADDITION
            print("Please type in the numbers you wish to add, type x when complete!")
            nums = multi_input()

            print(f'Your results are: {Calculator.addition(nums)}')
        
        elif user_input == 2: #SUBSTRACTION
            print("Please type the main number you want to subtract!")
            subtraction_main_num = input('')
            while check_int(subtraction_main_num) != True:
                subtraction_main_num = input('')
            subtraction_main_num = int(subtraction_main_num)
            print(f'{subtraction_main_num} is registered as main number!')
            print('')
            print('Please type the numbers you want to subtract with, type x when complete!')
            nums = multi_input()

            print(f'Your results are: {subtraction_main_num - sum(nums)}')
            
        Calculator.end_screen(username)
        
    def end_screen(username):
        print("Thank you, would you like to use the calculator again? (yes/no)")
        end_user_input = input('')
        if end_user_input.lower() == "yes":
            Calculator.main_page(username)
        elif end_user_input.lower() == "no":
            os.system('CLS' if os.name == 'nt' else 'clear')
            print('Thank you for using the calculator, have a good day!')
        else:
            print("I'm sorry, unrecognized input, you will be redirected to the main page!")
            print("")
            Calculator.main_page(username)

    #Processes
    def addition(data):
        res = sum(data)
        return res

#Main Driver
if __name__ == '__main__':
    os.system('CLS' if os.name == 'nt' else 'clear')

    #Input username and instantiate
    username = input('Please type your name: ')
    os.system('CLS' if os.name == 'nt' else 'clear')
    user = User(username)