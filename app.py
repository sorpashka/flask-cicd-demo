from flask import Flask, jsonify

app = Flask(__name__)


def get_greeting(name: str = "студент") -> str:
    """Возвращает приветствие для указанного имени."""
    return f"Добро пожаловать, {name}!"


@app.route("/")
def index():
    return (
        "<h1>Учебное Flask-приложение</h1>"
        f"<p>{get_greeting()}</p>"
        "<p>Проект для СРОП по дисциплине «Прикладные аспекты DevOps».</p>"
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(debug=True)
