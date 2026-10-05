import sqlite3
from typing import (Callable, Any, List)

DB_FILENAME = "pole_chudes.db"

class Db():

    class Secret():
        word: str
        hint: str


    def __init__(self):
        self.__migrate()
        self.__seed()


    def add_secret(self, word: str, hint: str):
        self.__do_write_operation(lambda cursor:
            cursor.execute(
                'INSERT OR REPLACE INTO Secrets (word, hint) VALUES (?, ?)',
                (word, hint)
            )
        )


    def delete_secret(self, word: str):
        self.__do_write_operation(lambda cursor:
            cursor.execute(
                'DELETE FROM Secrets WHERE word = ?',
                (word, )
            )
        )


    def get_secrets_count(self) -> int:
        return self.__do_read_operation(lambda cursor:
            cursor.execute(
                'SELECT COUNT(*) FROM Secrets'
            )
            .fetchone()[0]
        )

    def get_random_secret(self) -> Secret|None:
        row = self.__do_read_operation(lambda cursor:
            cursor.execute(
                'SELECT * FROM Secrets ORDER BY RANDOM() LIMIT 1'
            )
            .fetchone()
        )
        if not row: return None
        result = self.Secret()
        result.word = row['word']
        result.hint = row['hint']
        return result


    def get_all_secrets(self) -> List[Secret]:
        rows = self.__do_read_operation(lambda cursor:
            cursor.execute(
                'SELECT * FROM Secrets'
            )
            .fetchall()
        )
        results = []
        if not rows or not len(rows): return results
        for row in rows:
            result = self.Secret()
            result.word = row['word']
            result.hint = row['hint']
            results.append(result)
        return results

    def __migrate(self):
        self.__do_write_operation(lambda cursor:
            # Создаем таблицу
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Secrets (
                    word TEXT PRIMARY KEY,
                    hint TEXT NOT NULL
                )
            ''')
        )


    def __seed(self):
        self.add_secret('жираф', 'Зверь с длинной шеей')
        self.add_secret('слон', 'Огромный зверь с длинным носом')
        self.add_secret('тигр', 'Полосатый хищник')



    def __do_write_operation(self, callback: Callable[[sqlite3.Cursor], sqlite3.Cursor]):
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect(DB_FILENAME)
        cursor = connection.cursor()
        callback(cursor)
        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()


    def __do_read_operation(self, callback: Callable[[sqlite3.Cursor], Any]) -> Any:
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect(DB_FILENAME)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = callback(cursor)
        # Сохраняем изменения и закрываем соединение
        connection.close()
        return result





