from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QBoxLayout)

from gui.widgets.letterbox import LetterBox

from typing import List

class Table(QWidget):
    """ Набор из полей букв, разгаданных или неразгаданных """
    __word = ''
    __layout: QBoxLayout
    __letterboxes: List[LetterBox] = []
    
    
    def __init__(self, parent: QWidget|None):
        super().__init__(parent)
        self.__letterboxes = []
        self.__layout = QHBoxLayout(self)
        self.__layout.setSpacing(2)



    @property
    def word(self) -> str:
        return self.__word
    
    @word.setter
    def word(self, word: str):
        self.__word = word
        self.clear()
        layout = self.__layout
        layout.addStretch()
        for letter in word:
            letterbox = LetterBox()
            self.__letterboxes.append(letterbox)
            letterbox.letter = letter
            layout.addWidget(letterbox)
        layout.addStretch()
        


    def clear(self):
        layout = self.__layout
        for letterbox in self.__letterboxes:
            layout.removeWidget(letterbox)
            letterbox.setParent(None)
            letterbox.deleteLater()
        self.__letterboxes.clear()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if not widget: 
                layout.removeItem(item) # Уничтожает пружины (QSpacerItem)
