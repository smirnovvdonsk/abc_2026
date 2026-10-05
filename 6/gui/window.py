from PyQt5.QtWidgets import (QMainWindow, QStackedWidget)
from gui.screens.hello_screen import HelloScreen
from gui.screens.game_screen import GameScreen
from gui.screens.edit_screen import EditScreen
from logic.game import Game
from logic.db import Db

INITIAL_WINDOW_SIZE = (600, 300)
WINDOW_TITLE = "Поле чудес"

class MainWindow(QMainWindow):
    
    game: Game
    db: Db

    def __init__(self):
        super().__init__()

        self.game = Game()
        self.db = Db()

        self.hello_screen = HelloScreen(self, self.start_game, self.start_editing)
        self.game_screen = GameScreen(self, self.game, self.show_hello)
        self.edit_screen = EditScreen(self, self.db, self.show_hello)

        self.stack = QStackedWidget(self)

        self.stack.addWidget(self.hello_screen) # index 0
        self.stack.addWidget(self.game_screen) # index 1
        self.stack.addWidget(self.edit_screen) # index 2

        self.setCentralWidget(self.stack)

        self.setWindowTitle(WINDOW_TITLE)
        self.resize(*INITIAL_WINDOW_SIZE)

        self.show_hello()
        
        

    def show_hello(self):
        words_count = self.db.get_secrets_count()
        self.hello_screen.set_can_play(bool(words_count))
        self.stack.setCurrentIndex(0)


    def start_game(self):
        task = self.db.get_random_secret()
        if not task: return
        self.game.word = task.word
        self.game.hint = task.hint
        self.game_screen.refresh()
        self.stack.setCurrentIndex(1)



    def start_editing(self):
       self.edit_screen.refresh()
       self.stack.setCurrentIndex(2)



