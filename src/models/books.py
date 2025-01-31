from flask_restx import fields

from src.server.instance import server


book = server.api.model('Book', {
    'id': fields.String(required=True, description='O ID do registro'),
    'title': fields.String(required=True, min_Length=1, max_Length=200, description='O título do livro')
})