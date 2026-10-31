from app import app
from models import Livro, Leitor, Emprestimo

with app.app_context():
    print("LIVROS:", Livro.query.count())
    print("LEITORES:", Leitor.query.count())
    print("EMPRESTIMOS:", Emprestimo.query.count())
