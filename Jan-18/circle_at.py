# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 17:52:25 2022

@author: mrobbins
"""

from turtle import * 

def circle_at(x, y, r):
    """ Draw a circle with the center at (x, y) and radius r"""
    penup()
    goto(x, y - r)
    pendown()
    setheading(0)
    circle(r)

def main():
    left(90)
    circle_at(100, 100, 50)
    
    circle_at(200, 200, 25)

    exitonclick()
    
    
main()









