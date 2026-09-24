from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from PySide6.QtCore import QTimer

from ui.diagnosticSwitch import DiagnosticSwitch
from data.simulator import DataSimulator


class ChequeoWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20, 10, 20, 20
        )

        layout.setSpacing(10)

        self.diagnosticSwitch = (
            DiagnosticSwitch()
        )

        layout.addWidget(
            self.diagnosticSwitch
        )

        # Simulador
        self.simulator = DataSimulator()

        # Timer
        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.updateSimulation
        )

        # Primer valor inmediato
        self.updateSimulation()

        # 500 ms
        self.timer.start(
            500
        )


    def updateSimulation(self):

        data = self.simulator.update()

        self.diagnosticSwitch.updateData(
            data
        )