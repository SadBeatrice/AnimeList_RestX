import os
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

class server():
    def __init__(self, ):
        self.app = Flask(__name__)

        database_path = 'animelist.db'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.db = SQLAlchemy(self.app)

        self.create_database()

        self.api = Api(
            self.app,
            version='1.0',
            title='AnimeList API',
            description='API para gerenciar uma lista de animes assistidos',
            doc='/docs'
        )

    def create_database(self):
        # Cria o banco de dados, caso não exista
        with self.app.app_context():
            if not os.path.exists('animelist.db'):
                self.db.create_all()
                print("Banco de dados criado com sucesso!")
            else:
                print("Banco de dados já existe.")

    def run(self, ):
        self.app.run(debug=True)

server = server()
db = server.db