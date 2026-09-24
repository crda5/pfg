from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QHBoxLayout,
    QPushButton
)

from PySide6.QtCore import Qt


class configuracionRobotPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setupUi()


    def setupUi(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            40, 30, 40, 30
        )

        layout.setSpacing(20)

        # =========================
        # Selector de GDL
        # =========================

        selectorLayout = QHBoxLayout()

        label = QLabel(
            "Cantidad de GDL:"
        )

        self.gdlCombo = QComboBox()

        self.gdlCombo.addItems([
            "3",
            "4",
            "5",
            "6"
        ])

        self.btnSelectJoints = QPushButton(
            "Seleccionar articulaciones"
        )

        selectorLayout.addWidget(
            label
        )

        selectorLayout.addWidget(
            self.gdlCombo
        )

        selectorLayout.addWidget(
            self.btnSelectJoints
        )

        selectorLayout.addStretch()

        layout.addLayout(
            selectorLayout
        )

        # =========================
        # Texto de prueba
        # =========================

        self.selectionLabel = QLabel(
            "GDL seleccionados: 3"
        )

        self.selectionLabel.setAlignment(
            Qt.AlignLeft
        )

        layout.addWidget(
            self.selectionLabel
        )

        layout.addStretch()

        # =========================
        # Conexión de prueba
        # =========================

        self.gdlCombo.currentTextChanged.connect(
            self.updateSelection
        )


    def updateSelection(self, value):

        self.selectionLabel.setText(
            f"GDL seleccionados: {value}"
        )