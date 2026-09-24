from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt

from ui.components.speedometer import Speedometer
from ui.components.realTimeChart import RealTimeChart


class JointDashboard(QWidget):

    def __init__(
        self,
        jointName="J1",
        parent=None
    ):
        super().__init__(parent)

        self.jointName = jointName

        self.setupUi()


    def setupUi(self):

        mainLayout = QVBoxLayout(self)

        mainLayout.setContentsMargins(
            10, 10, 10, 10
        )

        mainLayout.setSpacing(10)

        # Nombre de articulación
        self.title = QLabel(
            f"Articulación {self.jointName}"
        )

        self.title.setAlignment(
            Qt.AlignCenter
        )

        mainLayout.addWidget(
            self.title
        )

        grid = QGridLayout()

        grid.setSpacing(12)

        # ==================================
        # VELOCIDAD
        # ==================================

        speedPanel = self.createPanel(
            "Velocidad angular"
        )

        self.speedometer = Speedometer(
            minimum=0,
            maximum=180,
            unit="°/s"
        )

        speedPanel.layout().addWidget(
            self.speedometer
        )

        grid.addWidget(
            speedPanel,
            0,
            0
        )

        # ==================================
        # TORQUE
        # ==================================

        torquePanel = self.createPanel(
            "Torque"
        )

        self.lblTorque = QLabel(
            "0.00 Nm"
        )

        self.lblTorque.setAlignment(
            Qt.AlignCenter
        )

        torquePanel.layout().addWidget(
            self.lblTorque
        )

        grid.addWidget(
            torquePanel,
            0,
            1
        )

        # ==================================
        # CORRIENTE
        # ==================================

        currentPanel = self.createPanel(
            "Corriente"
        )

        self.currentChart = RealTimeChart(
            title="",
            unit="A"
        )

        currentPanel.layout().addWidget(
            self.currentChart
        )

        grid.addWidget(
            currentPanel,
            1,
            0
        )

        # ==================================
        # TEMPERATURA
        # ==================================

        temperaturePanel = self.createPanel(
            "Temperatura"
        )

        self.temperatureChart = RealTimeChart(
            title="",
            unit="°C"
        )

        temperaturePanel.layout().addWidget(
            self.temperatureChart
        )

        grid.addWidget(
            temperaturePanel,
            1,
            1
        )

        # ==================================
        # ÁNGULO
        # ==================================

        anglePanel = self.createPanel(
            "Ángulo"
        )

        self.lblAngle = QLabel(
            "0.0 °"
        )

        self.lblAngle.setAlignment(
            Qt.AlignCenter
        )

        anglePanel.layout().addWidget(
            self.lblAngle
        )

        grid.addWidget(
            anglePanel,
            2,
            0
        )

        # ==================================
        # VIBRACIÓN
        # ==================================

        vibrationPanel = self.createPanel(
            "Vibración"
        )

        self.vibrationChart = RealTimeChart(
            title="",
            unit="m/s²"
        )

        vibrationPanel.layout().addWidget(
            self.vibrationChart
        )

        grid.addWidget(
            vibrationPanel,
            2,
            1
        )

        # ==================================
        # ERROR DE POSICIÓN
        # ==================================

        errorPanel = self.createPanel(
            "Error de posición"
        )

        self.errorChart = RealTimeChart(
            title="",
            unit="°"
        )

        errorPanel.layout().addWidget(
            self.errorChart
        )

        grid.addWidget(
            errorPanel,
            3,
            0,
            1,
            2
        )

        mainLayout.addLayout(
            grid
        )

        # ==================================
        # DATOS SECUNDARIOS
        # ==================================

        self.lblCycles = QLabel(
            "Ciclos: 0"
        )

        self.lblTime = QLabel(
            "Tiempo de operación: 0.0 s"
        )

        mainLayout.addWidget(
            self.lblCycles
        )

        mainLayout.addWidget(
            self.lblTime
        )


    def createPanel(
        self,
        title
    ):

        panel = QFrame()

        panel.setObjectName(
            "variablePanel"
        )

        layout = QVBoxLayout(
            panel
        )

        label = QLabel(
            title
        )

        label.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            label
        )

        return panel


    def updateData(
        self,
        data
    ):

        self.speedometer.setValue(
            data["velocidad"]
        )

        self.lblTorque.setText(
            f"{data['torque']:.2f} Nm"
        )

        self.currentChart.addValue(
            data["corriente"]
        )

        self.temperatureChart.addValue(
            data["temperatura"]
        )

        self.lblAngle.setText(
            f"{data['angulo']:.1f} °"
        )

        self.vibrationChart.addValue(
            data["vibracion"]
        )

        self.errorChart.addValue(
            data["errorPosicion"]
        )

        self.lblCycles.setText(
            f"Ciclos: {data['ciclos']}"
        )

        self.lblTime.setText(
            f"Tiempo de operación: "
            f"{data['tiempoOperacion']:.1f} s"
        )