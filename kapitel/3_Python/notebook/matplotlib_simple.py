#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:42:19 2018

@author: lindemann
"""

import matplotlib.pyplot as plt
import matplotlib.patches as pltp
import matplotlib.lines as pltl

current_fill_color = "w"
current_stroke_color = "k"
current_line_style = "-"
current_line_width = 1.0

_axes = None

do_stroke = True
do_fill = True


def fill(c):
    global do_fill, current_fill_color
    do_fill = True
    current_fill_color = c
    
def no_fill():
    global do_fill    
    do_fill = False
    
def stroke(c):
    global do_stroke, current_stroke_color
    do_stroke = True
    current_stroke_color = c

def no_stroke():
    global do_stroke
    do_stroke = False
    
def line_style(ls):
    global current_line_style
    current_line_style = ls
    
def line_width(lw):
    global current_line_width
    current_line_width = lw
    
def setup():
    plt.axes()
    plt.gcf().patch.set_facecolor('lightgray')    
    #plt.gca().set_facecolor((0.5, 0.9, 0.9))
    
    
def show():
    plt.axis("scaled")
    plt.axis("off")
    plt.show()


def ellipse(x, y, w, h):
    if do_stroke:
        ellipse = pltp.Ellipse((x, y), w, h, fc = current_fill_color, fill=do_fill, ec=current_stroke_color, ls=current_line_style)
    else:
        ellipse = pltp.Ellipse((x, y), w, h, fc = current_fill_color, fill=do_fill)
    plt.gca().add_patch(ellipse)
    
def rect(x, y, w, h):
    if do_stroke:
        rect = pltp.Rectangle((x, y), w, h , 
                              fc = current_fill_color, 
                              fill=do_fill, 
                              ec=current_stroke_color, 
                              ls=current_line_style, 
                              lw=current_line_width)
    else:
        rect = pltp.Rectangle((x, y), w, h , 
                              fc = current_fill_color, 
                              fill=do_fill)
        
    plt.gca().add_patch(rect)
    
def line(x1, y1, x2, y2):
    line = pltl.Line2D((x1, x2), (y1, y2), 
                       c=current_stroke_color, 
                       ls=current_line_style, 
                       lw=current_line_width)
    plt.gca().add_line(line)
    
