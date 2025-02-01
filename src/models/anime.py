from flask_restx import fields

from src.server.instance import server


# Definindo o modelo "Anime" para a API
anime_model = server.api.model('Anime', {
    'id': fields.String(required=True, description='O ID do registro.'),
    'title': fields.String(required=True, min_length=1, max_length=200, description='O título do anime.'),
    'nota': fields.Float(description='A nota dada ao anime.'),
    'comentario': fields.String(min_length=1, max_length=500, description='Um comentário sobre o anime (opcional).'),
    'status': fields.String(required=True, description='O status do anime (ex: "Assistido", "Assistindo", "Não assistido").')
})