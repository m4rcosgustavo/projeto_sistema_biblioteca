
from flask import render_template, request, redirect, url_for, flash

from controllers import leitores_bp
from database import db
from models import Leitor

from sqlalchemy.exc import IntegrityError


@leitores_bp.route("/")
def listar_leitores():

    leitores = Leitor.query.order_by(Leitor.nome).all()

    return render_template(
        "leitores/lista.html",
        leitores=leitores
    )


@leitores_bp.route("/novo", methods=["GET", "POST"])
def novo_leitor():

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()

        if not nome or not email:
            flash("Preencha nome e e-mail.", "erro")

            return render_template(
                "leitores/formulario.html",
                leitor=None
            )

        leitor = Leitor(
            nome=nome,
            email=email
        )

        db.session.add(leitor)

        try:
            db.session.commit()

        except IntegrityError:
            db.session.rollback()

            flash("Este e-mail já está cadastrado.", "erro")

            return render_template(
                "leitores/formulario.html",
                leitor=None
            )

        flash("Leitor cadastrado com sucesso!", "sucesso")

        return redirect(url_for("leitores.listar_leitores"))

    return render_template(
        "leitores/formulario.html",
        leitor=None
    )


@leitores_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_leitor(id):

    leitor = db.get_or_404(Leitor, id)

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()

        if not nome or not email:
            flash("Preencha nome e e-mail.", "erro")

            return render_template(
                "leitores/formulario.html",
                leitor=leitor
            )

        leitor.nome = nome
        leitor.email = email

        try:
            db.session.commit()

        except IntegrityError:
            db.session.rollback()

            flash("Este e-mail já está cadastrado por outro leitor.", "erro")

            return render_template(
                "leitores/formulario.html",
                leitor=leitor
            )

        flash("Leitor atualizado com sucesso!", "sucesso")

        return redirect(url_for("leitores.listar_leitores"))

    return render_template(
        "leitores/formulario.html",
        leitor=leitor
    )


@leitores_bp.route("/<int:id>/excluir", methods=["POST"])
def excluir_leitor(id):

    leitor = db.get_or_404(Leitor, id)

    if leitor.emprestimos:
        flash(
            "Não é possível excluir um leitor que possui empréstimos registrados.",
            "erro"
        )
    else:
        db.session.delete(leitor)
        db.session.commit()

        flash("Leitor excluído com sucesso!", "sucesso")

    return redirect(url_for("leitores.listar_leitores"))
