
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel
)
from gui.widgets.table import Table
from gui.buttons.stop_button import StopButton
from logic.game import Game
from typing import (Callable, Any)

class GameScreen(QWidget):

    __layout: QBoxLayout

    game: Game

    def __init__(self, parent: QWidget, game: Game, on_stop_click: Callable[..., Any]):
        super().__init__(parent)
        self.__on_stop_click = on_stop_click
        self.game = game
        self.__build_gui()
        self.refresh()


    def __build_gui(self):
        self.__layout = QVBoxLayout(self)
        self.setLayout(self.__layout)

        self.__hint_label = QLabel(self)

        self.__table = Table(self)

        input_region = QWidget(self)
        input_layout = QHBoxLayout(input_region)
        input_region.setLayout(input_layout)

        self.__input = QLineEdit(input_region)
        self.__input.setMaxLength(1)
        self.__input.returnPressed.connect(self.__on_letter_confirm_click)

        self.__confirm_button = QPushButton("Назвать букву", input_region)
        self.__confirm_button.clicked.connect(self.__on_letter_confirm_click)

        self.__result_label = QLabel(self)

        stop_button_region = QWidget(self)
        stop_button_layout = QHBoxLayout(stop_button_region)
        stop_button_region.setLayout(stop_button_layout)
        self.__stop_button = StopButton(self, self.__on_stop_click)
        stop_button_layout.addStretch()
        stop_button_layout.addWidget(self.__stop_button)



        input_layout.addStretch()
        input_layout.addWidget(self.__input)
        input_layout.addWidget(self.__confirm_button)
        input_layout.addStretch()
        
        # self.__layout.addStretch()
        self.__layout.addWidget(self.__hint_label)
        self.__layout.addWidget(self.__table)
        self.__layout.addWidget(input_region)
        self.__layout.addWidget(self.__result_label)
        self.__layout.addStretch()
        self.__layout.addWidget(stop_button_region)
        # self.__layout.addStretch()




    def __on_letter_confirm_click(self):
        self.game.commit_a_letter(self.__input.text())
        self.__input.clear()
        self.refresh()


    def refresh(self):
        self.__table.word = self.game.letters_to_show
        self.__hint_label.setText(self.game.hint)
        self.__result_label.setText(self.game.step_status)
        self.__input.setFocus()






    

    
        

