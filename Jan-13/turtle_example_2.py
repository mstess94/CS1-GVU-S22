# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:42:57 2022

@author: mrobbins
"""

from turtle import *

pensize(7)
penup()
goto(-200, -100)
pendown()

fillcolor("red")
begin_fill()
goto(-200, 100)
goto(200, -100)
goto(200, 100)
goto(-200, -100)
end_fill()


exitonclick()
