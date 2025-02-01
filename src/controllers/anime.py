from flask_restx import Resource, fields
from src.server.instance import server
from src.models.anime import Anime

app, api, db = server.app, server.api, server.db

# Modelo para documentação no Swagger
anime_model  = api.model('Anime', {
    'id': fields.Integer(readOnly=True, description='ID gerado automaticamente.'),
    'title': fields.String(required=True, description='Título do anime.'),
    'nota': fields.Float(description='Nota do anime.'),
    'comentario': fields.String(description='Comentário sobre o anime.'),
    'status': fields.String(required=True, description='Status do anime (ex: Assistido, Assistindo).')
})


@api.route('/animelist')
class AnimeList(Resource):

    # Método GET para retornar a lista completa de animes.
    @api.marshal_list_with(anime_model)
    def get(self, ):
        return Anime.query.all()
    
    # Método POST para adicionar um anime na lista.
    @api.expect(anime_model , validate=True)
    @api.marshal_list_with(anime_model)
    def post(self):
        dados = api.payload
        novo_anime = Anime(
            title=dados['title'],
            nota=dados.get('nota'),
            comentario=dados.get('comentario'),
            status=dados['status']
        )
        db.session.add(novo_anime)
        db.session.commit()
        return novo_anime, 201


@api.route('/animelist/<int:id>')
class AnimeDetail(Resource):
    # Método GET para retornar um anime específico pelo ID.
    @api.marshal_with(anime_model)
    def get(self, id):   
        anime = Anime.query.get_or_404(id)
        return anime


    @api.expect(anime_model , validate=True)
    @api.marshal_with(anime_model)
    def put(self, id):
        # Método PUT para editar um anime existente pelo ID.
        anime = Anime.query.get_or_404(id)
        dados = api.payload
        anime.title = dados['title']
        anime.nota = dados.get('nota')
        anime.comentario = dados.get('comentario')
        anime.status = dados['status']
        db.session.commit()
        return anime

    def delete(self, id):
        # Deleta um anime da lista pelo ID.
        anime = Anime.query.get_or_404(id)
        db.session.delete(anime)
        db.session.commit()
        return '', 204


