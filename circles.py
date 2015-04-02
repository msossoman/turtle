from turtle import *
turtle = Turtle()

# pink circle - I can't figure out why I have to use fill() twice with the 1st circle. 
# 				If I leave out the first fill() then the pink circle doesn't get filled in.
turtle.color('pink')
turtle.fill(50)
turtle.circle(50)
turtle.fill(50)

turtle.up()
turtle.goto(0, -100)
turtle.down()

# red circle
turtle.color('red')
turtle.circle(50)
turtle.fill(50)

turtle.up()
turtle.goto(0, -200)
turtle.down()

# green circle
turtle.color('green')
turtle.circle(50)
turtle.fill(50)

done()