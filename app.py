from flask import Flask, render_template

from database import db
from models import Autor, Livro, Leitor, Emprestimo

from controllers import (
    autores_bp,
    livros_bp,
    leitores_bp,
    emprestimos_bp
)

# Importa os controllers para registrar suas rotas
import controllers.autores
import controllers.livros
import controllers.leitores


def criar_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "biblioteca-chave-local"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///biblioteca.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(autores_bp)
    app.register_blueprint(livros_bp)
    app.register_blueprint(leitores_bp)
    app.register_blueprint(emprestimos_bp)

    @app.route("/")
    def inicio():
        return render_template("inicio.html")

    return app


app = criar_app()

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
