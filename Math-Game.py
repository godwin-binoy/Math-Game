print('Math Game\n---------')

import random

while True:
    score = 0
    difficulty = input('\nEnter diffficulty : ')
    operator = input('\n+ , - or * ?\n\nSelect operator : ')

    try:
        difficulty = int(difficulty)
    except:
        print('\nError : Make sure that you entered Integer\n')
        continue

    if difficulty < 1 :
        print('\nError : Make sure that difficulty is larger than 1\n')
        continue

    if operator != '+' and operator != '-' and operator != '*' :
        print("Error : Make sure that you entered valid operator")
        continue
    print("\nEnterr 'exit' to exit program\nEnter 'restart' to restart game\n")
    while True :
        first_numder = random.randint(2, 10 ** difficulty)
        second_number = random.randint(0, first_numder - 1)
        print(f'{first_numder} {operator} {second_number} ?')
        user_input = input('  : ')

        if user_input == 'exit' :
            exit()
        elif user_input == 'restart' :
            break
        else :

            try :
                user_input = int(user_input)
            except :
                print('\nError : Make sure that you entered valid input\n')
                continue

            if operator == '+' :
                answer = first_numder + second_number
            elif operator == '-' :
                answer = first_numder - second_number
            elif operator == '*' :
                answer = first_numder * second_number

        if user_input == answer :
            score += 1
        else :
            print(f'\nYou lose !\nAnswer is {answer}\nYour score : {score}\n')
            user_input = input('Enter to continue : ')

            if user_input == 'exit' :
                exit()
            elif user_input == 'restart' :
                break
            else :
                score = 0
                continue