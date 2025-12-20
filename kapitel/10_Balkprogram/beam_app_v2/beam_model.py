# -*- coding: utf-8 -*-
"""
Balkmodell för att beräkna en kontinuerlig balk

Klassen implementerar en kontinuerlig balk som bestående av flera segment. Varje segment kan ha olika längd, antal element, last och material. Balken kan ha olika typer av upplag och laster. Klassen använder sig av Calfem för att beräkna balken.
"""

import logging
import json

import numpy as np
import calfem.core as cfc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BeamModel:
    """Balk klass för att beräkna en kontinuerlig balk"""

    FIXED_Y = 1
    FIXED_XY = 2
    FIXED_XYR = 3

    DEFAULT_E = 2.1e9
    DEFAULT_A = 0.1 * 0.1
    DEFAULT_I = 0.1 * (0.1**3) / 12

    VERSION = "2.0"

    def __init__(self):
        """Klasskonstruktor"""

        self.new()

    def new(self) -> None:
        """Initiera balkmodell"""

        self.def_props = [BeamModel.DEFAULT_E, BeamModel.DEFAULT_A, BeamModel.DEFAULT_I]

        self.lengths = [2.0, 2.0, 3.0]
        self.segments = [100, 100, 100]
        self.supports = [
            BeamModel.FIXED_XY,
            BeamModel.FIXED_Y,
            BeamModel.FIXED_Y,
            BeamModel.FIXED_Y,
        ]

        self.loads = [1.0e3, 1.0e3, 0.5e3]
        self.properties = [self.def_props, self.def_props, self.def_props]

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

        self.solve()

    def add_segment(self) -> None:
        """Lägg till ett segment"""

        self.lengths.append(self.lengths[-1])
        self.segments.append(self.segments[-1])
        self.loads.append(self.loads[-1])
        self.supports.append(BeamModel.FIXED_Y)
        self.properties.append(self.properties[-1])
        self.solve()

    def remove_segment(self) -> None:
        """Ta bort ett segment"""

        if len(self.lengths) > 1:
            self.lengths.pop()
            self.segments.pop()
            self.loads.pop()
            self.supports.pop()
            self.properties.pop()
            self.solve()

    def solve(self) -> None:
        """Löser ett system av kontinuerliga balkar"""

        # Kontrollera att vi har materialegenskaper. Om inte,
        # tilldela standardvärden.

        if self.properties == None:
            self.properties = []
            for i in enumerate(self.segments):
                self.properties.append(self.def_props)

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

        self.x = np.zeros((self.n_elements + 1), float)

        # Assemblera styvhetsmatrisen

        dof = 1  # Räknare för frihetsgrader
        el = 0  # Elementräknare
        self.support_dofs = []  # Randvillkor för varje upplag
        x = 0.0  # Aktuell x-koordinat för element

        for l, n, q, p in zip(self.lengths, self.segments, self.loads, self.properties):
            l_n = l / n
            self.support_dofs.append([dof, dof + 1, dof + 2])
            for i in range(n):

                # Tilldela elementkoordinater

                ex[el, :] = [x, x + l_n]
                ey[el, :] = [0.0, 0.0]
                ep[el, :] = p
                eq[el, :] = [0.0, -q]
                x += l_n

                # Beräkna element styvhet

                Ke, fe = cfc.beam2e(ex[el, :], ey[el, :], ep[el, :], eq[el, :])

                # Tilldela elementtopologi

                etopo = np.array([dof, dof + 1, dof + 2, dof + 3, dof + 4, dof + 5])
                dof += 3

                # Assemblera in element i global styvhetsmatris

                cfc.assem(etopo, K, Ke, f, fe)
                edof[el, :] = etopo
                el += 1

        # Lägg till randvillkor för sista upplaget

        self.support_dofs.append([dof, dof + 1, dof + 2])

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

        ed = cfc.extract_eldisp(edof, a)

        # Skapa matris för de inre krafterna

        self.NVM = np.zeros((self.y_displ.shape[0], 3), float)

        # Beräkna elementkrafter

        i = 0

        for el_displ, el_x, el_y, el_ep, el_eq in zip(ed, ex, ey, ep, eq):
            es = cfc.beam2s(el_x, el_y, el_ep, el_displ, el_eq)
            self.NVM[i, :] = es[0]
            self.x[i] = el_x[0]
            i += 1

        # Sista positionen måste också tilldelas

        self.NVM[i, :] = es[1]
        self.x[i] = el_x[1]

    def save_as_json(self, filename: str) -> None:
        """Save beam model as json file"""

        try: 
            beam_dict = {}
            beam_dict["lengths"] = self.lengths
            beam_dict["segments"] = self.segments
            beam_dict["loads"] = self.loads
            beam_dict["supports"] = self.supports
            beam_dict["properties"] = self.properties
            beam_dict["version"] = BeamModel.VERSION

            with open(filename, "w") as json_file:
                json.dump(beam_dict, json_file, sort_keys=True, indent=4)

        except (IOError, KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error saving beam model: {e}")

    def open_from_json(self, filename: str) -> None:
        """Load beam model from json file"""

        try:
            with open(filename, "r") as json_file:
                self.new()
                beam_dict = json.load(json_file)

                version = beam_dict.get("version", "1.0")
                
                if version == "1.0":
                    # Hantera äldre versioner om nödvändigt
                    logger.info("Loading beam model version 1.0")


                self.lengths = beam_dict["lengths"]
                self.segments = beam_dict["segments"]
                self.loads = beam_dict["loads"]
                self.supports = beam_dict["supports"]
                self.properties = beam_dict["properties"]
                self.solve()

        except (IOError, KeyError, json.JSONDecodeError) as e:
            logger.error(f"Error loading beam model: {e}")

    @property
    def total_length(self):
        """Return total length of beam"""

        return sum(self.lengths)

    @property
    def max_load(self):
        """Return maximum load"""

        return np.max(self.loads)

    @property
    def min_load(self):
        """Return minimum load"""

        return np.min(self.loads)

    @property
    def max_abs_load(self):
        """Return maximum absolute load"""

        return np.max(np.abs(self.loads))

    @property
    def max_y_displ(self):
        """Return maximum y displacement"""

        return np.max(self.y_displ)

    @property
    def min_y_displ(self):
        """Return minimum y displacement"""

        return np.min(self.y_displ)

    @property
    def max_abs_y_displ(self):
        """Return maximum absolute y displacement"""

        return np.max(np.abs(self.y_displ))

    @property
    def max_abs_M(self):
        """Return maximum absolute moment"""

        return np.max(np.abs(self.NVM[:, 2]))

    @property
    def max_abs_V(self):
        """Return maximum absolute shear force"""

        return np.max(np.abs(self.NVM[:, 1]))


if __name__ == "__main__":

    beam = BeamModel()
    beam.solve()
