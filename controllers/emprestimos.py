
from flask import render_template

from controllers import emprestimos_bp
from models import Livro, Leitor, Emprestimo


@emprestimos_bp.route("/")
def listar_emprestimos():

    emprestimos = Emprestimo.query.order_by(
        Emprestimo.data_emprestimo.desc()
    ).all()

    return render_template(
        "emprestimos/lista.html",
        emprestimos=emprestimos
    )


@emprestimos_bp.route("/novo")
def novo_emprestimo():

    livros = Livro.query.order_by(Livro.titulo).all()
    leitores = Leitor.query.order_by(Leitor.nome).all()

    return render_template(
        "emprestimos/formulario.html",
        livros=livros,
        leitores=leitores
    )
