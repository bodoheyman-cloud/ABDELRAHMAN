 #import modules
import random
import curses
#initialize the curse library to create our screen
screen = curses.initscr()
#hide the mouse curse
curses.curs_set(0)
#getmax screen hight and width
screen_hight, screen_width = screen.getmaxyx()
#create new window
window = curses.newwin(screen_hight, screen_width, 0, 0)
 #allow window to recive keyboard arrows
window.keypad(1)
#set the dely for updating the screen
window.timeout(150)
#set the x,y coordinates of the initial position of snake's head
snk_x = screen_width // 2
snk_y = screen_hight // 4
#define the initial position of the snake body
snake = [
[snk_y, snk_x],
[snk_y-1, snk_x],
[snk_y-2, snk_x]
]
#create the food in the middle of window
food = [screen_hight // 2, screen_width // 2]
#add the food using PI charcter from curses module
window.addch(food[0], food[1], curses.ACS_DIAMOND) 
#set initial movment direction to right
key = curses.KEY_RIGHT
#create game loops that loops forever untill player loses or quits
while True:
    #get the next key that will be pressed by player
    next_key = window.getch()
    #if user doesnt input anything, key remains same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key
    #check if snake crashed in the walls or touched itself
    if snake[0][0] in [0, screen_hight] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
     #if it crashed close the window and exit
     curses.endwin
     quit()
    #set the new position of snake head based of direction
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
#insert the new head to the first position of snake's head in list
    snake.insert(0, new_head)
#check if snake ate the food
    if snake[0] == food:
        #remove food if snake ate it
        food = None
        #while food is removed, generate new food in a random place on screen
        while food is None:
         new_food = [
         random.randint(1, screen_hight-1),
         random.randint(1, screen_width-1),
         ]
           #set the food to new food if new food generated is not in snake body and add it to screen
         food = new_food if new_food not in snake else None
         window.addch(food[0], food[1], curses.ACS_DIAMOND)
    #otherwise remove the last part of snake body
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')
    #update the position of the snake on the screen
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD) 