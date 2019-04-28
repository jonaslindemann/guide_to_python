# -*- coding: utf-8 -*-
"""
Modul för klassen DrawView

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt

class DrawView(object):
    """Klass för att förenkla uppritning med Matplotlib"""
    def __init__(self):
        """Klasskonstruktor"""

        # Attribut för uppritning
        
        self.edge_color = 'black'
        self.face_color = 'yellow'
        self.line_width = 1
        self.axes = None
        self.fill = True
        self.close_polygon = False
        
    def line(self, x1, y1, x2, y2):
        """Lägg till en linje"""

        line = plt.Line2D((x1, x2), (y1, y2), c=self.edge_color, 
                          lw=self.line_width)
        
        self.axes.add_line(line)
        
    def polygon(self, points):
        """Lägg till en polygon med punkter"""

        line = plt.Polygon(points, closed=self.close_polygon, 
                           fill=self.fill, ec=self.edge_color, 
                           fc=self.face_color, lw=self.line_width)

        self.axes.add_line(line)
        
    def rect(self, x, y, w, h):
        """Lägg till en rektangel"""

        rectangle = plt.Rectangle((x, y), w, h, fc=self.face_color, 
                                  ec=self.edge_color, lw=self.line_width)

        self.axes.add_patch(rectangle)
        
    def circle(self, x, y, r):
        """Lägg till en cirkel"""

        circle = plt.Circle((x, y), radius=r, fc=self.face_color, 
                            ec=self.edge_color, zorder=100, lw=self.line_width)

        self.axes.add_patch(circle)            
        
    def triangle(self, x, y, w, h):
        """
        Lägg till en triangel med bredd och höjd

              (x, y)
              o -------
                      | h
                      |
           o     o ----

           |-----|
              w
        """
        
        points = [[x, y], [x+w/2,y-h], [x-w/2, y-h]]
        self.close_polygon = True
        self.fill = True
        self.polygon(points)
