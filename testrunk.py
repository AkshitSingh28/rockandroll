
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


global result
global Player1
global Player2


def user_input1():
    answer = 'Wrong'
    global Player1
    global Player2
    global result
    mark = 'wrong1'

    answer = input('Do you want to play the game? (yes or no)')

    while answer.lower() not in ['yes', 'no']:
        answer = input('Do you want to play the game? (yes or no)')

    if answer.lower() == 'yes':
        answer = input('How many players want to play the game? 1 or 2')

    while int(answer) not in [1, 2]:
        answer = input('How many players want to play the game? 1 or 2')

    if int(answer) == 2:
        print('Ok get ready!')

        mark = input('Player1 What would you like to choose? X or O ')

        while mark.upper() not in ['X', 'O']:
            mark = input('Player1 What would you like to choose? X or O ')

        if mark.upper() == 'X':
            print('Player1 chooses X')
            print('Player2 got O')

            Player1 = 'X'
            Player2 = 'O' or 'o'
            result = ['X', 'O' or 'o']

        elif mark.upper == 'O' or 'o':
            print('Player1 chooses O')
            print('Player2 got X')
            result = ['O'or 'o', 'X']

            Player1 = 'O' or "o"
            Player2 = 'X'

    Player1 = result[0]
    Player2 = result[1]
    display_board(board)



def user_input_player1(board):
    global choice
    choice = 'wrong1'
    #for i in range(1 ,9):
    choice = input('Player 1: what position will you choose between 1-9')

    while int(choice) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Incorrect input')
        choice = input('Player 1: what position will you choose between 1-9')

    if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        while board[int(choice)] not in '  ':
            print('Incorrect place choosed!')
            choice = input('Player 1: what position will you choose between 1-9')
    if board[int(choice)] in ' ':
        board[int(choice)] = Player1
        return display_board(board)


def user_input_player2(board):
    choice = input('player 2: what position will you choose between 1-9')

    while int(choice) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Incorrect input')
        choice = input('player 2: what position will you choose between 1-9')

    if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

        while board[int(choice)] not in ' ':
            print('Incorrect place choosed!')
            choice = input('player 2: what position will you choose between 1-9')
        if board[int(choice)] in ' ':
            board[int(choice)] = Player2
            display_board(board)


board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

global result
global Player1
global Player2


def user_input1():
    answer = 'Wrong'
    global Player1
    global Player2
    global result
    mark = 'wrong1'

    answer = input('Do you want to play the game? (yes or no)')

    while answer.lower() not in ['yes', 'no']:
        answer = input('Do you want to play the game? (yes or no)')

    if answer.lower() == 'yes':
        answer = input('How many players want to play the game? 1 or 2')

    while int(answer) not in [1, 2]:
        answer = input('How many players want to play the game? 1 or 2')

    if int(answer) == 2:
        print('Ok get ready!')

        mark = input('Player1 What would you like to choose? X or O ')

        while mark.upper() not in ['X', 'O']:
            mark = input('Player1 What would you like to choose? X or O ')

        if mark.upper() == 'X':
            print('Player1 chooses X')
            print('Player2 got O')

            Player1 = 'X'
            Player2 = 'O' or 'o'
            result = ['X', 'O' or 'o']

        elif mark.upper == 'O' or 'o':
            print('Player1 chooses O')
            print('Player2 got X')
            result = ['O'or 'o', 'X']

            Player1 = 'O' or "o"
            Player2 = 'X'

    Player1 = result[0]
    Player2 = result[1]
    display_board(board)



def user_input_player1(board):
    global choice
    choice = 'wrong1'
    #for i in range(1 ,9):
    choice = input('Player 1: what position will you choose between 1-9')

    while int(choice) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Incorrect input')
        choice = input('Player 1: what position will you choose between 1-9')

    if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        while board[int(choice)] not in '  ':
            print('Incorrect place choosed!')
            choice = input('Player 1: what position will you choose between 1-9')
    if board[int(choice)] in ' ':
        board[int(choice)] = Player1
        return display_board(board)


def user_input_player2(board):
    choice = input('player 2: what position will you choose between 1-9')

    while int(choice) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Incorrect input')
        choice = input('player 2: what position will you choose between 1-9')

    if int(choice) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

        while board[int(choice)] not in ' ':
            print('Incorrect place choosed!')
            choice = input('player 2: what position will you choose between 1-9')
        if board[int(choice)] in ' ':
            board[int(choice)] = Player2
            display_board(board)


def win_check(board):
    display_board(board)
    user_input1()

    while True:
         user_input_player1(board)

         user_input_player2(board)
         if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or (board[
             7] == 'X' and board[8] == 'X' and board[9] == 'X' )or (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or (board[3] == 'X' and board[5] == 'X' and
             board[7] == 'X') or (board[7] == 'X' and board[4] == 'X' and board[1] == 'X' )or (board[8] == 'X' and board[5] == 'X' and board[2] == 'X') or (board[9] == 'X' and board[6] == 'X' and board[3] == 'X'):
             print('Won')
             break

         elif (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or (board[4] == 'O' and board[5] == 'O' and board[6] == 'O') or (board[7] == 'O' and board[
             8] == 'O' and board[9] == 'O') or (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or (board[3] == 'O' and board[5] == 'O' and board[
             7] == 'O') or (board[7] == 'O' and board[4] == 'O' and board[1] == 'O' )or (board[8] == 'O' and board[5] == 'O' and board[2] == 'O') or (board[
             9] == 'O' and board[6] == 'O' and board[3] == 'O'):
             if Player1 == 'O':
                print('Player1 has won the match')
                break
             elif Player2 == 'O':
                print('Player2 has won the  match')
                break




win_check(board)