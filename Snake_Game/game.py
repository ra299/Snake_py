import turtle
import time
import random

delay = 0.2
#____Score
score = 0
high_score = 0

#____set up the screen

wn = turtle.Screen()
wn.title("Snake Game by Rahul")
wn.bgcolor("red")
wn.setup(width=600, height=600)
wn.tracer(0)   #____Turns of the screen update

#___    _Snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

#____Snake Food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0,100)

segments = []

#____Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")  
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 Hig Score: 0", align="center", font=("courier",24,"normal"))

#____Function

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#____Keyboard bindings

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


#____Main Game loop

while True:
    wn.update()

    #____acheck for a collision with the border   
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #____hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #____clear the segments list
        segments.clear()

        #____Reset the score
        score = 0

        #___Reset the dealy
        delay = 0.5

        #____update the score display
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score, high_score), align="center",font=("courier",24,"normal"))


    #____check for a collision with the food

    if head.distance(food) < 20:
        #____Move the food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        #____Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #____shoreten the dealay
        delay -=0.001

        #____Increase the soore
        score += 1

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("courier",24,"normal"))

    #____move the end segment frist in reverse order

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #____Move segment 0 to where the head is

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()

    #____check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

              #____hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

        #____clear the segments list
            segments.clear()
        #____Reset the score
            score = 0

        #____Reset the dealy
            delay = 0.1

        #____update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("courier",24,"normal"))    
    time.sleep(delay)

wn.mainloop()
