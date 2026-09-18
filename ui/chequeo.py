from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt, QTimer

from ui.diagnosticSwitch import DiagnosticSwitch
from data.simulator import DataSimulator


class ChequeoWidget(QWidget):

    def __init__(self):
        super().__init__()

        # Fondo blanco explícito
        self.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
            }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            20, 10, 20, 20
        )

        layout.setSpacing(10)

       
        # Panel Variables / Resultados
        self.diagnostic_switch = DiagnosticSwitch()

        layout.addWidget(
            self.diagnostic_switch
        )

        # Simulador
        self.simulator = DataSimulator()

        # Timer
        self.timer = QTimer(self)

        self.timer.timeout.connect(
            self.update_simulation
        )

        # Ejecutamos una vez inmediatamente
        self.update_simulation()

        # Después actualizamos cada 500 ms
        self.timer.start(500)


    def update_simulation(self):

        data = self.simulator.update()

        self.diagnostic_switch.update_data(
            data
        )