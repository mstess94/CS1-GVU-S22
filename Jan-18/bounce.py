# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:56:14 2022

@author: mrobbins
"""

from turtle import *

def move(distance):
    """ Move forward, recersing direction at the right side."""
    forward(distance)
    if xcor() > 320:
        setheading(180)
        
def main():
    shape("arrow")
    penup()
    speed(1)
    for i in range(100):
        move(10)
        
    exitonclick()
    
main()
    
    
    
    
    
    
    
    