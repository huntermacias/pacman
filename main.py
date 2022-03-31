import turtle
import time

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("A Maze for Pacman")
wn.setup(950,850)
wn.tracer(0)

# Create Character Class
class Character(turtle.Turtle):
  def __init__(self, shape, color, size):
    turtle.Turtle.__init__(self)
    self.shape(shape)
    self.color(color)
    self.penup()
    self.speed(0)
    self.shapesize(size, size, size)
    self.player_dx = 22
    self.player_dy = 22
    self.direction = "Left"
    self.prevDirection = "Left"
    self.nextDirection = "Left"
    self.setheading(90)

  def go_up(self): 
    self.prevDirection = self.direction 
    self.direction = "Up"

  def go_down(self):
    self.prevDirection = self.direction 
    self.direction = "Down"

  def go_left(self):
    self.prevDirection = self.direction 
    self.direction = "Left"

  def go_right(self):
    self.prevDirection = self.direction 
    self.direction = "Right"

  def valid_move(self, x, y, nextDir):
    if((x, y) not in walls): 
        self.goto(x, y)
    else: 
      self.nextDirection = nextDir

  def move(self): 
    if self.direction == "Up": 
      self.nextDirection = self.direction
      next_dir = self.direction
      move_to_x = self.xcor()
      move_to_y = self.ycor() + self.player_dy
      self.valid_move(move_to_x, move_to_y,next_dir)

    elif self.direction == "Down":
      self.nextDirection = self.direction
      next_dir = self.direction
      move_to_x = self.xcor()
      move_to_y = self.ycor() - self.player_dy
      self.valid_move(move_to_x, move_to_y,next_dir)

    elif self.direction == "Left":
      self.nextDirection = self.direction
      next_dir = self.direction
      move_to_x = self.xcor() - self.player_dx
      move_to_y = self.ycor()
      self.valid_move(move_to_x, move_to_y,next_dir)

    elif self.direction == "Right":
      self.nextDirection = self.direction
      next_dir = self.direction
      move_to_x = self.xcor() + self.player_dx
      move_to_y = self.ycor()
      self.valid_move(move_to_x, move_to_y,next_dir)

    # def can_turn(): 
    #   currDir = self.direction; 
    #   new_x = self.xcor() + self.player_dx
    #   new_y = self.ycor() + self.player_dy

    #   if (new_x, new_y) not in walls: 
    #     return True

    #   return False

# Create Levels:
#   level 0 - empty maze
#   Level 1 - easy maze
levels = [""]

my_file = open("board.txt", "r")
level_1 = my_file.readlines()


# Add our maze to our list
levels.append(level_1)

# Create level setup function
def setup_maze(level, walls):
  for row in range(len(level)):
    for col in range(len(level[row])):
      block = level[row][col]            # Get board value at each row,col position

      screen_x = -294 + (col * 22)       # Calculate screen coordinates for row, col
      screen_y = 350  - (row * 22)

      # Check if it is an X (representing another Wall/Block)
      if block == "#":
        walls.append((screen_x, screen_y)) # Add coordinates to wall list
        pen.goto(screen_x, screen_y)
        pen.stamp()
      elif block == ".": 
        pacdots.append((screen_x, screen_y))
        pacdot.goto(screen_x, screen_y)
        pacdot.dot(7, "pink")
      elif block == "O": 
        pacdots.append((screen_x, screen_y))
        pacdot.goto(screen_x, screen_y)
        pacdot.dot(14, "pink")
      elif block == "P": 
        pacman.goto(screen_x, screen_y)
      elif block == "b": 
        Blinky.goto(screen_x, screen_y)
      elif block == "c": 
        Clyde.goto(screen_x, screen_y)
      elif block == "p": 
        Pinky.goto(screen_x, screen_y)
      elif block == "i": 
        Inky.goto(screen_x, screen_y)

def continue_moving(next_dir): 
  pass
  
  
  # currX = pacman.xcor()
  # currY = pacman.ycor()
  # if pacman.direction == "up": 


    # if (currX, currY) not in walls and pacman.nextDirection != "stop": 
    #   pacman.direction = pacman.nextDirection
    # elif (currX, currY) not in walls and pacman.prevDirection != "stop":
    #   pacman.direction = pacman.prevDirection
      



def eatPacdot(score): 
  x = pacman.xcor()
  y = pacman.ycor()

  if (x,y) in pacdots: 
    pacdot.goto(x,y)
    pacdot.dot(14, "black")
    score += 1
    update_score(score)
  return score

def update_score(score):
  scorekeeper.undo()
  scorekeeper.write("Score: " + str(score), font=("arial", 17, "italic"))

# Create player/pen instances
pen = Character("square", "blue", 1)
scorekeeper = Character("classic", "white", 1)
pacman = Character("circle", "yellow", 1)
pacdot = Character("circle", "pink", 0.1)
pacdot.ht()
scorekeeper.ht()

Blinky = Character("turtle", "red", 1)
Clyde = Character("turtle", "orange", 1)
Pinky = Character("turtle", "pink", 1)
Inky = Character("turtle", "cyan", 1)

# Create wall coordinate list 
walls = []
pacdots = []
score = 0

# Set up the level 
setup_maze(levels[1], walls)

# keyboard bindings
turtle.listen()
turtle.onkeypress(pacman.go_left, "Left")
turtle.onkeypress(pacman.go_right, "Right")
turtle.onkeypress(pacman.go_down, "Down")
turtle.onkeypress(pacman.go_up, "Up")

scorekeeper.goto(-295,370)
scorekeeper.write("Score: " + str(score), font=("arial", 17, "italic"))

# Turn off screen updates
wn.tracer(0)

# Game Loop
while True: 
  wn.update()
  # if can_turn():
  pacman.move()
  # continue_moving(pacman.nextDirection)
  # print("Curr", pacman.direction)
  # print("Next", pacman.nextDirection)
  # print()
  score = eatPacdot(score)
  time.sleep(0.03)
      

turtle.mainloop()