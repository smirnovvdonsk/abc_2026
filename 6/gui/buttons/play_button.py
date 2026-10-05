
from PyQt5.QtWidgets import (QPushButton, QWidget)
from typing import Callable

class PlayButton(QPushButton):
     
    def __init__(
                self,
                parent: QWidget,
                on_click: Callable[..., None]
     ):
          super().__init__("Новая игра", parent)
          self.clicked.connect(on_click)


    
    @property
    def can_play(self) -> bool:
        return self.isEnabled()
    @can_play.setter
    def can_play(self, can_play: bool):
        self.setEnabled(can_play)
        self.setToolTip(None if can_play else "Невозможно играть, пока библиотека пуста")
        self.setToolTipDuration(200)