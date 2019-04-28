# -*- coding: utf-8 -*-
"""
Modul som innehåller klassdefinitionen för BeamModel

@author: Jonas Lindemann
"""

import calfem.core as cfc
import numpy as np

import json

class BeamModel(object):
    """Balk klass för att beräkna en kontinuerlig balk"""

    FIXED_Y = 1
    FIXED_XY = 2
    FIXED_XYR = 3

    def __init__(self):
        """Klasskonstruktor"""

        self.new()
        
    def new(self):
        """Initiera balkmodell"""

        self.lengths = [2.0, 3.0]
        self.segments = [10, 20]
        self.loads = [0.0, 0.0]
        self.supports = [BeamModel.FIXED_XY, BeamModel.FIXED_Y, BeamModel.FIXED_XYR]
        self.properties = None

        # Attribut som lagrar värden som tas fram vid beräkningen
        # och som behövs för att kunna rita upp modellen i
        # det grafiska gränssnittet.

        self.n_dofs = 0
        self.n_elements = 0
        self.x = None
        self.support_dofs = []
        self.y_displ = None
        self.x_displ = None
        self.rot = None
        self.NVM = None

    def solve(self):
        """Löser ett system av kontinuerliga balkar"""

        # Kontrollera att vi har materialegenskaper
        
        E = 2.1e9
        A = 0.1 * 0.1
        I = 0.1 * (0.1 ** 3) / 12

        if self.properties == None:
            self.properties = []
            for i in enumerate(self.segments):
                self.properties.append([E, A, I])

        # Beräkna antal element och frihetsgrader

        self.n_dofs = 0
        self.n_elements = 0

        for n in self.segments: 
            self.n_dofs += n * 3
            self.n_elements += n

        self.n_dofs += 3

        # Global styvhetsmatris och lastvektor

        K = np.zeros((self.n_dofs, self.n_dofs), float)
        f = np.zeros((self.n_dofs, 1), float)

        # Elementtopologimatris. Varje rad representerar
        # ett element och dess frihetsgradskopplingar.

        edof = np.zeros((self.n_elements, 6), int)

        # Elementkoordinatsmatriser. Varje rad
        # anger koordinaterna för varje element

        ex = np.zeros((self.n_elements, 2), float)
        ey = np.zeros((self.n_elements, 2), float)

        # Elementegenskapsmatris. Anger elementegenskaperna
        # för varje element.

        ep = np.zeros((self.n_elements, 3), float)

        # Elementlastvektor. Anger elementlasten för varje
        # element.

        eq = np.zeros((self.n_elements, 2), float)

        # X-koordinat för varje beräkningspunkt.

        self.x = np.zeros((self.n_elements+1), float)

        # Assemblera styvhetsmatrisen

        dof = 1 # Räknare för frihetsgrader
        el = 0  # Elementräknare
        self.support_dofs = [] # Randvillkor för varje upplag
        x = 0.0 # Aktuell x-koordinat för element

        for l, n, q, p in zip(self.lengths, self.segments, self.loads, self.properties):
            l_n = l / n
            self.support_dofs.append([dof, dof+1, dof+2])
            for i in range(n):

                # Tilldela elementkoordinater

                ex[el, :] = [x, x + l_n]
                ey[el, :] = [0.0, 0.0]
                ep[el, :] = p
                eq[el, :] = [0.0, q]
                x += l_n

                # Beräkna element styvhet

                Ke, fe = cfc.beam2e(ex[el, :], ey[el, :],
                                    ep[el, :], eq[el, :])

                # Tilldela elementtopologi

                etopo = np.array([dof, dof+1, dof+2, dof+3, dof+4, dof+5])
                dof += 3

                # Assemblera in element i global styvhetsmatris

                cfc.assem(etopo, K, Ke, f, fe)
                edof[el, :] = etopo
                el += 1

        # Lägg till randvillkor för sista upplaget

        self.support_dofs.append([dof, dof+1, dof+2])

        # Tillämpa randvillkor

        bc_prescr = []
        bc_val = []

        for dofs, support in zip(self.support_dofs, self.supports):
            if support == BeamModel.FIXED_Y:
                bc_prescr.append(dofs[1])
                bc_val.append(0.0)
            elif support == BeamModel.FIXED_XY:
                bc_prescr.append(dofs[0])
                bc_val.append(0.0)
                bc_prescr.append(dofs[1])
                bc_val.append(0.0)
            elif support == BeamModel.FIXED_XYR:
                bc_prescr.append(dofs[0])
                bc_val.append(0.0)
                bc_prescr.append(dofs[1])
                bc_val.append(0.0)
                bc_prescr.append(dofs[2])
                bc_val.append(0.0)

        # Lösning av ekvationssystem

        a, _ = cfc.solveq(K, f, np.asarray(bc_prescr), np.asarray(bc_val))

        # Tilldela resultatvariabler

        self.y_displ = a[1::3]
        self.x_displ = a[0::3]
        self.rot = a[2::3]

        # Beräkna inre krafter och förskjutningar

        ed = cfc.extractEldisp(edof, a)

        # Skapa matris för de inre krafterna

        self.NVM = np.zeros((self.y_displ.shape[0], 3), float)

        # Beräkna elementkrafter

        i = 0

        for el_displ, el_x, el_y, el_ep, el_eq in zip(ed, ex, ey, ep, eq):
            es = cfc.beam2s(el_x, el_y, el_ep, el_displ, el_eq)
            self.NVM[i, :] = es[0][0]
            self.x[i] = el_x[0]
            i += 1

        # Sista positionen måste också tilldelas

        self.NVM[i, :] = es[0][1]
        self.x[i] = el_x[1]

    def save_as_json(self, filename):
        """Save beam model as json file"""

        beam_dict = {}
        beam_dict["lengths"] = self.lengths
        beam_dict["segments"] = self.segments
        beam_dict["loads"] = self.loads
        beam_dict["supports"] = self.supports
        beam_dict["properties"] = self.properties

        with open(filename, "w") as json_file:
            json.dump(beam_dict, json_file, sort_keys=True, indent=4)

    def open_from_json(self, filename):
        """Load beam model from json file"""

        with open(filename, "r") as json_file:
            beam_dict = json.load(json_file)
            self.lengths = beam_dict["lengths"]
            self.segments = beam_dict["segments"]
            self.loads = beam_dict["loads"]
            self.supports = beam_dict["supports"]
            self.properties = beam_dict["properties"]
                            
if __name__ == "__main__":

    beam = BeamModel()
    beam.lengths = [2.0, 2.0, 3.0]
    beam.segments = [100, 100, 100]
    beam.supports = [Beam.FIXED_XY, Beam.FIXED_Y, Beam.FIXED_Y, Beam.FIXED_XYR]
    beam.loads = [-1.0e3, -1.0e3, -1.0e3]
    beam.solve()

    #plt.figure()
    #plt.plot(beam.y_displ)
    #plt.figure()
    #plt.plot(beam.NVM)
    #plt.show()
