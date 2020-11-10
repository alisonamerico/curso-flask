from flask import Flask, request

"""
Obs.: 'import app' Nunca deve acontecer no projeto
 que não seja para teste, ou seja projeto real
 nunca de ter esse import para não ocorrer "circular import"

Ex: from app import app
"""

"""Extensão Flask"""


def init_app(app: Flask):
    """Inicialização de extensões"""

    @app.route("/")
    def index():
        print(request.args)
        return "Esta rodando aguarde"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"
