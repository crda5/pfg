from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
    QFrame
)

from PySide6.QtCore import Qt


class DiagnosticSwitch(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(
            10, 10, 10, 10
        )

        main_layout.setSpacing(15)

        # =========================
        # Selector
        # =========================

        switch_layout = QHBoxLayout()

        self.btn_variables = QPushButton(
            "Variables"
        )

        self.btn_resultados = QPushButton(
            "Resultados"
        )

        self.btn_variables.setCheckable(True)
        self.btn_resultados.setCheckable(True)

        self.btn_variables.setChecked(True)

        # Estilo temporal explícito
        button_style = """
            QPushButton {
                background-color: #eeeeee;
                color: #202124;

                border: 1px solid #bdbdbd;
                border-radius: 6px;

                padding: 8px 30px;

                font-family: Arial;
                font-size: 14px;
            }

            QPushButton:checked {
                background-color: #3c4043;
                color: white;
            }
        """

        self.btn_variables.setStyleSheet(
            button_style
        )

        self.btn_resultados.setStyleSheet(
            button_style
        )

        switch_layout.addStretch()

        switch_layout.addWidget(
            self.btn_variables
        )

        switch_layout.addWidget(
            self.btn_resultados
        )

        switch_layout.addStretch()

        main_layout.addLayout(
            switch_layout
        )

        # =========================
        # Páginas
        # =========================

        self.pages = QStackedWidget()

        self.variables_page = (
            self.create_variables_page()
        )

        self.results_page = (
            self.create_results_page()
        )

        self.pages.addWidget(
            self.variables_page
        )

        self.pages.addWidget(
            self.results_page
        )

        main_layout.addWidget(
            self.pages
        )

        # =========================
        # Conexiones
        # =========================

        self.btn_variables.clicked.connect(
            self.show_variables
        )

        self.btn_resultados.clicked.connect(
            self.show_results
        )


    # =========================================
    # Variables
    # =========================================

    def create_variables_page(self):

        page = QFrame()

        page.setStyleSheet("""
            QFrame {
                background-color: white;

                border: 1px solid #dddddd;
                border-radius: 8px;
            }

            QLabel {
                color: #202124;
                background-color: transparent;

                border: none;

                font-family: Arial;
                font-size: 14px;

                padding: 4px;
            }
        """)

        layout = QVBoxLayout(page)

        titulo = QLabel(
            "Variables del sistema"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(titulo)

        self.lbl_angulo = QLabel(
            "Ángulo: 0.0 °"
        )

        self.lbl_velocidad = QLabel(
            "Velocidad: 0.0 °/s"
        )

        self.lbl_corriente = QLabel(
            "Corriente: 0.00 A"
        )

        self.lbl_torque = QLabel(
            "Torque: 0.00 Nm"
        )

        self.lbl_temperatura = QLabel(
            "Temperatura: 0.0 °C"
        )

        self.lbl_material = QLabel(
            "Material: Aluminio 6061"
        )

        self.lbl_dureza = QLabel(
            "Dureza: 95 HB"
        )

        self.lbl_friccion = QLabel(
            "Coeficiente de fricción: --"
        )

        layout.addWidget(
            self.lbl_angulo
        )

        layout.addWidget(
            self.lbl_velocidad
        )

        layout.addWidget(
            self.lbl_corriente
        )

        layout.addWidget(
            self.lbl_torque
        )

        layout.addWidget(
            self.lbl_temperatura
        )

        layout.addWidget(
            self.lbl_material
        )

        layout.addWidget(
            self.lbl_dureza
        )

        layout.addWidget(
            self.lbl_friccion
        )

        layout.addStretch()

        return page


    # =========================================
    # Resultados
    # =========================================

    def create_results_page(self):

        page = QFrame()

        page.setStyleSheet("""
            QFrame {
                background-color: white;

                border: 1px solid #dddddd;
                border-radius: 8px;
            }

            QLabel {
                color: #202124;
                background-color: transparent;

                border: none;

                font-family: Arial;
                font-size: 14px;

                padding: 4px;
            }
        """)

        layout = QVBoxLayout(page)

        titulo = QLabel(
            "Resultados del modelo"
        )

        titulo.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(titulo)

        self.lbl_desgaste = QLabel(
            "Desgaste acumulado: 0.0000 mm³"
        )

        self.lbl_vida = QLabel(
            "Vida útil restante: 100.0 %"
        )

        self.lbl_profundidad = QLabel(
            "Profundidad de desgaste: -- mm"
        )

        self.lbl_masa_perdida = QLabel(
            "Masa perdida estimada: -- mg"
        )

        self.lbl_tasa_desgaste = QLabel(
            "Tasa de desgaste: --"
        )

        self.lbl_estado = QLabel(
            "Estado: --"
        )

        layout.addWidget(
            self.lbl_desgaste
        )

        layout.addWidget(
            self.lbl_profundidad
        )

        layout.addWidget(
            self.lbl_masa_perdida
        )

        layout.addWidget(
            self.lbl_tasa_desgaste
        )

        layout.addWidget(
            self.lbl_vida
        )

        layout.addWidget(
            self.lbl_estado
        )

        layout.addStretch()

        return page


    # =========================================
    # Actualizar valores
    # =========================================

    def update_data(self, data):

        self.lbl_angulo.setText(
            f"Ángulo: {data['angulo']:.1f} °"
        )

        self.lbl_velocidad.setText(
            f"Velocidad: {data['velocidad']:.1f} °/s"
        )

        self.lbl_corriente.setText(
            f"Corriente: {data['corriente']:.2f} A"
        )

        self.lbl_torque.setText(
            f"Torque: {data['torque']:.2f} Nm"
        )

        self.lbl_temperatura.setText(
            f"Temperatura: {data['temperatura']:.1f} °C"
        )

        self.lbl_desgaste.setText(
            f"Desgaste acumulado: "
            f"{data['desgaste']:.5f} mm³"
        )

        self.lbl_vida.setText(
            f"Vida útil restante: "
            f"{data['vida_util']:.2f} %"
        )

        # Estado provisional
        vida = data["vida_util"]

        if vida > 65:

            estado = "Normal"

        elif vida > 45:

            estado = "Precaución"

        elif vida > 25:

            estado = "Advertencia"

        else:

            estado = "Crítico"

        self.lbl_estado.setText(
            f"Estado: {estado}"
        )


    # =========================================
    # Cambio de sección
    # =========================================

    def show_variables(self):

        self.pages.setCurrentIndex(0)

        self.btn_variables.setChecked(True)

        self.btn_resultados.setChecked(False)


    def show_results(self):

        self.pages.setCurrentIndex(1)

        self.btn_variables.setChecked(False)

        self.btn_resultados.setChecked(True)