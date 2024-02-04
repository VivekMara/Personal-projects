import turtle

#create a screen
wn = turtle.Screen()
wn.title("PONG Game")
wn.bgcolor('black')
wn.setup(width = 800, height = 600)
wn.tracer(0)#stops updating the screen i.e we have to manually update the screen

#score
score_A = 0
score_B = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)



#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1#every time the ball moves it moves by 2 pixels
ball.dy = 0.1

#scorecard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A : 0  Player B : 0", align = "center", font = ("courier", 20, 'normal') )







#functions
def paddle_a_up():
    y = paddle_a.ycor()#returns the y co ordinate 
    y += 20#adds 20 pixels to y co ordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()#returns the y co ordinate 
    y -= 20#adds 20 pixels to y co ordinate
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()#returns the y co ordinate 
    y += 20#adds 20 pixels to y co ordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()#returns the y co ordinate 
    y -= 20#adds 20 pixels to y co ordinate
    paddle_b.sety(y)


#keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, 'w') #user presses w which calls the paddle_a_up function
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


#main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy = ball.dy * -1 #reverses the direction

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy = ball.dy * -1 #reverses the direction

    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_A += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_A, score_B), align = "center", font = ("courier", 20, 'normal') )
    
    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_B += 1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_A, score_B), align = "center", font = ("courier", 20, 'normal') )

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <  -340 and ball.xcor() >  -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
