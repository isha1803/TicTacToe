#!/usr/bin/env python
# coding: utf-8

# In[1]:


print([1,2,3,4,5])


# In[2]:


print([1,2,3])
print([4,5,6])
print([7,8,9])


# In[3]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)


# In[4]:


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 =[' ',' ',' ']
display(row1,row2,row3)


# In[5]:


row2[1]='X'


# In[6]:


display(row1,row2,row3)


# In[7]:


input('please enter a value: ')


# In[8]:


result= input('Please enter a value : ')


# In[9]:


type(result)


# In[10]:


float(result)


# In[11]:


int(result)


# In[12]:


#or

result= input('Enter Value : ')


# In[13]:


result_int= int(result)


# In[14]:


type(result)


# In[15]:


type(result_int)


# In[16]:


int(3.671)


# In[17]:


position_index = int(input('Choose a position : '))


# In[18]:


row1[position_index]


# In[19]:


type(position_index)


# In[20]:


result= input('enter a number : ')


# In[21]:


2+2
2+3


# In[24]:


result= int(input('Enter a number : '))


# In[25]:


def user_choice():
    
    
    choice = input('Please enter a number : ')
    
    return int(choice)


# In[1]:


game_list= [0,1,2]


# In[2]:


def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)


# In[3]:


display_game(game_list)


# In[9]:


def position_choice():
    
    choice = 'wrong'
    
    while choice not in['0', '1', '2']:
        
        choice = input('Pick a Position (0,1,2): ')
        if choice not in ['0','1','2']:
            print('sORRY INVALID CHOICE!')
            
            
    return int(choice)


# In[10]:


position_choice()


# In[11]:


def replacement_choice(game_list,position):
       
       user_placement = input('Type a string to place at position: ')
       
       game_list[position] = user_placement
       
       return game_list


# In[12]:


replacement_choice(game_list,1)


# In[13]:


def gameon_choice():
    
    choice ='wrong'
    
    while choice not in ['Y','N']:
        choice = input('Keep playing? (Y or N) ')
        if choice not in ['Y','N']:
            print("Sorry I don't understand, please choose Y or N")
    if choice == 'Y':
        return True
    else:
        return False 


# In[14]:


gameon_choice()


# In[15]:


game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()


# In[ ]:





# In[ ]:





# In[25]:


from IPython.display import clear_output

def game_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[26]:


board = ['c','X','O','X','O','X','O','X','O','X']
game_board(board)
game_board(board)


# In[27]:


game_board(board)


# In[28]:


def input_marker():
    '''
    OUTPUT =(Player 1 marker, Player 2 marker)
    '''
    
    
    marker=''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
    if marker =='X':
        return ('X','O')
    else:
        return ('O','X')
        


# In[29]:


input_marker()


# In[30]:


player1_marker, player2_marker = input_marker()


# In[31]:


player1_marker


# In[32]:


player2_marker


# In[33]:


def position_marker(board,marker,position):
    board[position] = marker
    return marker


# In[34]:


position_marker(board,'@',5)
game_board(board)


# In[35]:


def win_check(board, marker):
    #TO SEE WHO WON
    
    #CHECK COLUMNS, rows, diagonals
    if (board[7]==board[8] ==board[9]== marker)or (board[4]==board[5] ==board[6]== marker) or (board[1]==board[2] ==board[3]== marker) or (board[7]==board[4] ==board[1]== marker) or (board[8]==board[5] ==board[2]== marker) or (board[9]==board[6] ==board[3]== marker) or (board[7]==board[5] ==board[3]== marker) or (board[1]==board[5] ==board[9]== marker) :
        return True
    else:
        return False


# In[36]:


win_check(board,'X')


# In[37]:


win_check(board,'O')


# In[38]:


import random
    
def choose_first():
    flip= random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[39]:


choose_first()


# In[40]:


def space_check(board,position):
    return board[position] == ' '


# In[41]:


def full_board(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        #Board id=s not full
        
    return True
#board is full


# In[42]:


def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose A Position: (1-9) '))
        
    return position


# In[43]:


range(1,10)


# In[44]:


def replay():
    choice = input('Play again ?: Yes OR No')
    
    return choice == 'Yes'
    


# In[46]:


#WHILE LOOP TO KEEP RUNNING THE GAME

print('Welcome To Tic Tac Toe')
##set everything up(board< who's first, chosen markers)

while True:
    #play the game
    the_board= [' ']*10
    turn = choose_first()
    player1_marker, player2_marker = input_marker()
    
    print(turn + 'will go first')
    
    play_game = input('Ready to play? y or n? :')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on= False
    
    #game play
    while game_on:
        if turn == 'Player 1':
            #show board
            game_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker on position chosen
            position_marker(the_board,player1_marker,position)
            
            #check if they won
            if win_check(the_board,player1_marker) == True:
                game_board(the_board)
                print('Player 1 has Won!!!')
                game_on = False
            else:
                if full_board(the_board):
                    game_board(the_board)
                    print('The game is a tie!')
                    game_on= False
                else:
                    turn = 'Player 2'
       
    
        ##player two turn 
        
        
        else:
            #show board
            game_board(the_board)
            
            #choose position
            position = player_choice(the_board)
            
            #place marker on position chosen
            position_marker(the_board,player2_marker,position)
            
            #check if they won
            if win_check(the_board,player2_marker) == True:
                game_board(the_board)
                print('Player 2 has Won!!!')
                game_on = False
            else:
                if full_board(the_board):
                    game_board(the_board)
                    print('The game is a tie!')
                    game_on= False
                else:
                    turn = 'Player 1'
            
            
    if not replay():
        break



#BREAK OUT OF THE WHILE LOOP ON REPLAY()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




