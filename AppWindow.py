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


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("HMI de Diagnóstico para Cobots")

        self.resize(1500,900)

        self.setup_ui()

    def setup_ui(self):

        # =========================
        # CONTENEDOR PRINCIPAL
        # =========================

        central_widget = QWidget()

        central_widget.setObjectName("centralContainer")

        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        main_layout.setContentsMargins(0, 0, 0, 0)

        main_layout.setSpacing(0)

        # =========================
        # MENÚ LATERAL
        # =========================

        self.sidebar = Sidebar()

        main_layout.addWidget(
        self.sidebar
        )

        # =========================
        # CONTENIDO DERECHO
        # =========================

        content_container = QWidget()

        content_layout = QVBoxLayout(
        content_container
        )

        content_layout.setContentsMargins(
        0, 0, 0, 0
        )

        content_layout.setSpacing(0)

        # =========================
        # ENCABEZADO SUPERIOR
        # =========================

        header = QWidget()

        header.setObjectName("header")

        header_layout = QVBoxLayout(header)

        header_layout.setContentsMargins(0, 12, 0, 8)

        self.screen_title = QLabel("Chequeo / Diagnóstico")

        self.screen_title.setObjectName("screenTitle")

        self.screen_title.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(self.screen_title)

        content_layout.addWidget(header)

        # =========================
        # PÁGINAS
        # =========================

        self.pages = QStackedWidget()

        self.pages.setObjectName("pages")

        self.chequeo_page = ChequeoWidget()

        self.pages.addWidget(self.chequeo_page)

        content_layout.addWidget(self.pages)

        main_layout.addWidget(content_container)