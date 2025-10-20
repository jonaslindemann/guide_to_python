# -*- coding: utf-8 -*-
"""
Uppritningskontroll för balkmodell (QWidget)

Implementerar en QWidget för att rita en balkmodell. Klassen hanterar uppritning av balkar, stöd, laster, moment, förskjutningar och dimensioner. Klassen är avsedd att användas som en del av en PyQt-applikation för att visualisera en balkmodell.
"""

from qtpy.QtGui import QPainter, QColor
from qtpy.QtCore import Qt

from draw_widget import DrawWidget
from beam_model import BeamModel

import numpy as np


class BeamWidget(DrawWidget):
    def __init__(self, beam_model: BeamModel):
        """BeamWidget constructor"""
        super().__init__()

        self.beam_model = beam_model

        self.rel_support_size = 0.02
        self.rel_margin = 0.1
        self.rel_max_height = 0.1
        self.rel_dim_dist = 0.02

        self.__show_loads = True
        self.__show_displacement = True
        self.__show_moments = True
        self.__show_section_force = True
        self.__show_dimensions = True

        self.update_scale_factors()

    def update_scale_factors(self) -> None:
        y_max = self.beam_model.y_displ.max()
        y_min = self.beam_model.y_displ.min()

        self.max_abs_load = self.beam_model.max_abs_load
        self.y_max = self.beam_model.max_abs_y_displ
        self.max_V = self.beam_model.max_abs_V
        self.max_M = self.beam_model.max_abs_M

        self.set_world_bounds(
            -self.margin,
            -self.max_height * 0.5,
            self.total_length + 2 * self.margin,
            self.max_height,
        )

    def on_model_updated(self) -> None:
        self.update_scale_factors()
        self.update()

    def draw_beams(self) -> None:

        # Draw beam

        self.stroke_color = Qt.black
        self.fill_color = Qt.white
        self.stroke_width = 2.0

        for i, length in enumerate(self.beam_model.lengths):
            x0 = sum(self.beam_model.lengths[:i])
            x1 = x0 + length
            y0 = 0
            y1 = 0

            self.line(x0, y0, x1, y1)

    def draw_dimensions(self) -> None:

        # Draw dimensions
        self.stroke_color = Qt.black
        self.fill_color = Qt.black
        self.stroke_width = 1.0
        self.text_color = Qt.black

        y_start = -self.max_height - self.dim_dist
        y_end = -self.max_height * 2 - self.dim_dist
        y_dim_line = y_end + self.dim_dist

        for i, length in enumerate(self.beam_model.lengths):
            x = sum(self.beam_model.lengths[:i])
            y = 0

            self.line(x, y_start, x, y_end)
            self.arrow(
                x,
                y_dim_line,
                x + self.beam_model.lengths[i],
                y_dim_line,
                arrow_size=self.dim_dist * 0.5,
            )
            self.text(
                x + self.beam_model.lengths[i] / 2,
                y_dim_line + self.dim_dist * 0.5,
                f"{self.beam_model.lengths[i]:.2f}",
                font_size=self.dim_dist,
                hor_align="center",
                vert_align="bottom",
            )

        x += self.beam_model.lengths[-1]
        self.line(x, y_start, x, y_end)

    def draw_supports(self) -> None:

        # Draw supports
        self.stroke_color = Qt.black
        self.fill_color = Qt.white
        self.stroke_width = 2.0

        for i, support in enumerate(self.beam_model.supports):
            x = sum(self.beam_model.lengths[:i])
            y = 0

            if support == BeamModel.FIXED_XY:
                self.draw_support(x, y)
            elif support == BeamModel.FIXED_Y:
                self.draw_support(x, y, roller=True)
            elif support == BeamModel.FIXED_XYR:
                self.draw_support(x, y, fixed=True)

    def draw_loads(self) -> None:
        # Draw loads
        self.stroke_color = QColor(128, 50, 50)
        self.fill_color = QColor(128, 50, 50, 64)
        self.stroke_width = 2.0
        self.text_color = QColor(128, 50, 50)

        for i, load in enumerate(self.beam_model.loads):
            x = sum(self.beam_model.lengths[:i])
            y = 0

            q = load / self.beam_model.lengths[i]

            self.draw_load(
                x,
                self.beam_model.lengths[i],
                (load / self.max_abs_load) * self.max_height,
            )

            if load > 0:
                self.text(
                    x + self.beam_model.lengths[i] / 2,
                    (load / self.max_abs_load) * self.max_height + self.dim_dist,
                    f"q = {load:.0f} N/m",
                    font_size=self.dim_dist,
                    hor_align="center",
                    vert_align="bottom",
                )
            else:
                self.text(
                    x + self.beam_model.lengths[i] / 2,
                    (load / self.max_abs_load) * self.max_height,
                    f"q = {load:.0f} N/m",
                    font_size=self.dim_dist,
                    hor_align="center",
                    vert_align="top",
                )

    def draw_moments(self) :

        # Draw moments
        self.stroke_color = QColor(50, 128, 50)
        self.fill_color = QColor(50, 128, 50, 64)
        self.stroke_width = 2.0

        for i in range(len(self.beam_model.x) - 1):
            x0 = self.beam_model.x[i]
            x1 = self.beam_model.x[i + 1]
            y0 = self.max_height * self.beam_model.NVM[i, 1] / self.y_max
            y1 = self.max_height * self.beam_model.NVM[i + 1, 1] / self.y_max

            self.line(x0, y0, x1, y1)

    def on_draw(self) -> None:
        """Draw the widget"""

        if self.show_loads:
            self.draw_loads()
        if self.show_displacement:
            self.draw_displacement()
        if self.show_moments:
            self.draw_moments()
        if self.show_section_force:
            self.draw_section_force()

        self.draw_supports()
        self.draw_beams()

        if self.show_dimensions:
            self.draw_dimensions()

    def draw_support(self, x: float, y: float, roller: bool=False, fixed: bool=False) -> None:
        """Draw a support at position x, y with angle and radius"""

        if roller:
            self.circle(x, y - self.support_size * 0.5, self.support_size * 0.5)
            self.line(
                x - self.support_size,
                y - self.support_size,
                x + self.support_size,
                y - self.support_size,
            )
        else:
            if fixed:
                self.line(x, y - self.support_size, x, y + self.support_size)
            else:
                self.triangle(x, y, self.support_size, self.support_size)
                self.line(
                    x - self.support_size,
                    y - self.support_size,
                    x + self.support_size,
                    y - self.support_size,
                )

    def draw_load(self, x: float, w: float, h: float) -> None:
        """Draw a load at position x, y with angle and radius"""

        self.rect(x, 0, w, h)
        self.line(x + w / 2, h, x + w / 2, 0.0)

        if h > 0.0:
            self.line(
                x + w / 2,
                0.0,
                x + w / 2 - self.support_size * 0.5,
                self.support_size * 0.5,
            )
            self.line(
                x + w / 2,
                0.0,
                x + w / 2 + self.support_size * 0.5,
                self.support_size * 0.5,
            )
        else:
            self.line(
                x + w / 2,
                0.0,
                x + w / 2 - self.support_size * 0.5,
                -self.support_size * 0.5,
            )
            self.line(
                x + w / 2,
                0.0,
                x + w / 2 + self.support_size * 0.5,
                -self.support_size * 0.5,
            )

    def draw_displacement(self) -> None:
        # Draw displacements
        self.stroke_color = QColor(128, 50, 50)
        self.fill_color = QColor(128, 50, 50, 64)
        self.stroke_width = 2.0

        for i in range(len(self.beam_model.x) - 1):
            x0 = self.beam_model.x[i]
            x1 = self.beam_model.x[i + 1]
            y0 = self.max_height * self.beam_model.y_displ[i] / self.y_max
            y1 = self.max_height * self.beam_model.y_displ[i + 1] / self.y_max

            self.line(x0, y0, x1, y1)

    def draw_moments(self) -> None:

        # Draw moments
        self.stroke_color = QColor(50, 128, 50)
        self.fill_color = QColor(50, 128, 50, 64)
        self.stroke_width = 2.0

        points = (
            np.vstack(
                (
                    self.beam_model.x,
                    -self.max_height * self.beam_model.NVM[:, 2] / self.max_M,
                )
            ).T
        ).copy()
        points = np.vstack(
            (np.array([0.0, 0.0]), points, np.array([self.beam_model.x[-1], 0.0]))
        )

        self.polygon(points)

    def draw_section_force(self) -> None:

        # Draw moments
        self.stroke_color = QColor(50, 50, 128)
        self.fill_color = QColor(50, 50, 128, 64)
        self.stroke_width = 2.0

        points = (
            np.vstack(
                (
                    self.beam_model.x,
                    -self.max_height * self.beam_model.NVM[:, 1] / self.max_V,
                )
            ).T
        ).copy()
        points = np.vstack((points, np.array([self.beam_model.x[-1], 0.0])))
        points = np.vstack(
            (np.array([0.0, 0.0]), points, np.array([self.beam_model.x[-1], 0.0]))
        )

        self.polygon(points)

    @property
    def total_length(self):
        return self.beam_model.total_length

    @property
    def rel_support_size(self):
        return self.__rel_support_size

    @rel_support_size.setter
    def rel_support_size(self, size):
        self.__rel_support_size = size
        self.support_size = size * self.total_length

    @property
    def rel_margin(self):
        return self.__rel_margin

    @rel_margin.setter
    def rel_margin(self, margin):
        self.__rel_margin = margin
        self.margin = margin * self.total_length

    @property
    def rel_max_height(self):
        return self.__rel_max_height

    @rel_max_height.setter
    def rel_max_height(self, height):
        self.__rel_max_height = height
        self.max_height = height * self.total_length

    @property
    def rel_dim_dist(self):
        return self.__rel_dim_dist

    @rel_dim_dist.setter
    def rel_dim_dist(self, dist):
        self.__rel_dim_dist = dist
        self.dim_dist = dist * self.total_length

    @property
    def show_loads(self):
        return self.__show_loads

    @show_loads.setter
    def show_loads(self, show):
        self.__show_loads = show
        self.update()

    @property
    def show_displacement(self):
        return self.__show_displacement

    @show_displacement.setter
    def show_displacement(self, show):
        self.__show_displacement = show
        self.update()

    @property
    def show_moments(self):
        return self.__show_moments

    @show_moments.setter
    def show_moments(self, show):
        self.__show_moments = show
        self.update()

    @property
    def show_section_force(self):
        return self.__show_section_force

    @show_section_force.setter
    def show_section_force(self, show):
        self.__show_section_force = show
        self.update()

    @property
    def show_dimensions(self):
        return self.__show_dimensions

    @show_dimensions.setter
    def show_dimensions(self, show):
        self.__show_dimensions = show
        self.update()
