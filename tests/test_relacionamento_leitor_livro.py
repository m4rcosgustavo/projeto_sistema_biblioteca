
from datetime import date

from app import app
from database import db
from models import Autor, Livro, Leitor, Emprestimo


def test_leitor_pode_ter_varios_livros_e_livro_pode_ter_varios_leitores():
    with app.app_context():
        try:
            autor = Autor(
                nome="Autor do teste N:N",
                nacionalidade="Brasileira"
            )

            leitor1 = Leitor(
                nome="Leitor um do teste N:N",
                email="leitor1.teste.nn@example.com"
            )
            leitor2 = Leitor(
                nome="Leitor dois do teste N:N",
                email="leitor2.teste.nn@example.com"
            )

            livro1 = Livro(
                titulo="Livro um do teste N:N",
                genero="Teste",
                ano_publicacao=2025,
                autor=autor
            )
            livro2 = Livro(
                titulo="Livro dois do teste N:N",
                genero="Teste",
                ano_publicacao=2026,
                autor=autor
            )

            emprestimo1 = Emprestimo(
                leitor=leitor1,
                livro=livro1,
                data_emprestimo=date(2026, 10, 30)
            )
            emprestimo2 = Emprestimo(
                leitor=leitor1,
                livro=livro2,
                data_emprestimo=date(2026, 10, 30)
            )
            emprestimo3 = Emprestimo(
                leitor=leitor2,
                livro=livro1,
                data_emprestimo=date(2026, 10, 30)
            )

            db.session.add_all([
                autor, leitor1, leitor2,
                livro1, livro2,
                emprestimo1, emprestimo2, emprestimo3
            ])

            db.session.flush()

            # Um leitor pode pegar vários livros.
            assert len(leitor1.emprestimos) == 2

            # Um livro pode ser emprestado a leitores diferentes.
            assert len(livro1.emprestimos) == 2

            # Verifica as chaves estrangeiras.
            assert emprestimo1.leitor_id == leitor1.id
            assert emprestimo1.livro_id == livro1.id

            assert emprestimo2.leitor_id == leitor1.id
            assert emprestimo2.livro_id == livro2.id

            assert emprestimo3.leitor_id == leitor2.id
            assert emprestimo3.livro_id == livro1.id

        finally:
            db.session.rollback()
            db.session.remove()
