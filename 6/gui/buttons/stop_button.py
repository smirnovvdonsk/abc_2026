
from PyQt5.QtWidgets import (QPushButton, QWidget)
from typing import Callable

class StopButton(QPushButton):
     
    def __init__(
                self,
                parent: QWidget,
                on_click: Callable[..., None]
     ):
          super().__init__("Завершить", parent)
          self.clicked.connect(on_click)
