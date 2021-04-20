from turtle import *
 
circle(100,180)#小半圆
circle(200,180)#大半圆
circle(100,-180)#月牙中半圆

 #黑色填充
fillcolor('black')
begin_fill()
circle(100,180)
circle(200,180)
circle(100,-180)
end_fill()

 #抬起画笔
penup()
goto(0,100)
dot(50)
goto(0,-100)
pencolor('white')
dot(50)

 #隐藏画笔
hideturtle()
done()
