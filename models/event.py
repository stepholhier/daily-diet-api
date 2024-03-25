from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    esta_na_dieta = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Evento {self.nome}>'
