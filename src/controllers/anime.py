from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.models.anime import anime_model

app, api = server.app, server.api

# Lista simulando o banco de dados
animes_db = [
    {
        'id': '0',
        'title': 'Sousou no Frieren',
        'nota': 9.5,
        'comentario': 'Definitivamente um dos meus favoritos, emocionante e fofo.',
        'status': 'Assistido'
    },
    {
        'id': '1',
        'title': 'Mahoutsukai no Yome',
        'nota': 8.5,
        'comentario': 'Calmo e fofo, gostei muito, há momentos que é lento até de mais.',
        'status': 'Assistido'
    }
]


@api.route('/animelist')
class AnimeList(Resource):

    # Método GET para retornar a lista completa de animes.
    @api.marshal_list_with(anime_model)
    def get(self, ):
        return animes_db
    
    # Método POST para adicionar um anime na lista.
    @api.expect(anime_model, validate=True)
    @api.marshal_list_with(anime_model)
    def post(self):
        novo_anime = api.payload
        animes_db.append(novo_anime)
        return novo_anime, 201



@api.route('/animelist/<string:id>')
class AnimeDetail(Resource):
    # Retorna um anime específico pelo ID.
    @api.marshal_with(anime_model)
    def get(self, id):   
        anime = next((anime for anime in animes_db if anime['id'] == id), None)
        if anime:
            return anime
        api.abort(404, f"Anime com ID {id} não encontrado.")

    @api.expect(anime_model, validate=True)
    @api.marshal_with(anime_model)
    def put(self, id):
        # Edita um anime existente pelo ID.
        anime = next((anime for anime in animes_db if anime['id'] == id), None)
        if not anime:
            api.abort(404, f"Anime com ID {id} não encontrado.")
        dados_atualizados = api.payload
        anime.update(dados_atualizados)
        return anime

    def delete(self, id):
        # Deleta um anime da lista pelo ID.
        anime = next((anime for anime in animes_db if anime['id'] == id), None)
        if not anime:
            api.abort(404, f"Anime com ID {id} não encontrado.")
        animes_db.remove(anime)
        return '', 204


