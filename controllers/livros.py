from flask import render_template, request, redirect, url_for, flash

from controllers import livros_bp
from database import db
from models import Livro, Autor


@livros_bp.route("/")
def listar_livros():
    livros = Livro.query.order_by(Livro.titulo).all()

    return render_template(
        "livros/lista.html",
        livros=livros
    )


@livros_bp.route("/novo", methods=["GET", "POST"])
def novo_livro():

    autores = Autor.query.order_by(Autor.nome).all()

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor_id = request.form.get("autor_id", type=int)

        if not titulo or not autor_id or not db.session.get(Autor, autor_id):
            flash("Informe o título e selecione um autor válido.", "erro")

            return render_template(
                "livros/formulario.html",
                livro=None,
                autores=autores
            )

        ano = request.form.get("ano_publicacao", type=int)

        livro = Livro(
            titulo=titulo,
            genero=request.form.get("genero", "").strip() or None,
            ano_publicacao=ano,
            autor_id=autor_id
        )

        db.session.add(livro)
        db.session.commit()

        flash("Livro cadastrado com sucesso!", "sucesso")

        return redirect(url_for("livros.listar_livros"))

    return render_template(
        "livros/formulario.html",
        livro=None,
        autores=autores
    )


@livros_bp.route("/<int:id>/editar", methods=["GET", "POST"])
def editar_livro(id):

    livro = db.get_or_404(Livro, id)
    autores = Autor.query.order_by(Autor.nome).all()

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        autor_id = request.form.get("autor_id", type=int)

        if not titulo or not autor_id or not db.session.get(Autor, autor_id):
            flash("Informe o título e selecione um autor válido.", "erro")

            return render_template(
                "livros/formulario.html",
                livro=livro,
                autores=autores
            )

        livro.titulo = titulo
        livro.genero = request.form.get("genero", "").strip() or None
        livro.ano_publicacao = request.form.get("ano_publicacao", type=int)
        livro.autor_id = autor_id

        db.session.commit()

        flash("Livro atualizado com sucesso!", "sucesso")

        return redirect(url_for("livros.listar_livros"))

    return render_template(
        "livros/formulario.html",
        livro=livro,
        autores=autores
    )


@livros_bp.route("/<int:id>/excluir", methods=["POST"])
def excluir_livro(id):

    livro = db.get_or_404(Livro, id)

    if livro.emprestimos:
        flash(
            "Não é possível excluir um livro que possui empréstimos registrados.",
            "erro"
        )
    else:
        db.session.delete(livro)
        db.session.commit()

        flash("Livro excluído com sucesso!", "sucesso")

    return redirect(url_for("livros.listar_livros"))
