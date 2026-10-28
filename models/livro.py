from database import db


class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(60))
    ano_publicacao = db.Column(db.Integer)
    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)

    autor = db.relationship("Autor", back_populates="livros")
    emprestimos = db.relationship("Emprestimo", back_populates="livro")