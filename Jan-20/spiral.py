"""
Created on Wednesday, Jan 19 22:25:25 2022
@author: mrobbins
"""

from turtle import * 

def spiral(firststep, angle, gap):

  step = firststep
  while step > 0:
      forward(step)
      left(angle)

main()
