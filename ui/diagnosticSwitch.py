from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
    QFrame,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PySide6.QtCore import Qt

from ui.components.jointDashboard import JointDashboard


class DiagnosticSwitch(QWidget):

    def __init__(self):
        super().__init__()

        # Temporalmente usamos las 6.
        # Después esto vendrá del selector de GDL.
        self.activeJoints = [
            1, 2, 3, 4, 5, 6
        ]

        self.jointDashboards = {}

        self.setupUi()


    def setupUi(self):

        mainLayout = QVBoxLayout(self)

        mainLayout.setContentsMargins(
            10, 10, 10, 10
        )

        mainLayout.setSpacing(10)

        # ==================================
        # SELECTOR PRINCIPAL
        # ==================================

        switchLayout = QHBoxLayout()

        self.btnVariables = QPushButton(
            "Variables"
        )

        self.btnData = QPushButton(
            "Datos del sistema"
        )

        self.btnResults = QPushButton(
            "Resultados"
        )

        for button in [
            self.btnVariables,
            self.btnData,
            self.btnResults
        ]:
            button.setCheckable(True)

        self.btnVariables.setChecked(True)

        switchLayout.addStretch()

        switchLayout.addWidget(
            self.btnVariables
        )

        switchLayout.addWidget(
            self.btnData
        )

        switchLayout.addWidget(
            self.btnResults
        )

        switchLayout.addStretch()

        mainLayout.addLayout(
            switchLayout
        )

        # ==================================
        # PÁGINAS PRINCIPALES
        # ==================================

        self.pages = QStackedWidget()

        self.variablesPage = (
            self.createVariablesPage()
        )

        self.dataPage = (
            self.createDataPage()
        )

        self.resultsPage = (
            self.createResultsPage()
        )

        self.pages.addWidget(
            self.variablesPage
        )

        self.pages.addWidget(
            self.dataPage
        )

        self.pages.addWidget(
            self.resultsPage
        )

        mainLayout.addWidget(
            self.pages
        )

        # ==================================
        # CONEXIONES
        # ==================================

        self.btnVariables.clicked.connect(
            self.showVariables
        )

        self.btnData.clicked.connect(
            self.showData
        )

        self.btnResults.clicked.connect(
            self.showResults
        )


    # ======================================
    # VARIABLES
    # ======================================

    def createVariablesPage(self):

        page = QWidget()

        layout = QVBoxLayout(page)

        # Selector J1...J6
        jointSelectorLayout = QHBoxLayout()

        self.jointButtons = {}

        for joint in self.activeJoints:

            button = QPushButton(
                f"J{joint}"
            )

            button.setCheckable(True)

            if joint == self.activeJoints[0]:
                button.setChecked(True)

            button.clicked.connect(
                lambda checked,
                jointNumber=joint:
                self.showJoint(
                    jointNumber
                )
            )

            self.jointButtons[joint] = button

            jointSelectorLayout.addWidget(
                button
            )

        jointSelectorLayout.addStretch()

        layout.addLayout(
            jointSelectorLayout
        )

        # Paneles por articulación
        self.jointPages = QStackedWidget()

        for joint in self.activeJoints:

            dashboard = JointDashboard(
                jointName=f"J{joint}"
            )

            self.jointDashboards[joint] = (
                dashboard
            )

            self.jointPages.addWidget(
                dashboard
            )

        layout.addWidget(
            self.jointPages
        )

        return page


    # ======================================
    # DATOS DEL SISTEMA
    # ======================================

    def createDataPage(self):

        page = QFrame()

        layout = QVBoxLayout(page)

        title = QLabel(
            "Datos del sistema"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            title
        )

        self.dataTable = QTableWidget()

        self.dataTable.setColumnCount(4)

        self.dataTable.setHorizontalHeaderLabels([
            "Categoría",
            "Parámetro",
            "Valor",
            "Unidad"
        ])

        # Valores provisionales
        data = [
            (
                "Robot",
                "Grados de libertad",
                "6",
                "-"
            ),
            (
                "Robot",
                "Articulaciones activas",
                "J1, J2, J3, J4, J5, J6",
                "-"
            ),
            (
                "Motor",
                "Velocidad máxima",
                "180",
                "°/s"
            ),
            (
                "Material",
                "Material principal",
                "Aluminio",
                "-"
            )
        ]

        self.dataTable.setRowCount(
            len(data)
        )

        for row, values in enumerate(
            data
        ):

            for column, value in enumerate(
                values
            ):

                self.dataTable.setItem(
                    row,
                    column,
                    QTableWidgetItem(
                        str(value)
                    )
                )

        self.dataTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        layout.addWidget(
            self.dataTable
        )

        return page


    # ======================================
    # RESULTADOS
    # ======================================

    def createResultsPage(self):

        page = QFrame()

        layout = QVBoxLayout(page)

        title = QLabel(
            "Resultados del modelo"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            title
        )

        self.lblWear = QLabel(
            "Desgaste acumulado: --"
        )

        self.lblRemainingLife = QLabel(
            "Vida útil restante: --"
        )

        self.lblState = QLabel(
            "Estado: --"
        )

        layout.addWidget(
            self.lblWear
        )

        layout.addWidget(
            self.lblRemainingLife
        )

        layout.addWidget(
            self.lblState
        )

        layout.addStretch()

        return page


    # ======================================
    # CAMBIAR ARTICULACIÓN
    # ======================================

    def showJoint(
        self,
        jointNumber
    ):

        index = self.activeJoints.index(
            jointNumber
        )

        self.jointPages.setCurrentIndex(
            index
        )

        for joint, button in (
            self.jointButtons.items()
        ):

            button.setChecked(
                joint == jointNumber
            )


    # ======================================
    # ACTUALIZAR LOS 6 GDL
    # ======================================

    def updateData(
        self,
        data
    ):

        for joint in self.activeJoints:

            if joint in data:

                self.jointDashboards[
                    joint
                ].updateData(
                    data[joint]
                )


    # ======================================
    # SWITCH PRINCIPAL
    # ======================================

    def showVariables(self):

        self.pages.setCurrentIndex(0)

        self.btnVariables.setChecked(True)
        self.btnData.setChecked(False)
        self.btnResults.setChecked(False)


    def showData(self):

        self.pages.setCurrentIndex(1)

        self.btnVariables.setChecked(False)
        self.btnData.setChecked(True)
        self.btnResults.setChecked(False)


    def showResults(self):

        self.pages.setCurrentIndex(2)

        self.btnVariables.setChecked(False)
        self.btnData.setChecked(False)
        self.btnResults.setChecked(True)