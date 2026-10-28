from database import db


class Emprestimo(db.Model):
    __tablename__ = "emprestimos"

    id = db.Column(db.Integer, primary_key=True)
    leitor_id = db.Column(db.Integer, db.ForeignKey("leitores.id"), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey("livros.id"), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date)

    leitor = db.relationship("Leitor", back_populates="emprestimos")
    livro = db.relationship("Livro", back_populates="emprestimos")
