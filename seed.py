
from datetime import date

from app import app
from database import db
from models import Autor, Livro, Leitor, Emprestimo


def popular_banco():
    with app.app_context():

        # CADASTRAR AUTORES
        autores_iniciais = [
            ("Machado de Assis", "Brasileira"),
            ("Clarice Lispector", "Ucraniana"),
            ("Monteiro Lobato", "Brasileira"),
            ("José de Alencar", "Brasileira"),
            ("Graciliano Ramos", "Brasileira")
        ]

        for nome, nacionalidade in autores_iniciais:
            if not Autor.query.filter_by(nome=nome).first():
                db.session.add(
                    Autor(nome=nome, nacionalidade=nacionalidade)
                )

        db.session.flush()

        # CADASTRAR LIVROS
        livros_iniciais = [
            ("Dom Casmurro", "Romance", 1899, "Machado de Assis"),
            ("Memórias Póstumas de Brás Cubas", "Romance", 1881, "Machado de Assis"),
            ("A Hora da Estrela", "Romance", 1977, "Clarice Lispector"),
            ("Laços de Família", "Contos", 1960, "Clarice Lispector"),
            ("O Sítio do Picapau Amarelo", "Infantil", 1920, "Monteiro Lobato"),
            ("A Chave do Tamanho", "Infantil", 1942, "Monteiro Lobato"),
            ("Iracema", "Romance", 1865, "José de Alencar"),
            ("O Guarani", "Romance", 1857, "José de Alencar"),
            ("Vidas Secas", "Romance", 1938, "Graciliano Ramos"),
            ("São Bernardo", "Romance", 1934, "Graciliano Ramos")
        ]

        for titulo, genero, ano, nome_autor in livros_iniciais:
            if not Livro.query.filter_by(titulo=titulo).first():
                autor = Autor.query.filter_by(nome=nome_autor).first()

                db.session.add(
                    Livro(
                        titulo=titulo,
                        genero=genero,
                        ano_publicacao=ano,
                        autor_id=autor.id
                    )
                )

        db.session.flush()

        # CADASTRAR LEITORES
        leitores_iniciais = [
            ("Ana Silva", "ana@email.com"),
            ("Pedro Santos", "pedro@email.com"),
            ("Maria Oliveira", "maria@email.com"),
            ("João Costa", "joao@email.com"),
            ("Lucas Souza", "lucas@email.com")
        ]

        for nome, email in leitores_iniciais:
            if not Leitor.query.filter_by(email=email).first():
                db.session.add(
                    Leitor(nome=nome, email=email)
                )

        db.session.flush()

        # CADASTRAR EMPRÉSTIMOS
        emprestimos_iniciais = [
            ("ana@email.com", "Dom Casmurro", date(2026, 10, 20)),
            ("pedro@email.com", "A Hora da Estrela", date(2026, 10, 21)),
            ("maria@email.com", "O Sítio do Picapau Amarelo", date(2026, 10, 22)),
            ("joao@email.com", "Iracema", date(2026, 10, 23)),
            ("lucas@email.com", "Vidas Secas", date(2026, 10, 24)),
            ("ana@email.com", "Memórias Póstumas de Brás Cubas", date(2026, 10, 25))
        ]

        for email, titulo, data in emprestimos_iniciais:
            leitor = Leitor.query.filter_by(email=email).first()
            livro = Livro.query.filter_by(titulo=titulo).first()

            if leitor and livro:
                existente = Emprestimo.query.filter_by(
                    leitor_id=leitor.id,
                    livro_id=livro.id
                ).first()

                if not existente:
                    db.session.add(
                        Emprestimo(
                            leitor_id=leitor.id,
                            livro_id=livro.id,
                            data_emprestimo=data,
                            data_devolucao=None
                        )
                    )

        db.session.commit()

        print("\nBanco atualizado com sucesso!")
        print("Autores:", Autor.query.count())
        print("Livros:", Livro.query.count())
        print("Leitores:", Leitor.query.count())
        print("Empréstimos:", Emprestimo.query.count())


if __name__ == "__main__":
    popular_banco()
