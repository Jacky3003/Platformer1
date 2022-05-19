import turtle

wn = turtle.Screen()
wn.title('Platformer by Jacky')
wn.bgcolor('light green')
wn.tracer(0)
wn.screensize(800, 800)

# player in game

player = turtle.Turtle()
player.speed(0)
player.shape('square')
player.penup()
player.goto(-300, -250)
player.shapesize(2, 2)
player.color('blue')
player.dy = 0.5
player.dx = 0.3

# platforms

platone = turtle.Turtle()
platone.speed(0)
platone.shape('square')
platone.penup()
platone.goto(-300, -300)
platone.shapesize(1, 7)
platone.color('grey')

plat_hor = turtle.Turtle()  # moving horizontally
plat_hor.speed(0)
plat_hor.penup()
plat_hor.goto(-200, -250)
plat_hor.shapesize(1, 5)
plat_hor.color('grey')
plat_hor.shape('square')
plat_hor.dx = 0.3

plattwo = turtle.Turtle()
plattwo.speed(0)
plattwo.shape('square')
plattwo.penup()
plattwo.goto(-150, -150)
plattwo.shapesize(1, 7)
plattwo.color('grey')

plat_vert = turtle.Turtle()  # moving vertically
plat_vert.speed(0)
plat_vert.shape('square')
plat_vert.penup()
plat_vert.goto(250, -225)
plat_vert.shapesize(7, 3)
plat_vert.color('red')
plat_vert.dy = 0.5

platthree = turtle.Turtle()
platthree.speed(0)
platthree.shape('square')
platthree.penup()
platthree.goto(400, -100)
platthree.shapesize(2, 4)
platthree.color('grey')

platfour = turtle.Turtle()
platfour.speed(0)
platfour.shape('square')
platfour.penup()
platfour.goto(0, 0)
platfour.shapesize(1, 15)
platfour.color('grey')

platfive = turtle.Turtle()
platfive.speed(0)
platfive.shape('square')
platfive.penup()
platfive.goto(-400, 0)
platfive.shapesize(3, 7)
platfive.color('grey')

finish = turtle.Turtle()
finish.speed(0)
finish.shape('square')
finish.penup()
finish.goto(-400, 60)
finish.shapesize(3, 3)
finish.color('dark green')


# score for coins

title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(-450, 350)
title.write('Stage', align='left', font=('helvetica', 20, 'bold'))

coin_one = turtle.Turtle()
coin_one.penup()
coin_one.speed(0)
coin_one.shape('square')
coin_one.shapesize(1, 1)
coin_one.color('yellow')
coin_one.goto(400, -60)

coin_two = turtle.Turtle()
coin_two.penup()
coin_two.speed(0)
coin_two.shape('square')
coin_two.shapesize(1, 1)
coin_two.color('yellow')
coin_two.goto(-150, -120)

coin_three = turtle.Turtle()
coin_three.penup()
coin_three.speed(0)
coin_three.shape('square')
coin_three.shapesize(1, 1)
coin_three.color('yellow')
coin_three.goto(0, 30)

# spikes

spike_one = turtle.Turtle()
spike_one.penup()
spike_one.shape('triangle')
spike_one.shapesize(2, 2)
spike_one.color('red')
spike_one.goto(-50, 22)
spike_one.tilt(90)
spike_one.tiltangle()
spike_one.dx = 0.3

spike_two = turtle.Turtle()
spike_two.penup()
spike_two.shape('triangle')
spike_two.shapesize(2, 2)
spike_two.color('red')
spike_two.goto(50, 22)
spike_two.tilt(90)
spike_two.tiltangle()
spike_two.dx = 0.3

# player movement, functions and buttons


def left():
    x = player.xcor()
    x -= 15
    player.setx(x)


def right():
    x = player.xcor()
    x += 15
    player.setx(x)


def jump():
    if player.ycor() < 175:
        y = player.ycor()
        y += 100
        player.sety(y)

wn.onkeypress(right, 'd')
wn.onkeypress(left, 'a')
wn.onkeypress(jump, 'w')
wn.listen()

while True:

    wn.update()


    plat_hor.setx(plat_hor.xcor() + plat_hor.dx)
    plat_vert.sety(plat_vert.ycor() + plat_vert.dy)

    if plat_hor.xcor() > 300:
        plat_hor.dx = -plat_hor.dx
    if plat_hor.xcor() < -200:
        plat_hor.dx = -plat_hor.dx

    spike_one.setx(spike_one.xcor() + spike_one.dx)
    spike_two.setx(spike_two.xcor() + spike_two.dx)

    if spike_one.xcor() < -130:
        spike_one.dx = -spike_one.dx
    if spike_one.xcor() > -40:
        spike_one.dx = -spike_one.dx

    if spike_two.xcor() > 130:
        spike_two.dx = -spike_two.dx
    if spike_two.xcor() < 40:
        spike_two.dx = -spike_two.dx

    if plat_vert.ycor() > 300:
        plat_vert.dy = -plat_vert.dy
    if plat_vert.ycor() < -300:
        plat_vert.dy = -plat_vert.dy

    if player.ycor() < player.ycor() + 1:
        player.sety(player.ycor() - player.dy)
        if player.ycor() < platone.ycor() + 30 and (platone.xcor() - 80 < player.xcor() < platone.xcor() + 80 and player.ycor() > platone.ycor()):
            player.sety(platone.ycor() + 30)

        if player.ycor() < platthree.ycor() + 40 and (platthree.xcor() - 60 < player.xcor() < platthree.xcor() + 60 and player.ycor() > platthree.ycor()):
            player.sety(platthree.ycor() + 40)

        if player.ycor() < plattwo.ycor() + 30 and (plattwo.xcor() - 95 < player.xcor() < plattwo.xcor() + 95 and player.ycor() > plattwo.ycor()):
            player.sety(plattwo.ycor() + 30)

        if player.ycor() < platfour.ycor() + 30 and (platfour.xcor() - 170 < player.xcor() < platfour.xcor() + 170 and player.ycor() > platfour.ycor()):
            player.sety(platfour.ycor() + 30)

        if player.ycor() < platfive.ycor() + 50 and (platfive.xcor() - 90 < player.xcor() < platfive.xcor() + 90 and player.ycor() > platfive.ycor()):
            player.sety(platfive.ycor() + 50)

        if player.ycor() < plat_hor.ycor() + 30 and (plat_hor.xcor() - 70 < player.xcor() < plat_hor.xcor() + 70 and player.ycor() > plat_hor.ycor()):
            player.sety(plat_hor.ycor() + 30)
            player.setx(plat_hor.xcor())

        if plat_vert.xcor() - 40 < player.xcor() < plat_vert.xcor() + 40 and plat_vert.ycor() - 75 < player.ycor() < plat_vert.ycor() + 75:

            # player.ycor() < plat_vert.ycor() + 30 and (plat_vert.xcor() - 40 < player.xcor() < plat_vert.xcor() + 40 and player.ycor() > plat_vert.ycor()):

            player.sety(plat_vert.ycor() + 30)
            title.clear()
            title.write('Game Over :(, starting over...', align='left', font=('helvetica', 20, 'bold'))
            player.setpos(-300, -250)
            coin_one.showturtle()
            coin_two.showturtle()
            coin_three.showturtle()

    if coin_one.xcor() - 10 < player.xcor() < coin_one.xcor() + 10 and coin_one.ycor() - 10 < player.ycor() < coin_one.ycor() + 10:
        coin_one.hideturtle()
        title.clear()
        title.write('Great!', align='left', font=('helvetica', 20, 'bold'))

    if coin_two.xcor() - 10 < player.xcor() < coin_two.xcor() + 10 and coin_two.ycor() - 10 < player.ycor() < coin_two.ycor() + 10:
        coin_two.hideturtle()
        title.clear()
        title.write('Keep Going!', align='left', font=('helvetica', 20, 'bold'))

    if coin_three.xcor() - 10 < player.xcor() < coin_three.xcor() + 10 and coin_three.ycor() - 10 < player.ycor() < coin_three.ycor() + 10:
        coin_three.hideturtle()
        title.clear()
        title.write('Doing good!'.format(1), align='left', font=('helvetica', 20, 'bold'))

    if finish.xcor() - 20 < player.xcor() < finish.xcor() + 20 and finish.ycor() - 20 < player.ycor() < finish.ycor() + 20:
        if not(coin_three.isvisible()):
            if not(coin_two.isvisible()):
                if not(coin_one.isvisible()):
                    title.clear()
                    title.write('Clear! Starting over...', align='left', font=('helvetica', 20, 'bold'))
                    player.setpos(-300, -250)
                    coin_one.showturtle()
                    coin_two.showturtle()
                    coin_three.showturtle()

    if spike_one.xcor() - 20 < player.xcor() < spike_one.xcor() + 20 and spike_one.ycor() - 20 < player.ycor() < spike_one.ycor() + 20:
        title.clear()
        title.write('Game Over :(, starting over...', align='left', font=('helvetica', 20, 'bold'))
        player.setpos(-300, -250)
        coin_one.showturtle()
        coin_two.showturtle()
        coin_three.showturtle()

    if spike_two.xcor() - 20 < player.xcor() < spike_two.xcor() + 20 and spike_two.ycor() - 20 < player.ycor() < spike_two.ycor() + 20:
        title.clear()
        title.write('Game Over :(, starting over...', align='left', font=('helvetica', 20, 'bold'))
        player.setpos(-300, -250)
        coin_one.showturtle()
        coin_two.showturtle()
        coin_three.showturtle()

    if player.ycor() < -400:
        title.clear()
        title.write('Game Over :(, starting over...', align='left', font=('helvetica', 20, 'bold'))
        player.setpos(-300, -250)
        coin_one.showturtle()
        coin_two.showturtle()
        coin_three.showturtle()







