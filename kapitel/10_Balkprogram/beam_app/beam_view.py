# -*- coding: utf-8 -*-
"""
Modul som implementerar klassen BeamView

@author: Jonas Lindemann
"""

import beam_model as bm
import draw_view as dv

class BeamView(dv.DrawView):
    """BeamView klass för att rita upp modell och resultat"""

    def __init__(self, beam_model, figure):
        """BeamView konstruktor"""

        # BeamView ärver från DrawView varför
        # vi måste anropa dess konstruktor

        super().__init__()

        # Referenser till figur och balkmodell

        self.fig = figure
        self.beam_model = beam_model

        # Attribut för att de olika axes-objekten
        # för uppritning.

        self.axes_geometry = None
        self.axes_top = None
        self.axes_middle = None
        self.axes_bottom = None

        # Attribut som styr utseendet av uppritningen.
        
        self.support_rel = 0.008
        self.load_rel = 0.02
        

    def setup_plots(self):
        """Konfigurera plot yta"""

        # Rensa figur

        self.fig.clear()

        # Konfigurera subplottar

        self.axes_geometry = self.fig.add_subplot(411)
        self.axes_top = self.fig.add_subplot(412)
        self.axes_middle = self.fig.add_subplot(413)
        self.axes_bottom = self.fig.add_subplot(414)

        self.fig.subplots_adjust(left=0.1, bottom=0.05,
                                 right=0.95, top=0.95,
                                 wspace=0.0, hspace=0.7)

    def draw_diagrams(self):
        """Rita diagram"""

        # Tilldela variabler som används vid
        # uppritningen.

        V = self.beam_model.NVM[:, 1]
        M = self.beam_model.NVM[:, 2]

        V_max = V.max()
        V_min = V.min()

        M_max = M.max()
        M_min = M.min()

        y_max = self.beam_model.y_displ.max()
        y_min = self.beam_model.y_displ.min()

        # Rita resultatdiagram
        
        self.axes_top.set_title("Deformationer")
        self.axes_top.set_ylim(y_min, y_max)
        self.axes_top.axhline(color='black', linewidth=1)
        self.axes_top.plot(self.beam_model.x, self.beam_model.y_displ)

        self.axes_middle.set_title("Tvärkrafter")
        self.axes_middle.set_ylim(V_max, V_min)
        self.axes_middle.axhline(color='black', linewidth=1)
        self.axes_middle.plot(self.beam_model.x, V, color='black')
        self.axes_middle.fill_between(self.beam_model.x, 0, V, facecolor='b')

        self.axes_bottom.set_title("Moment")
        self.axes_bottom.set_ylim(M_max, M_min)
        self.axes_bottom.axhline(color='black', linewidth=1)
        self.axes_bottom.plot(self.beam_model.x, M, color='black')
        self.axes_bottom.fill_between(self.beam_model.x, 0, M, facecolor='r')
        
    def draw_geometry(self):
        """Rita upp geometri och laster"""

        # Konfigurera axes objekt.
        
        self.axes_geometry.set_title("Geometri, randvillkor och laster")
        self.axes_geometry.set_xlim(self.axes_top.get_xlim())

        # Beräkna totallängd och max q last

        tot_length = sum(self.beam_model.lengths)
        q_max = abs(max(self.beam_model.loads))

        # Attribut för DrawView

        self.axes = self.axes_geometry
        self.line_width = 2
        
        x = 0

        for l, n, q, p, s in zip(self.beam_model.lengths,
                                 self.beam_model.segments, 
                                 self.beam_model.loads, 
                                 self.beam_model.properties,
                                 self.beam_model.supports):

            # Rita linje för balk

            self.face_color = 'turquoise'
            self.rect(x, 0.0, l, -q*tot_length*self.load_rel/q_max)
            self.line(x, 0.0, x + l, 0.0)
            self.face_color = 'white'

            # Rita randvillkor
            
            if s == bm.BeamModel.FIXED_XY:
                self.triangle(x, 0.0, tot_length*self.support_rel*2, tot_length*self.support_rel*2)
            elif s == bm.BeamModel.FIXED_Y:
                self.circle(x, -tot_length*self.support_rel, tot_length*self.support_rel)
            else:
                self.line_width = 4
                self.edge_color = 'gray'
                self.line(x, -tot_length*self.support_rel*3, x, tot_length*self.support_rel*3)
                self.line_width = 2
                self.edge_color = 'black'
            x += l

        # Rita sista randvillkoret
            
        if self.beam_model.supports[-1] == bm.BeamModel.FIXED_XY:
            self.triangle(x, 0.0, tot_length*self.support_rel, tot_length*self.support_rel)
        elif self.beam_model.supports[-1] == bm.BeamModel.FIXED_Y:
            self.circle(x, -tot_length*self.support_rel, tot_length*self.support_rel)
        else:
            self.line_width = 4
            self.edge_color = 'gray'
            self.line(x, -tot_length*self.support_rel*3, x, tot_length*self.support_rel*3)
            self.line_width = 2
            self.edge_color = 'black'


        # Stäng av axlar och sätt lika skalning i båda riktningar

        self.axes_geometry.axis('off')
        self.axes_geometry.axis('equal')


    def draw(self):
        """Rutin för att rita upp allting"""

        self.setup_plots()
        self.draw_diagrams()
        self.draw_geometry()

        # Dessa kommandon måste anropas
        # för att diagrammen skall uppdateras

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()