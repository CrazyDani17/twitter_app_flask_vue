from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from controladores.usuario_blueprint import user_blueprint
from controladores.tweet_blueprint import tweet_blueprint
from controladores.auditoria_blueprint import auditoria_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(tweet_blueprint)
app.register_blueprint(auditoria_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)