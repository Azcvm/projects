import turtle

win =turtle.Screen()
win.title("asmit ")
win.bgcolor("gray")
win.setup(width=800, height=600)   #screen size
#win.tracer(0)

#scores
score1=0
score2=0
#bat1
bat1= turtle.Turtle()
bat1.speed(0)
bat1.shape("square")
bat1.shapesize(stretch_wid=5,stretch_len=1)
bat1.color("white")
bat1.penup()
bat1.goto(-350,0)

#bat2
bat2= turtle.Turtle()
bat2.speed(0)
bat2.shape("square")
bat2.shapesize(stretch_wid=5,stretch_len=1)
bat2.color("white")
bat2.penup()
bat2.goto(350,0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-0.1


#scorepen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player1 :0   player2 : 0", align="center",font=("courier",24,"normal"))


#bat movement
def bat1_up():
    y=bat1.ycor()
    y += 20
    bat1.sety(y)

def bat1_down():
    y=bat1.ycor()
    y -= 20
    bat1.sety(y)

def bat2_up():
    y=bat2.ycor()
    y += 20
    bat2.sety(y)

def bat2_down():
    y=bat2.ycor()
    y -= 20
    bat2.sety(y)


#keyboard input
win.listen()
win.onkeypress(bat1_up,"w")
win.onkeypress(bat1_down,"s")
win.onkeypress(bat2_up,"Up")
win.onkeypress(bat2_down,"Down")


#game loop

while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy -= 0.2

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy += 0.2

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx -= 0.2
        score1+=1
        pen.clear()
        pen.write("player1 :{}    player2 : {}".format(score1,score2), align="center",font=("courier",24,"normal"))

    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx += 0.2
        score2+=1
        pen.clear()
        pen.write("player1 :{}    player2 : {}".format(score1,score2), align="center",font=("courier",24,"normal"))
    
    #bat and ball
    if (ball.xcor()> 340 and ball.xcor()<350) and (ball.ycor()<bat2.ycor()+ 40 and ball.ycor()>bat2.ycor() -40):
        ball.setx(340)
        ball.dx+= -0.2


    if (ball.xcor()< -340 and ball.xcor()>-350) and (ball.ycor()<bat1.ycor()+ 40 and ball.ycor()>bat1.ycor() -40):
        ball.setx(-340)
        ball.dx += 0.2
    