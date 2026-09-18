from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QLabel
)

from PySide6.QtCore import Qt


class Sidebar(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("sidebar")

        self.setFixedWidth(150)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            10, 20, 10, 20
        )

        layout.setSpacing(10)

        # =========================
        # TÍTULO
        # =========================

        title = QLabel("COBOT HMI")

        title.setObjectName("sidebarTitle")

        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        # =========================
        # BOTONES
        # =========================

        self.btn_chequeo = QPushButton(
            "Chequeo"
        )

        self.btn_pestana2 = QPushButton(
            "Pestaña 2"
        )

        self.btn_pestana3 = QPushButton(
            "Pestaña 3"
        )

        self.btn_configuracion = QPushButton(
            "Configuración"
        )

        self.buttons = [
            self.btn_chequeo,
            self.btn_pestana2,
            self.btn_pestana3,
            self.btn_configuracion
        ]

        for button in self.buttons:

            button.setFixedHeight(50)

            button.setStyleSheet("""
                QPushButton {
                    color: #d4d4d4;
                    background-color: transparent;

                    border: none;
                    border-radius: 5px;

                    text-align: left;

                    padding-left: 20px;

                    font-size: 15px;
                }

                QPushButton:hover {
                    background-color: #2a2d2e;
                    color: white;
                }

                QPushButton:pressed {
                    background-color: #37373d;
                }
            """)

            layout.addWidget(button)

        layout.addStretch()