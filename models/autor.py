from database import db


class Autor(db.Model):
    __tablename__ = "autores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(60))

    livros = db.relationship("Livro", back_populates="autor")

    def __repr__(self):
        return self.nome
