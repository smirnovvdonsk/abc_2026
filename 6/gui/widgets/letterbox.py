from PyQt5.QtWidgets import (QLineEdit, QWidget)
from PyQt5.QtCore import Qt

class LetterBox(QLineEdit):
    """ Поле одной буквы, разгаданной или неразгаданной """
    def __init__(self, parent: QWidget|None=None):
        super().__init__(parent)
        FONT_PIXEL_SIZE = 20
        LETTERBOX_PIXEL_SIZE = round(FONT_PIXEL_SIZE * 1.4)
        self.setMaxLength(1)
        font = self.font()
        font.setPixelSize(FONT_PIXEL_SIZE)
        self.setFixedWidth(LETTERBOX_PIXEL_SIZE)
        self.setFixedHeight(LETTERBOX_PIXEL_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setEnabled(False)

    @property
    def letter(self) -> str:
        return self.text()
    @letter.setter
    def letter(self, letter: str):
        self.setText(letter)