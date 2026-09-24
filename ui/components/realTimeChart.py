from collections import deque

import pyqtgraph as pg

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt


class RealTimeChart(QWidget):

    def __init__(
        self,
        title,
        unit,
        maxPoints=100,
        parent=None
    ):
        super().__init__(parent)

        self.maxPoints = maxPoints

        self.xData = deque(
            maxlen=maxPoints
        )

        self.yData = deque(
            maxlen=maxPoints
        )

        self.counter = 0

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            5, 5, 5, 5
        )

        if title:

            titleLabel = QLabel(
                title
            )

            titleLabel.setAlignment(
                Qt.AlignCenter
            )

            layout.addWidget(
                titleLabel
            )

        self.graph = pg.PlotWidget()

        self.graph.setBackground(
            "w"
        )

        self.graph.showGrid(
            x=True,
            y=True,
            alpha=0.2
        )

        self.graph.setLabel(
            "left",
            unit
        )

        self.graph.setLabel(
            "bottom",
            "Muestras"
        )

        self.curve = self.graph.plot(
            [],
            []
        )

        layout.addWidget(
            self.graph
        )


    def addValue(
        self,
        value
    ):

        self.counter += 1

        self.xData.append(
            self.counter
        )

        self.yData.append(
            value
        )

        self.curve.setData(
            list(self.xData),
            list(self.yData)
        )