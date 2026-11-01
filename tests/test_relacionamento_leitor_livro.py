from datetime import date
from uuid import uuid4

from app import app
from database import db
from models import Autor, Livro, Leitor, Emprestimo


def test_leitor_pode_ter_varios_livros_e_livro_pode_ter_varios_leitores():
    with app.app_context():
        try:
            identificador = uuid4().hex

            autor = Autor(
                nome=f"Autor do teste {identificador}",
                nacionalidade="Brasileira"
            )

            leitor1 = Leitor(
                nome="Leitor um do teste N:N",
                email=f"leitor1.{identificador}@example.com"
            )

            leitor2 = Leitor(
                nome="Leitor dois do teste N:N",
                email=f"leitor2.{identificador}@example.com"
            )

            livro1 = Livro(
                titulo=f"Livro um do teste {identificador}",
                genero="Teste",
                ano_publicacao=2025,
                autor=autor
            )

            livro2 = Livro(
                titulo=f"Livro dois do teste {identificador}",
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
                autor,
                leitor1,
                leitor2,
                livro1,
                livro2,
                emprestimo1,
                emprestimo2,
                emprestimo3
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

            # Guarda os IDs para consultar os registros.
            leitor_id = leitor1.id
            livro_id = livro1.id

            db.session.expire_all()

            leitor_salvo = db.session.get(Leitor, leitor_id)
            livro_salvo = db.session.get(Livro, livro_id)

            # Verifica se os registros continuam acessíveis.
            assert leitor_salvo is not None
            assert livro_salvo is not None

            # Verifica os relacionamentos após a consulta.
            assert len(leitor_salvo.emprestimos) == 2
            assert len(livro_salvo.emprestimos) == 2

        finally:
            # Desfaz as alterações feitas durante o teste.
            db.session.rollback()
            db.session.remove()