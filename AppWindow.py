from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel
)

from PySide6.QtCore import Qt

from ui.sidebar import Sidebar
from ui.chequeo import ChequeoWidget
from ui.configuracionRobot.configuracionRobotPage import configuracionRobotPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "HMI de Diagnóstico para Cobots"
        )

        self.resize(
            1500,
            900
        )

        self.setupUi()
        self.connectNavigation()


    def setupUi(self):

        # =====================================
        # CONTENEDOR PRINCIPAL
        # =====================================

        centralWidget = QWidget()

        centralWidget.setObjectName(
            "centralContainer"
        )

        self.setCentralWidget(
            centralWidget
        )

        mainLayout = QHBoxLayout(
            centralWidget
        )

        mainLayout.setContentsMargins(
            0, 0, 0, 0
        )

        mainLayout.setSpacing(0)


        # =====================================
        # SIDEBAR IZQUIERDO
        # =====================================

        self.sidebar = Sidebar()

        mainLayout.addWidget(
            self.sidebar
        )


        # =====================================
        # ZONA DERECHA
        # =====================================

        contentContainer = QWidget()

        contentContainer.setObjectName(
            "contentContainer"
        )

        contentLayout = QVBoxLayout(
            contentContainer
        )

        contentLayout.setContentsMargins(
            0, 0, 0, 0
        )

        contentLayout.setSpacing(0)


        # =====================================
        # TÍTULO SUPERIOR
        # =====================================

        header = QWidget()

        header.setObjectName(
            "header"
        )

        headerLayout = QVBoxLayout(
            header
        )

        headerLayout.setContentsMargins(
            0, 12, 0, 8
        )

        self.screen_title = QLabel(
            "Chequeo / Diagnóstico"
        )

        self.screen_title.setObjectName(
            "screenTitle"
        )

        self.screen_title.setAlignment(
            Qt.AlignCenter
        )

        headerLayout.addWidget(
            self.screen_title
        )

        contentLayout.addWidget(
            header
        )


        # =====================================
        # PÁGINAS
        # =====================================

        self.pages = QStackedWidget()

        self.pages.setObjectName(
            "pages"
        )

        self.chequeoPage = ChequeoWidget()

        self.configuracionRobotPage = (
            configuracionRobotPage()
        )

        self.pages.addWidget(
            self.chequeoPage
        )

        self.pages.addWidget(
            self.configuracionRobotPage
        )

        self.pages.setCurrentIndex(0)

        contentLayout.addWidget(
            self.pages
        )


        # =====================================
        # IMPORTANTE:
        # AGREGAR LA ZONA DERECHA
        # =====================================

        mainLayout.addWidget(
            contentContainer
        )


    # =========================================
    # NAVEGACIÓN
    # =========================================

    def connectNavigation(self):

        self.sidebar.btn_chequeo.clicked.connect(
            lambda: self.changePage(
                0,
                "Chequeo / Diagnóstico"
            )
        )

        self.sidebar.btn_pestana2.clicked.connect(
            lambda: self.changePage(
                1,
                "Configuración del robot"
            )
        )


    def changePage(
        self,
        index,
        title
    ):

        self.pages.setCurrentIndex(
            index
        )

        self.screen_title.setText(
            title
        )