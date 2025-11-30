# -*- coding: utf-8 -*-
"""
Uppritningskontroll för värmeflödesmodell (QWidget)

Implementerar en QWidget för att rita en värmeflödesmodell. Klassen hanterar uppritning av materiallager, temperaturfördelning, värmeflöde och dimensioner. Klassen är avsedd att användas som en del av en PyQt-applikation för att visualisera en värmeflödesmodell.
"""

from qtpy.QtGui import QPainter, QColor
from qtpy.QtCore import Qt

from draw_widget import DrawWidget
from energy_model import HeatFlow1DModel

import numpy as np


class EnergyWidget(DrawWidget):
    def __init__(self, heat_model: HeatFlow1DModel):
        """EnergyWidget constructor"""
        super().__init__()

        self.heat_model = heat_model

        # Kom ihåg max thickness för skalning


        self.hatch_scale = 3.0

        self.rel_margin = 0.1
        self.rel_max_height = 0.8
        self.initial_height = self.heat_model.total_thickness * self.rel_max_height 
        self.rel_dim_dist = 0.05
        self.rel_layer_height = 0.05


        self.__show_temperature = True
        self.__show_heat_flux = True
        self.__show_dimensions = True

        self.__dark_mode = False

        self.update_scale_factors()

    def update_scale_factors(self) -> None:

        self.rel_max_height = 0.8


        if self.heat_model.temperatures is not None:
            self.T_max = self.heat_model.temperatures.max()
            self.T_min = self.heat_model.temperatures.min()
        else:
            self.T_max = 100.0
            self.T_min = 0.0

        if self.heat_model.heat_flux is not None:
            self.max_flux = np.abs(self.heat_model.heat_flux).max()
        else:
            self.max_flux = 1.0

        self.set_world_bounds(
            -self.margin,
            -(self.max_height*0.5)/2.0-self.margin-self.dim_dist*1.5,
            self.total_thickness + self.margin*2,
            self.max_height*0.5 + self.margin*2 + self.dim_dist*3,
        )

    def on_model_updated(self) -> None:
        self.update_scale_factors()
        self.update()

    def draw_layers(self) -> None:
        """Rita materiallager"""

        if self.dark_mode:
            self.stroke_color = QColor(150, 150, 150)  # Medium gray for hatch lines
            self.fill_color = QColor(50, 50, 50)  # Dark gray background
        else:
            self.stroke_color = Qt.black
            self.fill_color = QColor(220, 220, 220)

        self.stroke_width = 2.0


        x_pos = 0.0
        for i, layer in enumerate(self.heat_model.layers):
            # Rita lager som rektangel

            self.save_state()

            if layer.pattern == layer.BDiagPattern:
                self.fill_pattern = Qt.BDiagPattern
            elif layer.pattern == layer.FDiagPattern:
                self.fill_pattern = Qt.FDiagPattern
            elif layer.pattern == layer.DiagCrossPattern:
                self.fill_pattern = Qt.DiagCrossPattern
            elif layer.pattern == layer.HorPattern:
                self.fill_pattern = Qt.HorPattern
            elif layer.pattern == layer.VertPattern:
                self.fill_pattern = Qt.VerPattern
            elif layer.pattern == layer.CrossPattern:
                self.fill_pattern = Qt.CrossPattern
            else:
                self.fill_pattern = Qt.SolidPattern


            self.stroke_color = QColor(180, 180, 180) if self.dark_mode else Qt.black
            self.fill_color = QColor(80, 80, 80) if self.dark_mode else QColor(220, 220, 220)

            self.optional_rect(x_pos, -(self.max_height*0.5)/2.0, layer.thickness, self.max_height*0.5, True, True, False, False)

            self.restore_state()

            
            # Rita lagernummer
            if self.dark_mode:
                self.text_color = Qt.white
            else:
                self.text_color = Qt.black

            self.circle(x_pos + layer.thickness / 2, -self.s2wd(self.height()*0.01), self.s2wd(self.height()*0.02))
            
            self.text(
                x_pos + layer.thickness / 2,
                0,
                f"{i+1}",
                font_size=self.s2wd(self.height()*0.03),
                hor_align="center",
                vert_align="middle"
            )
            
            x_pos += layer.thickness

        #self.restore_state()

    def draw_dimensions(self) -> None:
        """Rita dimensioner för lager"""

        if self.dark_mode:
            self.stroke_color = Qt.white
            self.fill_color = Qt.white
            self.text_color = Qt.white
        else:
            self.stroke_color = Qt.black
            self.fill_color = Qt.black
            self.text_color = Qt.black

        self.stroke_width = 1.0

        y_start = -self.max_height*0.5/2 - self.s2wd(self.height()*0.02)
        y_end = -self.max_height*0.5/2 - self.s2wd(self.height()*0.1)
        y_dim_line = y_end + self.s2wd(self.height()*0.01)

        x_pos = 0.0
        for i, layer in enumerate(self.heat_model.layers):
            self.line(x_pos, y_start, x_pos, y_end)
            self.arrow(
                x_pos,
                y_dim_line,
                x_pos + layer.thickness,
                y_dim_line,
                arrow_size=self.s2wd(self.height()*0.02),
            )
            self.text(
                x_pos + layer.thickness / 2,
                y_dim_line + self.s2wd(self.height()*0.02),
                f"{layer.thickness:.3f} m",
                font_size=self.s2wd(self.height()*0.02),
                hor_align="center",
                vert_align="bottom",
            )
            
            x_pos += layer.thickness

        self.line(x_pos, y_start, x_pos, y_end)

    def draw_temperature(self) -> None:
        """Rita temperaturfördelning"""

        if self.heat_model.temperatures is None or self.heat_model.coords is None:
            return

        if self.dark_mode:
            self.stroke_color = QColor(255, 100, 100)
            self.fill_color = QColor(255, 100, 100, 128)
        else:
            self.stroke_color = QColor(200, 50, 50)
            self.fill_color = QColor(200, 50, 50, 64)

        self.stroke_width = 2.0

        # Rita temperaturkurva normaliserad till max_height
        T_range = self.T_max - self.T_min
        if T_range > 0:
            for i in range(len(self.heat_model.coords) - 1):
                x0 = self.heat_model.coords[i]
                x1 = self.heat_model.coords[i + 1]
                y0 = self.max_height * (self.heat_model.temperatures[i] - self.T_min) / T_range
                y1 = self.max_height * (self.heat_model.temperatures[i + 1] - self.T_min) / T_range

                self.line(x0, y0, x1, y1)

    def draw_heat_flux(self) -> None:
        """Rita värmeflöde"""

        if self.heat_model.heat_flux is None or self.heat_model.coords is None:
            return

        if self.dark_mode:
            self.stroke_color = QColor(50, 150, 255)
            self.fill_color = QColor(50, 150, 255, 128)
        else:
            self.stroke_color = QColor(50, 100, 200)
            self.fill_color = QColor(50, 100, 200, 64)

        self.stroke_width = 2.0

        # Rita värmeflöde som staplar
        if self.max_flux > 0:
            num_elements = len(self.heat_model.heat_flux)
            for i in range(num_elements):
                x0 = self.heat_model.coords[i]
                x1 = self.heat_model.coords[i + 1]
                y = -self.max_height * self.heat_model.heat_flux[i] / self.max_flux

                # Rita värmeflöde som rektangel
                self.rect(x0, 0, x1 - x0, y)

    def on_draw(self) -> None:
        """Draw the widget"""

        #if self.show_temperature:
        #    self.draw_temperature()
        #if self.show_heat_flux:
        #    self.draw_heat_flux()

        self.draw_layers()

        if self.show_dimensions:
            self.draw_dimensions()



    @property
    def total_thickness(self):
        return self.heat_model.total_thickness

    @property
    def rel_layer_height(self):
        return self.__rel_layer_height

    @rel_layer_height.setter
    def rel_layer_height(self, height):
        self.__rel_layer_height = height
        self.layer_height = height * self.total_thickness

    @property
    def rel_margin(self):
        return self.__rel_margin

    @rel_margin.setter
    def rel_margin(self, margin):
        self.__rel_margin = margin
        self.margin = margin * self.total_thickness

    @property
    def rel_max_height(self):
        return self.__rel_max_height

    @rel_max_height.setter
    def rel_max_height(self, height):
        self.__rel_max_height = height
        self.max_height = height * self.total_thickness

    @property
    def rel_dim_dist(self):
        return self.__rel_dim_dist

    @rel_dim_dist.setter
    def rel_dim_dist(self, dist):
        self.__rel_dim_dist = dist
        self.dim_dist = dist * self.max_height

    @property
    def show_temperature(self):
        return self.__show_temperature

    @show_temperature.setter
    def show_temperature(self, show):
        self.__show_temperature = show
        self.update()

    @property
    def show_heat_flux(self):
        return self.__show_heat_flux

    @show_heat_flux.setter
    def show_heat_flux(self, show):
        self.__show_heat_flux = show
        self.update()

    @property
    def show_dimensions(self):
        return self.__show_dimensions

    @show_dimensions.setter
    def show_dimensions(self, show):
        self.__show_dimensions = show
        self.update()

    @property
    def dark_mode(self):
        return self.__dark_mode
    
    @dark_mode.setter
    def dark_mode(self, dark: bool):
        self.__dark_mode = dark
        if dark:
            self.background_color = QColor(30, 30, 30)
            self.text_color = Qt.white
        else:
            self.background_color = Qt.white
            self.text_color = Qt.black
        self.update()
