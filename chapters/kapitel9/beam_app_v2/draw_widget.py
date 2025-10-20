# -*- coding: utf-8 -*-
"""
Abstrakt uppritnings kontroll för uppritning (QWidget)

Implementerar en abstrakt klass för att rita i en QWidget. Klassen hanterar uppritning i värd- och fönsterkoordinater samt skalning och centrering av innehållet. Metoder för att rita linjer, cirklar, rektanglar, polygoner och text finns implementerade.

Klassen är avsedd att användas som en bas för att skapa anpassade uppritningskontroller i PyQt-applikationer.
"""

from qtpy.QtWidgets import QWidget
from qtpy.QtGui import QPainter, QTransform, QPen, QBrush, QFont
from qtpy.QtCore import Qt, QPointF, QRectF


class DrawWidget(QWidget):
    def __init__(self):
        """DrawWidget konstruktor"""
        super().__init__()

        # Koordinatgränser
        self.world_bounds = QRectF(-10, -10, 20, 20)  # xmin, ymin, bredd, höjd
        self.__update_transform()

        self.__stroke_color = Qt.black
        self.__fill_color = Qt.white
        self.__stroke_width = 1.0
        self.__text_color = Qt.black
        self.__painter = None

        self.stroke_pen = QPen(self.__stroke_color, self.__stroke_width)
        self.fill_brush = QBrush(self.__fill_color)
        self.font = QFont()
        self.text_pen = QPen(self.__text_color)

    def update(self) -> None:
        """Uppdatera kontrollen"""
        self.__update_transform()
        self.__update_painter()

    def __update_transform(self) -> None:
        """Uppdatera transformationsmatrisen mellan världs- och fönsterkoordinater"""
        if not self.width() or not self.height():
            return

        # Skapa vyrektangel (i fönsterkoordinater)
        viewport = QRectF(0, 0, self.width(), self.height())

        # Beräkna transformationsmatrisen
        self.transform = QTransform()

        # Skala för att passa vyn samtidigt som aspektförhållandet bibehålls
        scale_x = viewport.width() / self.world_bounds.width()
        scale_y = viewport.height() / self.world_bounds.height()
        self.scale = min(scale_x, scale_y)

        # Centrera innehållet
        tx = viewport.width() / 2
        ty = viewport.height() / 2

        # Skapa transformationen: översätt till centrum, skala, vänd Y-axeln
        self.transform.translate(tx, ty)
        self.transform.scale(
            self.scale, -self.scale
        )  # Vänd Y-axeln för att matcha matematisk konvention
        self.transform.translate(
            -self.world_bounds.center().x(), -self.world_bounds.center().y()
        )

    def __update_painter(self) -> None:
        """Uppdatera pennor och penslar baserat på aktuella färger och storlekar"""

        self.stroke_pen.setColor(self.__stroke_color)
        self.stroke_pen.setWidth(int(self.__stroke_width))
        self.fill_brush.setColor(self.__fill_color)
        self.text_pen.setColor(self.__text_color)

        if self.__painter is None:
            return

        self.__painter.setRenderHints(
            QPainter.Antialiasing | QPainter.TextAntialiasing
        )
        self.__painter.setPen(self.stroke_pen)
        self.__painter.setBrush(self.fill_brush)

    def paintEvent(self, event) -> None:
        """Rita kontrollen"""

        super().paintEvent(event)
        
        self.painter.fillRect(0, 0, self.width(), self.height(), Qt.white)

        # Delegera uppritning till underklassen
        self.on_draw()

        self.painter.end()
        self.painter = None

    def on_draw(self) -> None:
        """Metod för att implementera uppritning i underklasser"""
        pass

    def resizeEvent(self, event) -> None:
        """Hantera storleksändringar av kontrollen"""
        super().resizeEvent(event)

        self.__update_transform()
        self.update()

    def set_world_bounds(self, xmin: float, ymin: float, width: float, height: float) -> None:
        """Uppdatera världskoordinater"""
        self.world_bounds = QRectF(xmin, ymin, width, height)
        self.__update_transform()

        self.update()

    def window_to_world(self, x: int, y: int) -> QPointF:
        """Konvertera fönsterkoordinater till världskoordinater"""
        return self.transform.inverted()[0].map(QPointF(x, y))

    def world_to_window(self, x: float, y: float) -> QPointF:
        """Konvertera världskoordinater till fönsterkoordinater"""
        return self.transform.map(QPointF(x, y))

    def polygon(self, points: list[tuple[float, float]]) -> None:
        """Rita en polygon med punkter"""
        mapped_points = [self.transform.map(QPointF(x, y)) for x, y in points]
        self.painter.drawPolygon(mapped_points)

    def line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Rita en linje"""
        p1 = self.transform.map(QPointF(x1, y1))
        p2 = self.transform.map(QPointF(x2, y2))
        self.painter.drawLine(p1, p2)

    def arrow(self, x1: float, y1: float, x2: float, y2: float, arrow_size: int=5, arrow_start: bool=True, arrow_end: bool=True) -> None:
        """Rita en pil"""
        p1 = self.transform.map(QPointF(x1, y1))
        p2 = self.transform.map(QPointF(x2, y2))
        self.painter.drawLine(p1, p2)

        dx = p2.x() - p1.x()
        dy = p2.y() - p1.y()
        length = (dx**2 + dy**2) ** 0.5
        if length == 0:
            return

        dx /= length
        dy /= length

        s_arrow_size = arrow_size * abs(self.scale)

        if arrow_end:
            p3 = QPointF(
                p2.x() - dx * s_arrow_size + dy * s_arrow_size / 2,
                p2.y() - dy * s_arrow_size - dx * s_arrow_size / 2,
            )
            p4 = QPointF(
                p2.x() - dx * s_arrow_size - dy * s_arrow_size / 2,
                p2.y() - dy * s_arrow_size + dx * s_arrow_size / 2,
            )
            self.painter.drawLine(p2, p3)
            self.painter.drawLine(p2, p4)

        if arrow_start:
            p5 = QPointF(
                p1.x() + dx * s_arrow_size + dy * s_arrow_size / 2,
                p1.y() + dy * s_arrow_size - dx * s_arrow_size / 2,
            )
            p6 = QPointF(
                p1.x() + dx * s_arrow_size - dy * s_arrow_size / 2,
                p1.y() + dy * s_arrow_size + dx * s_arrow_size / 2,
            )
            self.painter.drawLine(p1, p5)
            self.painter.drawLine(p1, p6)

    def rect(self, x: float, y: float, w: float, h: float) -> None:
        """Rita en rektangel"""
        p1 = self.transform.map(QPointF(x, y))
        p2 = self.transform.map(QPointF(x + w, y + h))
        self.painter.drawRect(QRectF(p1, p2))

    def circle(self, x: float, y: float, r: float) -> None:
        """Rita en cirkel"""
        p = self.transform.map(QPointF(x, y))
        screen_r = r * abs(self.scale)
        self.painter.drawEllipse(
            QRectF(p.x() - screen_r, p.y() - screen_r, 2 * screen_r, 2 * screen_r)
        )

    def triangle(self, x: float, y: float, w: float, h: float) -> None:
        """Rita en triangel"""
        p1 = self.transform.map(QPointF(x, y))
        p2 = self.transform.map(QPointF(x + w / 2, y - h))
        p3 = self.transform.map(QPointF(x - w / 2, y - h))
        self.painter.drawPolygon([p1, p2, p3])

    def text(self, x: float, y: float, text: str, font_size: int=12, hor_align: str="left", vert_align: str="middle"):
        """
        Rita text i världskoordinater med skärmpixelstorlek på fonten

        Parametrar:
            x, y: Världskoordinater för textposition
            text: Sträng att visa
            font_size: Storlek i skärmpixlar (standard: 12)
            hor_align: Horisontell justering - "left", "right" eller "center" (standard: "left")
            vert_align: Vertikal justering - "top", "middle" eller "bottom" (standard: "middle")
        """
        # Ställ in fonten
        font = self.painter.font()
        font.setPixelSize(int(font_size * abs(self.scale)))
        self.painter.setFont(font)

        # Hämta textmått för justering
        metrics = self.painter.fontMetrics()
        text_width = metrics.horizontalAdvance(text)
        text_height = metrics.height()

        # Transformera ankarpunkten från värld till skärmkoordinater
        p = self.transform.map(QPointF(x, y))

        # Justera x-position baserat på horisontell justering
        if hor_align == "right":
            p.setX(p.x() - text_width)
        elif hor_align == "center":
            p.setX(p.x() - text_width / 2)

        # Justera y-position baserat på vertikal justering
        if vert_align == "top":
            p.setY(p.y() + text_height)
        elif vert_align == "middle":
            p.setY(p.y() + text_height / 2)
        # För bottenjustering behövs ingen justering eftersom Qt ritar från botten

        self.painter.setPen(self.text_pen)
        self.painter.drawText(p, text)
        self.painter.setPen(self.stroke_pen)

    @property
    def painter(self) -> QPainter:
        """Returnera den aktuella QPainter-objektet för kontrollen"""

        if self.__painter is None:
            self.__painter = QPainter(self)

        self.__update_painter()

        return self.__painter
    
    @painter.setter
    def painter(self, painter):
        """Sätt en ny QPainter för kontrollen"""
        self.__painter = painter
        self.__update_painter()

    @property
    def stroke_color(self):
        return self.__stroke_color

    @stroke_color.setter
    def stroke_color(self, color):
        self.__stroke_color = color
        self.stroke_pen.setColor(color)

    @property
    def fill_color(self):
        return self.__fill_color

    @fill_color.setter
    def fill_color(self, color):
        self.__fill_color = color
        self.fill_brush.setColor(color)

    @property
    def stroke_width(self):
        return self.__stroke_width

    @stroke_width.setter
    def stroke_width(self, width):
        self.__stroke_width = width
        self.stroke_pen.setWidth(int(width))

    @property
    def text_color(self):
        return self.__font_color

    @text_color.setter
    def text_color(self, color):
        self.__font_color = color
        self.text_pen.setColor(color)
