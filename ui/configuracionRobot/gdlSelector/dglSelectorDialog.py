from PySide6.QtWidgets import QDialog


class GdlSelectorDialog(QDialog):

    def __init__(
        self,
        gdlCount,
        parent=None
    ):
        super().__init__(parent)

        self.gdlCount = gdlCount

        self.setWindowTitle(
            "Selección de articulaciones"
        )

        self.resize(
            700,
            600
        )