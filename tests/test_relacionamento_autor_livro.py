from app import app
from database import db
from models import Autor, Livro


def test_autor_pode_ter_varios_livros():
    with app.app_context():
        try:
            autor = Autor(
                nome="Autor de teste",
                nacionalidade="Brasileira"
            )

            livro1 = Livro(
                titulo="Livro um",
                genero="Teste",
                ano_publicacao=2025,
                autor=autor
            )

            livro2 = Livro(
                titulo="Livro dois",
                genero="Teste",
                ano_publicacao=2026,
                autor=autor
            )

            db.session.add_all([autor, livro1, livro2])
            db.session.flush()

            assert livro1.autor_id == autor.id
            assert livro2.autor_id == autor.id
            assert len(autor.livros) == 2

        finally:
            db.session.rollback()
            db.session.remove()