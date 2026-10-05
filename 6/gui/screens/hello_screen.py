from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton
)
from typing import Callable

from gui.buttons.play_button import PlayButton

class HelloScreen(QWidget):

    __layout: QVBoxLayout
    
    def __init__(
            self,
            parent: QWidget,
            on_start_game_click: Callable[..., None],
            on_edit_library_click: Callable[..., None]
            ):
        super().__init__(parent)

        self.__layout = QVBoxLayout(self)

        self.__play_button = PlayButton(self, on_start_game_click)

        self.__edit_button = QPushButton("Править библиотеку")
        self.__edit_button.clicked.connect(on_edit_library_click)

        # self.__layout.setSpacing(10)
        self.__layout.addStretch()
        self.__layout.addWidget(self.__play_button)
        self.__layout.addStretch()
        self.__layout.addWidget(self.__edit_button)
        self.__layout.addStretch()


    def set_can_play(self, can_play: bool):
        self.__play_button.setDisabled(not can_play)
        self.__play_button.setToolTip(None if can_play else "Невозможно играть, пока библиотека пуста")
        self.__play_button.setToolTipDuration(200)







