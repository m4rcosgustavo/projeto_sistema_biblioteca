from flask import render_template, request, redirect, url_for, flash

from models import Autor
from controllers import autores_bp
from database import db


@autores_bp.route("/")
def listar_autores():
    autores = Autor.query.order_by(Autor.nome).all()

    return render_template(
        "autores/lista.html",
        autores=autores
    )


@autores_bp.route("/novo", methods=["GET", "POST"])
def novo_autor():

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        nacionalidade = request.form.get("nacionalidade", "").strip()

        if not nome:
            flash("Informe o nome do autor.", "erro")
            return render_template(
                "autores/formulario.html",
                autor=None
            )

        autor = Autor(
            nome=nome,
            nacionalidade=nacionalidade or None
        )

        db.session.add(autor)
        db.session.commit()

        flash("Autor cadastrado com sucesso!", "sucesso")

        return redirect(url_for("autores.listar_autores"))

    return render_template(
        "autores/formulario.html",
        autor=None
    )


@autores_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_autor(id):

    autor = db.get_or_404(Autor, id)

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()

        if not nome:
            flash("Informe o nome do autor.", "erro")
            return render_template(
                "autores/formulario.html",
                autor=autor
            )

        autor.nome = nome
        autor.nacionalidade = (
            request.form.get("nacionalidade", "").strip() or None
        )

        db.session.commit()

        flash("Autor atualizado com sucesso!", "sucesso")

        return redirect(url_for("autores.listar_autores"))

    return render_template(
        "autores/formulario.html",
        autor=autor
    )


@autores_bp.route("/<int:id>/excluir", methods=["POST"])
def excluir_autor(id):

    autor = db.get_or_404(Autor, id)

    if autor.livros:
        flash(
            "Não é possível excluir um autor que possui livros cadastrados.",
            "erro"
        )
    else:
        db.session.delete(autor)
        db.session.commit()

        flash("Autor excluído com sucesso!", "sucesso")

    return redirect(url_for("autores.listar_autores"))
