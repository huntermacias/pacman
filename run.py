import turtle
import time
import math
import random
from utils import *


# READING BOARD FROM TEXT FILE
board = open("pacman/board.txt", "r") 
board_lines = board.readlines()
board = ""
for line in board_lines:
	board += line

# REPLACE BOARD WITH ITS NUMERICAL VALUES
board_dict = {"#": "0",	".": "1",	"O": "2", 	"_": "3"}
for bk in board_dict.keys():
	board = board.replace(bk, board_dict[bk])
board.strip()

# INIT GAME VARIABLES
W = 1100
H = 950
playing = True
box_size = 14
food_size = 8


# create Turtles from utils.py -> PARAMETERS: shape, color, startx=0, starty=0, dx=0, dy=0
pacman = create_turtle("circle", "yellow", 0,0,4,4)
food = create_turtle("classic", "pink", -400, 475, 0,0, "yes")
pen = create_turtle("classic", "blue")


screen = turtle.Screen()
screen.bgcolor("Black")
screen.setup(W,H,-4000,0)
screen.tracer(0)

def drawfood(boardnum, food_size):
	x = food.xcor()
	y = food.ycor()

	for f in board:
		food.forward(15)
		if f ==  "1":
			food.dot(food_size, "White")
		elif f == "2":
			food.dot(food_size * 2, "White")
		elif f == "\n":
			food.goto(x,y-30)
			x = food.xcor()
			y = food.ycor()

def rectangle(w,h,x,y):
	pen.penup()
	pen.goto(x,y)
	pen.pendown()
	pen.begin_fill()
	for i in range(0,4):
		pen.forward(w)
		pen.left(90)
		pen.forward(h)
		pen.left(90)
	pen.end_fill()

def draw_walls():
     #         w,   h,   x,   y
	rectangle(800, 15, -380, 435) # top wall
	rectangle(800, 15,-380, -435) # bottom wall
	rectangle(15, 330 , -395, -435) # bottom left side wall
	rectangle(15, 290 , -395, 160) # top left side wall 
	rectangle(160, 15, -395, 160) # left inner wall 1
	rectangle(15, 115, -250, 60) # left inner wall 2
	rectangle(160, 15, -395, 60) # left inner wall 3


def curve(weight, x, y):
	pen.penup()
	pen.goto(x, y)
	pen.pendown()
	pen.setheading(-90)
	length = weight*math.pi/36
	pen.begin_fill()
	for i in range(9):
		pen.forward(length)
		pen.right(10)
		pen.setheading(180)
		pen.forward(weight/2)
		pen.left(90)
		pen.forward(weight)
		pen.left(90)
		pen.forward(weight/2)
		pen.left(90)
		pen.right(90)
		pen.forward(weight/2)
	for i in range(18):
		pen.left(5)
		pen.forward(length)
		pen.forward(weight/2)
		pen.left(90)
		pen.forward(weight)
		pen.end_fill()
		pen.setheading(0)

# pacman movements
def pac_move():
	x = pacman.xcor()
	y = pacman.ycor()
	if pacman.direction == "left":
		pacman.goto(x-pacman.dy, y)
	elif pacman.direction == "right":
		pacman.goto(x+pacman.dy, y)
	elif pacman.direction == "up":
		pacman.goto(x, y+pacman.dx)
	elif pacman.direction == "down":
		pacman.goto(x, y-pacman.dx)

def pac_left():
	pacman.direction = "left"
def pac_right():
	pacman.direction = "right"
def pac_up():
	pacman.direction = "up"
def pac_down():
	pacman.direction = "down"

drawfood(board,food_size)
draw_walls()



screen.onkeypress(pac_left, "Left")
screen.onkeypress(pac_right, "Right")
screen.onkeypress(pac_up, "Up")
screen.onkeypress(pac_down, "Down")
screen.listen()

# Main game loop
while playing:
	screen.update()
	pac_move()
	time.sleep(.045)


turtle.mainloop()