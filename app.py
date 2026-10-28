
from flask import Flask
from database import db
from models import Autor, Livro, Leitor, Emprestimo


def criar_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def inicio():
        return "Sistema de Biblioteca funcionando!"

    return app


app = criar_app()

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
