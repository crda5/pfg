import math

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QPen,
    QColor,
    QFont
)
from PySide6.QtCore import (
    Qt,
    QPointF
)


class Speedometer(QWidget):

    def __init__(
        self,
        minimum=0,
        maximum=180,
        unit="°/s",
        parent=None
    ):
        super().__init__(parent)

        self.minimum = minimum
        self.maximum = maximum

        self.value = minimum

        self.unit = unit

        self.setMinimumSize(
            260,
            190
        )


    # ======================================
    # Actualizar velocidad
    # ======================================

    def setValue(self, value):

        self.value = max(
            self.minimum,
            min(value, self.maximum)
        )

        self.update()


    # ======================================
    # Dibujar velocímetro
    # ======================================

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        width = self.width()
        height = self.height()

        center = QPointF(
            width / 2,
            height * 0.72
        )

        radius = min(
            width * 0.38,
            height * 0.58
        )

        # ==============================
        # Arco exterior
        # ==============================

        pen = QPen(
            QColor("#404040")
        )

        pen.setWidth(8)

        pen.setCapStyle(
            Qt.RoundCap
        )

        painter.setPen(pen)

        rect = (
            center.x() - radius,
            center.y() - radius,
            radius * 2,
            radius * 2
        )

        painter.drawArc(
            int(rect[0]),
            int(rect[1]),
            int(rect[2]),
            int(rect[3]),
            0 * 16,
            180 * 16
        )

        # ==============================
        # Marcas
        # ==============================

        painter.setPen(
            QPen(
                QColor("#606060"),
                2
            )
        )

        divisions = 10

        for i in range(
            divisions + 1
        ):

            fraction = (
                i / divisions
            )

            angle = (
                math.pi
                -
                fraction * math.pi
            )

            outer = radius

            inner = radius - 14

            x1 = (
                center.x()
                +
                outer * math.cos(angle)
            )

            y1 = (
                center.y()
                -
                outer * math.sin(angle)
            )

            x2 = (
                center.x()
                +
                inner * math.cos(angle)
            )

            y2 = (
                center.y()
                -
                inner * math.sin(angle)
            )

            painter.drawLine(
                QPointF(x1, y1),
                QPointF(x2, y2)
            )

        # ==============================
        # Aguja
        # ==============================

        fraction = (
            self.value - self.minimum
        ) / (
            self.maximum
            - self.minimum
        )

        angle = (
            math.pi
            -
            fraction * math.pi
        )

        needle_length = (
            radius - 25
        )

        needle_x = (
            center.x()
            +
            needle_length
            * math.cos(angle)
        )

        needle_y = (
            center.y()
            -
            needle_length
            * math.sin(angle)
        )

        needle_pen = QPen(
            QColor("#d93025"),
            4
        )

        needle_pen.setCapStyle(
            Qt.RoundCap
        )

        painter.setPen(
            needle_pen
        )

        painter.drawLine(
            center,
            QPointF(
                needle_x,
                needle_y
            )
        )

        # Centro de la aguja
        painter.setBrush(
            QColor("#303030")
        )

        painter.setPen(
            Qt.NoPen
        )

        painter.drawEllipse(
            center,
            7,
            7
        )

        # ==============================
        # Valor
        # ==============================

        painter.setPen(
            QColor("#202124")
        )

        painter.setFont(
            QFont(
                "Arial",
                16,
                QFont.Bold
            )
        )

        painter.drawText(
            0,
            int(height * 0.72),
            width,
            35,
            Qt.AlignCenter,
            f"{self.value:.1f}"
        )

        # ==============================
        # Unidad
        # ==============================

        painter.setFont(
            QFont(
                "Arial",
                10
            )
        )

        painter.drawText(
            0,
            int(height * 0.84),
            width,
            25,
            Qt.AlignCenter,
            self.unit
        )