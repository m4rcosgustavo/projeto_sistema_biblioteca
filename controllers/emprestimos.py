from datetime import date

from flask import render_template, request, redirect, url_for, flash

from controllers import emprestimos_bp
from database import db
from models import Livro, Leitor, Emprestimo


@emprestimos_bp.route("/")
def listar_emprestimos():

    livro_id = request.args.get("livro_id", type=int)
    leitor_id = request.args.get("leitor_id", type=int)

    consulta = Emprestimo.query

    if livro_id:
        consulta = consulta.filter_by(livro_id=livro_id)

    if leitor_id:
        consulta = consulta.filter_by(leitor_id=leitor_id)

    emprestimos = consulta.order_by(
        Emprestimo.data_emprestimo.desc()
    ).all()

    livros = Livro.query.order_by(Livro.titulo).all()
    leitores = Leitor.query.order_by(Leitor.nome).all()

    return render_template(
        "emprestimos/lista.html",
        emprestimos=emprestimos,
        livros=livros,
        leitores=leitores,
        livro_id=livro_id,
        leitor_id=leitor_id
    )


@emprestimos_bp.route("/novo", methods=["GET", "POST"])
def novo_emprestimo():

    livros = Livro.query.order_by(Livro.titulo).all()
    leitores = Leitor.query.order_by(Leitor.nome).all()

    if request.method == "POST":

        livro_id = request.form.get("livro_id", type=int)
        leitor_id = request.form.get("leitor_id", type=int)

        livro = db.session.get(Livro, livro_id) if livro_id else None
        leitor = db.session.get(Leitor, leitor_id) if leitor_id else None

        if not livro or not leitor:
            flash("Selecione um livro e um leitor válidos.", "erro")

            return render_template(
                "emprestimos/formulario.html",
                livros=livros,
                leitores=leitores
            )

        emprestimo_pendente = Emprestimo.query.filter_by(
            livro_id=livro_id,
            data_devolucao=None
        ).first()

        if emprestimo_pendente:
            flash("Este livro já possui um empréstimo pendente.", "erro")

            return render_template(
                "emprestimos/formulario.html",
                livros=livros,
                leitores=leitores
            )

        emprestimo = Emprestimo(
            leitor_id=leitor_id,
            livro_id=livro_id,
            data_emprestimo=date.today()
        )

        db.session.add(emprestimo)
        db.session.commit()

        flash("Empréstimo registrado com sucesso!", "sucesso")

        return redirect(url_for("emprestimos.listar_emprestimos"))

    return render_template(
        "emprestimos/formulario.html",
        livros=livros,
        leitores=leitores
    )

@emprestimos_bp.route("/<int:id>/devolver", methods=["POST"])
def devolver_emprestimo(id):
    emprestimo = db.get_or_404(Emprestimo, id)

    if emprestimo.data_devolucao:
        flash("Este livro já foi devolvido.", "erro")
    else:
        emprestimo.data_devolucao = date.today()
        db.session.commit()
        flash("Livro devolvido com sucesso!", "sucesso")

    return redirect(url_for("emprestimos.listar_emprestimos"))


@emprestimos_bp.route("/<int:id>/excluir", methods=["POST"])
def excluir_emprestimo(id):

    emprestimo = db.get_or_404(Emprestimo, id)

    db.session.delete(emprestimo)
    db.session.commit()

    flash("Empréstimo excluído com sucesso!", "sucesso")

    return redirect(url_for("emprestimos.listar_emprestimos"))