from database import db


class Leitor(db.Model):
    __tablename__ = "leitores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    emprestimos = db.relationship("Emprestimo", back_populates="leitor")