import turtle

def create_turtle(shape, color, startx=0, starty=0, dx=0, dy=0, hide="no"):
	t = turtle.Turtle()
	t.shape(shape)
	t.color(color)
	t.penup()
	t.goto(startx, starty)
	t.velocity = dx
	t.speed(0)
	t.setheading(0)
	t.direction = "stop"
	t.dx = dx
	t.dy = dy
	if hide == "yes":
		t.hideturtle()
	return t
