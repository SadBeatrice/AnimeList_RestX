from src.server.instance import db

class Anime(db.Model):

    # Tabela da Lista de animes.
    __tablename__ = 'animes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    nota = db.Column(db.Float, nullable=True)
    comentario = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), nullable=False)

    # se chamar o anime retornará o título
    def __repr__(self):
        return f'<{self.title}>'