import turtle
import time
import random

delay = 0.1

#set  up  the screen
wn = turtle.Screen()
wn.title("snake game By Eshwar")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)


#snakle head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"


# snk food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



segments = []




#functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"



def move():
    if  head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if  head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if  head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if  head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


##keyboard
wn.listen()
wn.onkeypress(go_up   , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left , "a")




#main game loop
while True:
    wn.update()

    # chweack for collision with food
    if head.distance(food) < 20:
        # new spot to food
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)



        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

    #move the tail first
        for i in range(len(segments)-1,0,-1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x,y)

        #move segment 0 to the head
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)

            

    move()

    time.sleep(delay)

wn.mainloop()

