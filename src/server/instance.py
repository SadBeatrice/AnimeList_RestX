from flask import Flask
from flask_restx import Api

class server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='AnimeList API',
            description='A simple API',
            doc='/docs'
        )

    def run(self, ):
        self.app.run(
            debug=True
        )

server = server()