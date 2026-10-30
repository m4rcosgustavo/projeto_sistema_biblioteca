from flask import render_template

from controllers import emprestimos_bp
from models import Livro, Leitor


@emprestimos_bp.route("/novo")
def novo_emprestimo():

    livros = Livro.query.order_by(Livro.titulo).all()
    leitores = Leitor.query.order_by(Leitor.nome).all()

    return render_template(
        "emprestimos/formulario.html",
        livros=livros,
        leitores=leitores
    )
