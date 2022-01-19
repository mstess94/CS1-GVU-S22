# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:31:01 2022

@author: mrobbins
"""

from turtle import *

def polygon(num_sides, length):
    """ Draw num_sides-sided polygon with given side length"""
    for i in range(num_sides):
        forward(length)
        left(360/num_sides)
        
def main():
    """Draw polygons with 3-9 sides"""
    for j in range(3, 10):
        polygon(j, 80)
    
    exitonclick()
    
main()






