# Contextos

from flask import request, session, g
from flask import current_app, g
from flask_admin import Admin
from flask import Flask

app = Flask(__name__)

# 1 Configuração

# Add configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://.."

# Registrar Rotas


@app.route("/path")
def funcao():
    ...


app.add_url_rule("/path", callable)

# Inicializar extensoes

Admin.init_app(app)

# Registrar BLueprints
app.register_blueprints(...)

# add hooks


@app.before_request(...)
@app.error_handler(...)
# Chamar outras factories
#views.init_app(app)

# 2 App Context

# App está pronto! `app`

# Testar
# app.test_client
# debug
# objetos globais do Flask
# (importar request, session, g)
#- Hooks


# 3 Request Context
# usar globais do flask

request.args
request.form
