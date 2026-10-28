
from flask import Flask
from database import db


def criar_app():
    app = Flask(__name__)

    # Configuração do banco SQLite
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicialização da conexão com o banco
    db.init_app(app)

    @app.route("/")
    def inicio():
        return "Sistema de Biblioteca funcionando!"

    return app


app = criar_app()


if __name__ == "__main__":
    app.run(debug=True)
