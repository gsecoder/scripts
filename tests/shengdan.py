# -*- encoding: utf-8 -*-
"""
@File    :   shengdan.py
@Time    :   2019/12/2514:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import turtle

screen = turtle.Screen()
screen.setup(800, 600)
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()
circle.goto(0, 280)
circle.stamp()
k = 0
for i in range(1, 17):
    y = 30 * i
    for j in range(i - k):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()
    if i % 4 == 0:
        x = 30 * (j + 1 )
        circle.color('red')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x,-y + 280)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30 * (j + 1)
        circle.color('yellow')
        circle.goto(-x, -y + 280)
        circle.stamp()
        circle.goto(x, -y + 280)
        circle.stamp()
square.color('brown')
for i in range(17,20):
    y = 30 * i
    for j in range(3):
        x = 30 * j
        square.goto(x, -y + 280)
        square.stamp()
        square.goto(-x, -y + 280)
        square.stamp()
turtle.exitonclick()
