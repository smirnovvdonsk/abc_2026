
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton, QLabel,
    QListWidget
)
from logic.db import Db

from typing import (List, Callable, Any)

from gui.buttons.stop_button import StopButton


class EditScreen(QWidget):

    __layout: QBoxLayout

    __secrets: List[Db.Secret]

    db: Db


    def __init__(self, parent: QWidget, db: Db, on_stop_click: Callable[..., Any]):
        super().__init__(parent)
        self.__on_stop_click = on_stop_click
        self.db = db
        self.__secrets = []
        self.__build_gui()
        self.refresh()


    def __build_gui(self):
        self.__layout = QVBoxLayout(self)
        self.setLayout(self.__layout)

        self.__list_widget = QListWidget()
        self.__list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.__list_widget.itemSelectionChanged.connect(self.__on_selection_changed)

        word_input_region = QWidget(self)
        word_input_layout = QHBoxLayout(word_input_region)
        word_input_region.setLayout(word_input_layout)
        self.__word_input = QLineEdit(word_input_region)
        self.__word_input.textChanged.connect(self.__on_input_text_changed)
        word_input_layout.addWidget(QLabel('Слово:', word_input_region))
        word_input_layout.addWidget(self.__word_input)
        
        hint_input_region = QWidget(self)
        hint_input_layout = QHBoxLayout(hint_input_region)
        hint_input_region.setLayout(hint_input_layout)
        self.__hint_input = QLineEdit(hint_input_region)
        self.__hint_input.textChanged.connect(self.__on_input_text_changed)
        hint_input_layout.addWidget(QLabel('Подсказка:', hint_input_region))
        hint_input_layout.addWidget(self.__hint_input)


        buttons_region = QWidget(self)
        buttons_layout = QHBoxLayout(buttons_region)
        buttons_region.setLayout(buttons_layout)
        self.__confirm_button = QPushButton("Добавить или изменить", buttons_region)
        self.__confirm_button.clicked.connect(self.__on_confirm_click)
        self.__delete_button = QPushButton("Удалить", buttons_region)
        self.__delete_button.clicked.connect(self.__on_delete_click)
        buttons_layout.addWidget(self.__confirm_button)
        buttons_layout.addWidget(self.__delete_button)


        stop_button_region = QWidget(self)
        stop_button_layout = QHBoxLayout(stop_button_region)
        stop_button_region.setLayout(stop_button_layout)
        self.__stop_button = StopButton(self, self.__on_stop_click)
        stop_button_layout.addStretch()
        stop_button_layout.addWidget(self.__stop_button)

        
        # self.__layout.addStretch()
        self.__layout.addWidget(self.__list_widget)
        # self.__layout.addStretch()
        self.__layout.addWidget(word_input_region)
        self.__layout.addWidget(hint_input_region)
        self.__layout.addWidget(buttons_region)
        self.__layout.addStretch()
        self.__layout.addWidget(stop_button_region)



    def __on_confirm_click(self):
        word = self.__word_input.text()
        hint = self.__hint_input.text()
        if not word or not hint: return
        self.db.add_secret(word, hint)
        self.refresh()


    def __on_delete_click(self):
        word = self.__word_input.text()
        if not word: return
        self.db.delete_secret(word)
        self.refresh()

    def __clear_inputs(self):
        self.__word_input.clear()
        self.__hint_input.clear()

    

    def refresh(self):
        self.__clear_inputs()
        self.__list_widget.clear()
        self.__secrets = self.db.get_all_secrets()
        for secret in self.__secrets:
            self.__list_widget.addItem(secret.word)
        self.__on_input_text_changed()

    def __on_selection_changed(self):
        selected = self.__list_widget.selectedItems()
        if selected:
            word = selected[0].text()
            if not word: return self.__clear_inputs()
            self.__word_input.setText(word)
            secret: Db.Secret|None = None
            for s in self.__secrets:
                if s.word == word: secret = s
            hint = secret.hint if secret else ''         
            self.__hint_input.setText(hint)
        else:
            self.__clear_inputs()


    def __on_input_text_changed(self):
        hasWord = bool(self.__word_input.text())
        hasHint = bool(self.__hint_input.text())
        self.__confirm_button.setEnabled(hasWord and hasHint)
        self.__delete_button.setEnabled(hasWord)








    

    
        

