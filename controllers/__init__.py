from flask import Blueprint

autores_bp = Blueprint("autores", __name__, url_prefix="/autores")
livros_bp = Blueprint("livros", __name__, url_prefix="/livros")
leitores_bp = Blueprint("leitores", __name__, url_prefix="/leitores")
emprestimos_bp = Blueprint("emprestimos", __name__, url_prefix="/emprestimos")