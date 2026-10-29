
from flask import render_template
from models import Autor
from controllers import autores_bp


@autores_bp.route("/", methods=["GET"])
def listar_autores():
    autores = Autor.query.order_by(Autor.nome).all()

    return render_template(
        "autores/lista.html",
        autores=autores
    )
