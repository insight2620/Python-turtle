from turtle import *
 
circle(100,180)
circle(200,180)
circle(100,-180)
 
fillcolor('black')
 
begin_fill()
 
circle(100,180)
circle(200,180)
circle(100,-180)
 
end_fill()
 
penup()
 
goto(0,100)
dot(50)
goto(0,-100)
pencolor('white')
dot(50)
 
hideturtle()
 
done()
