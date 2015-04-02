from turtle import *

# pink circle - I can't figure out why I have to use fill() twice with the 1st circle 
# 				If I leave out the first fill() then the pink circle doesn't get filled in
color('pink')
fill(50)
circle(50)
fill(50)

up()
goto(0, -100)
down()

# red circle
color('red')
circle(50)
fill(50)

up()
goto(0, -200)
down()

# green circle
color('green')
circle(50)
fill(50)

done()