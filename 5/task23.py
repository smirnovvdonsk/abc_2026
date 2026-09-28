# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов


def get_html(body_content: str) -> str:
    return f"""
            <!DOCTYPE html>
            <html lang="ru">
                <head></head>
                <body>
                    {body_content}
                </body>
            </html>
        """


from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return get_html("""
        <ul>
            <li><a href="about"> О компании </a></li>
            <li><a href="contacts"> Контакты </a></li>
            <li><a href="posts"> Список постов </a></li>
        </ul>
    """)

@app.route("/about")
def about():
    return get_html("""
        <h2> О компании </h2>
        <p> ООО&nbsp;<q>Вектор</q> </p>
        <p> Горизонтальное&nbsp;бурение </p>
        <p> <a href="/"> &leftarrow;&nbsp;На&nbsp;главную </a> </p>
    """)

@app.route("/contacts")
def contacts():
    return get_html("""
        <h2> Контакты </h2>
        <p> <a href="tel:+79991234567">+7 (999) 123-45-67</a> </p>
        <p> <a href="mailto:mail@vector.ru">mail@vector.ru</a> </p>
        <p> <a href="/"> &leftarrow;&nbsp;На&nbsp;главную </a> </p>
    """)

@app.route("/posts")
def posts():
    return get_html("""
        <h2> Список постов </h2>
        <ul>
            <li><a href="posts/1"> Пост #1 </a></li>
            <li><a href="posts/2"> Пост #2 </a></li>
            <li><a href="posts/3"> Пост #3 </a></li>
        </ul>
        <p> <a href="/"> &leftarrow;&nbsp;На&nbsp;главную </a> </p>
    """)

@app.route("/posts/<int:post_id>")
def post(post_id):
    return get_html(f"""
        <h2> Пост №{post_id} </h2>
        <p>
           Некоторое содержимое поста №{post_id}...
        </p>
        <p> <a href="/posts"> &leftarrow;&nbsp;Назад к списку </a> </p>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)