from typing import Set
from enum import Enum


class Game():

    class LetterGuessResult(Enum):
        LETTER_GUESSED = "LETTER_GUESSED"
        LETTER_GUESSED_AGAIN = "LETTER_GUESSED_AGAIN"
        LETTER_NOT_GUESSED = "LETTER_NOT_GUESSED"
        LETTER_NOT_GUESSED_AGAIN = "LETTER_NOT_GUESSED_AGAIN"

    class Status(Enum):
        IN_PROGRESS = "IN_PROGRESS"
        DONE = "DONE"

    __word: str
    __hint: str
    __step_status: str
    __mentioned_letters: Set[str]

    def __init__(self):
        self.__mentioned_letters = set()
        self.__step_status = ''
        self.word = ''
        self.hint = ''

    @property
    def word(self):
        return self.__word    
    @word.setter
    def word(self, word: str):
        self.__word = word.upper()
        self.__mentioned_letters.clear()
        self.__step_status = ''

    @property
    def hint(self):
        return self.__hint   
    @hint.setter
    def hint(self, hint: str):
        self.__hint = hint

    @property
    def mentioned_letters(self) -> list[str]:
        return list(self.__mentioned_letters)

    @property
    def guessed_letters(self) -> list[str]:
        result = []
        if not len(self.word): return result
        for l in self.mentioned_letters:
            if l in self.word: result.append(l)
        return result

    @property
    def status(self) -> Status:
        return self.Status.DONE if set(self.word) == set(self.guessed_letters) else self.Status.IN_PROGRESS

    @property
    def step_status(self) -> str:
        return self.__step_status  

    @property
    def letters_to_show(self) -> str:
        result = ''
        if not len(self.word): return result
        for l in self.word:
            result += (l if l in self.__mentioned_letters else ' ')
        return result

    def commit_a_letter(self, letter: str) -> LetterGuessResult:
        if not len(letter): return self.LetterGuessResult.LETTER_NOT_GUESSED
        l = letter[0].upper()
        is_already_mentioned = l in self.__mentioned_letters
        if not is_already_mentioned:
            self.__mentioned_letters.add(l)
        is_guessed = l in self.word
        if not is_guessed:
            result = self.LetterGuessResult.LETTER_NOT_GUESSED_AGAIN if is_already_mentioned else self.LetterGuessResult.LETTER_NOT_GUESSED
        else:
            result = self.LetterGuessResult.LETTER_GUESSED_AGAIN if is_already_mentioned else self.LetterGuessResult.LETTER_GUESSED
        if self.status == self.Status.DONE:
            self.__step_status = 'Слово разгадано полностью'
            return result
        match result:
            case self.LetterGuessResult.LETTER_GUESSED:
                self.__step_status = f'Да, в слове есть буква "{l}"'
            case self.LetterGuessResult.LETTER_GUESSED_AGAIN:
                self.__step_status = f'Да, в слове есть буква "{l}" и она уже была угадана ранее'
            case self.LetterGuessResult.LETTER_NOT_GUESSED:
                self.__step_status = f'Нет, в слове нет буквы "{l}"'
            case self.LetterGuessResult.LETTER_NOT_GUESSED_AGAIN:
                self.__step_status = f'Нет, в слове нет буквы "{l}" и она уже была названа ранее'
        return result

    