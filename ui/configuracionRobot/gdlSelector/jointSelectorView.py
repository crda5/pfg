from PySide6.QtWidgets import QWidget


class JointSelectorView(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.jointMask = [
            False,
            False,
            False,
            False,
            False,
            False
        ]