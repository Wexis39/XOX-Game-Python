import random

row0 = [' ',' ',' ']
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']

print('\nXOX Game - by Wexis')

clearBoard =(
""" 
 1 | 2 | 3    
---+---+---
 4 | 5 | 6   
---+---+---
 7 | 8 | 9
""")

def printBoard():
    print(f"""
 {row0[0]} | {row0[1]} | {row0[2]}      1 | 2 | 3    
---+---+---    ---+---+---
 {row1[0]} | {row1[1]} | {row1[2]}      4 | 5 | 6   
---+---+---    ---+---+---
 {row2[0]} | {row2[1]} | {row2[2]}      7 | 8 | 9  
""")

def checkWinner():
    # Row check (For X)
    if row0[0] == 'X' and row0[1] == 'X' and row0[2] == 'X':
        print('\n* X Won!\n')
        exit()
    elif row1[0] == 'X' and row1[1] == 'X' and row1[2] == 'X':
        print('\n* X Won!\n')
        exit()
    elif row2[0] == 'X' and row2[1] == 'X' and row2[2] == 'X':
        print('\n* X Won!\n')
        exit()
    # Column check (For X)
    elif row0[0] == 'X' and row1[0] == 'X' and row2[0] == 'X':
        print('\n* X Won!\n')
        exit()
    elif row0[1] == 'X' and row1[1] == 'X' and row2[1] == 'X':
        print('\n* X Won!\n')
        exit()
    elif row0[2] == 'X' and row1[2] == 'X' and row2[2] == 'X':
        print('\n* X Won!\n')
        exit()
    # Cross check (For X)
    elif row0[0] == 'X' and row1[1] == 'X' and row2[2] == 'X':
        print('\n* X Won!\n')
        exit()
    elif row0[2] == 'X' and row1[1] == 'X' and row2[0] == 'X':
        print('\n* X Won!\n')
        exit()
    # Row check (For O)
    elif row0[0] == 'O' and row0[1] == 'O' and row0[2] == 'O':
        print('\n* O Won!\n')
        exit()
    elif row1[0] == 'O' and row1[1] == 'O' and row1[2] == 'O':
        print('\n* O Won!\n')
        exit()
    elif row2[0] == 'O' and row2[1] == 'O' and row2[2] == 'O':
        print('\n* O Won!\n')
        exit()
    # Column check (For O)
    elif row0[0] == 'O' and row1[0] == 'O' and row2[0] == 'O':
        print('\n* O Won!\n')
        exit()
    elif row0[1] == 'O' and row1[1] == 'O' and row2[1] == 'O':
        print('\n* O Won!\n')
        exit()
    elif row0[2] == 'O' and row1[2] == 'O' and row2[2] == 'O':
        print('\n* O Won!\n')
        exit()
    # Cross check (For O)
    elif row0[0] == 'O' and row1[1] == 'O' and row2[2] == 'O':
        print('\n* O Won!\n')
        exit()
    elif row0[2] == 'O' and row1[1] == 'O' and row2[0] == 'O':
        print('\n* O Won!\n')
        exit()    
    elif (row0[0] != ' ' and row0[1] != ' ' and row0[2] != ' ' 
          and row1[0] != ' ' and row1[1] != ' ' and  row1[2] != ' ' 
          and row2[0] != ' ' and row2[1] != ' ' and row2[2] != ' '):
        print('\n* Draw!\n')
        exit()

def playerControl_X():
    while True:
        xinput = input("- X's turn: ")
        if xinput == '1' and row0[0] == ' ':
            row0[0] = 'X'
            break
        elif xinput == '2' and row0[1] == ' ':
            row0[1] = 'X'
            break
        elif xinput == '3' and row0[2] == ' ':
            row0[2] = 'X'
            break
        elif xinput == '4' and row1[0] == ' ':
            row1[0] = 'X'
            break
        elif xinput == '5' and row1[1] == ' ':
            row1[1] = 'X'
            break
        elif xinput == '6' and row1[2] == ' ':
            row1[2] = 'X'
            break
        elif xinput == '7' and row2[0] == ' ':
            row2[0] = 'X'
            break
        elif xinput == '8' and row2[1] == ' ':
            row2[1] = 'X'
            break
        elif xinput == '9' and row2[2] == ' ':
            row2[2] = 'X'
            break
        else:
            print('Please select a valid option.')
    printBoard()
    checkWinner()

def playerControl_O():
    while True:
        oinput = input("- O's turn: ")
        if oinput == '1' and row0[0] == ' ':
            row0[0] = 'O'
            break
        elif oinput == '2' and row0[1] == ' ':
            row0[1] = 'O'
            break
        elif oinput == '3' and row0[2] == ' ':
            row0[2] = 'O'
            break
        elif oinput == '4' and row1[0] == ' ':
            row1[0] = 'O'
            break
        elif oinput == '5' and row1[1] == ' ':
            row1[1] = 'O'
            break
        elif oinput == '6' and row1[2] == ' ':
            row1[2] = 'O'
            break
        elif oinput == '7' and row2[0] == ' ':
            row2[0] = 'O'
            break
        elif oinput == '8' and row2[1] == ' ':
            row2[1] = 'O'
            break
        elif oinput == '9' and row2[2] == ' ':
            row2[2] = 'O'
            break
        else:
            print('Please select a valid option.')

    printBoard()
    checkWinner()

def friendGame():
    print(clearBoard)
    print('- You are player X and your friend is player O')
    def playerX():
        playerControl_X()
    def playerO():
        playerControl_O()

    while True:
        playerX()
        playerO()

def botGame():
    print(clearBoard)
    print('- You are player X and bot is player O')
    def playerX_botGame():
        playerControl_X()
    def botControl():
        randomBot = str(random.randint(1,9))
        while True:
            if randomBot == '1' and row0[0] == ' ':
                row0[0] = 'O'
                break
            elif randomBot == '2' and row0[1] == ' ':
                row0[1] = 'O'
                break
            elif randomBot == '3' and row0[2] == ' ':
                row0[2] = 'O'
                break
            elif randomBot == '4' and row1[0] == ' ':
                row1[0] = 'O'
                break
            elif randomBot == '5' and row1[1] == ' ':
                row1[1] = 'O'
                break
            elif randomBot == '6' and row1[2] == ' ':
                row1[2] = 'O'
                break
            elif randomBot == '7' and row2[0] == ' ':
                row2[0] = 'O'
                break
            elif randomBot == '8' and row2[1] == ' ':
                row2[1] = 'O'
                break
            elif randomBot == '9' and row2[2] == ' ':
                row2[2] = 'O'
                break
            else:
                botControl()

        printBoard()
        checkWinner()
    
    while True:
        playerX_botGame()
        botControl()

while True:
    decision = input('{}\nWill you play with your friend or with a bot?\n1-With friend\n2-With bot\n* Choice: '.format('-'*29))
    if decision == '1':
        print('{}\n- Friend selected\n{}'.format('-'*20,'-'*20))
        friendGame()
        break
    elif decision == '2':
        print('{}\n- Bot selected\n{}'.format('-'*20,'-'*20))
        botGame()
        break
    else:
        print('{}\nPlease select a valid option.'.format('-'*29))