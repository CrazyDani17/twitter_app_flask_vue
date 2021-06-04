from flask import Flask
from flask import request
from flask import jsonify
import psycopg2
import hashlib
import json
from flask_cors import CORS, cross_origin


#-----------------------------------------------------------------------#
#Flask
#-----------------------------------------------------------------------#

#libraries: sudo pip3 install psycopg2-binary

app = Flask(__name__)
cors = CORS(app)

@app.route('/create_user', methods=['POST'])
@cross_origin() # new decorator
def create_user():
    print(request.json)
    params = {
        'user_name' : request.json['user_name'],
        'password' : request.json['password'],
        'nombre_completo' : request.json['nombre_completo'],
        'email' : request.json['email'],
        'tipo_de_usuario' : request.json['tipo_de_usuario']
    }
    query = """insert into users (user_name, password, nombre_completo, email, tipo_de_usuario) 
         values (%(user_name)s, %(password)s, %(nombre_completo)s, %(email)s, %(tipo_de_usuario)s) RETURNING user_id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {
        'user_id': id_of_new_row,
        'user_name': params['user_name'],
        'password': params['password'],
        'nombre_completo': params['nombre_completo'],
        'email': params['email'],
        'tipo_de_usuario': params['tipo_de_usuario']
    }
    return jsonify(content)

@app.route('/users', methods=['POST','GET'])
@cross_origin() # new decorator
def users():
    cursor.execute("SELECT * from users")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {
            'user_id': result[5], 
            'user_name': result[0],
            'password': result[1],
            'nombre_completo' : result[2],
            'email' : result[3],
            'tipo_de_usuario' : result[4],
        }

        data.append(content)
        content = {}
    return jsonify(data)


@app.route('/user/<id>', methods=['POST'])
@cross_origin() # new decorator
def user(id):
    cursor.execute("SELECT * from users where user_id="+id)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {
            'user_id': result[5], 
            'user_name': result[0], 
            'password': result[1],
            'nombre_completo' : result[2],
            'email' : result[3],
            'tipo_de_usuario' : result[4],
        }
        data.append(content)
        content = {}
    return jsonify(data)

@app.route('/update_user/<id>', methods=['POST'])
@cross_origin() # new decorator
def update_user(id):
    params = {
        'user_id' : id,
        'user_name' : request.json['user_name'],
        #'password' : hashlib.sha1(request.json['password']).hexdigest(),
        'password' : request.json['password'],
        'nombre_completo' : request.json['nombre_completo'],
        'email' : request.json['email'],
        'tipo_de_usuario' : request.json['tipo_de_usuario']
    }

    query = """UPDATE users SET user_name = %(user_name)s, password = %(password)s, nombre_completo = %(nombre_completo)s, email = %(email)s, tipo_de_usuario = %(tipo_de_usuario)s WHERE user_id = %(user_id)s"""
    cursor.execute(query, params)
    conn.commit()

    content = {
        'user_id': id,
        'user_name': params['user_name'],
        'password': params['password'],
        'nombre_completo': params['nombre_completo'],
        'email': params['email'],
        'tipo_de_usuario': params['tipo_de_usuario']
    }
    return jsonify(content)

@app.route('/delete_user/<id>', methods = ['POST'])
@cross_origin() # new decorator
def delete_user(id):
    cursor.execute('DELETE FROM users WHERE user_id = ' + id + '  RETURNING user_id' )                                      
    conn.commit()
    user_id = cursor.fetchone()
    if user_id:
        content = {
            'user_id': user_id[0],
            'eliminado' : "True",
        }
    else:
        content = {
            'user_id': id,
            'eliminado' : "False",
        }
    return jsonify(content)

@app.route('/create_tweet', methods=['POST'])
@cross_origin() # new decorator
def create_tweet():
    print(request.json)

    params = {
        'tweet' : request.json['tweet'],
        'puntaje' : request.json['puntaje'],
        'calificacion' : request.json['calificacion'],
        'twitter_username' : request.json['twitter_username'],
        'twitter_user_location' : request.json['twitter_user_location'],
        'hashtags' : request.json['hashtags'],
        'user_id' : request.json['user_id']

    }
    query = """insert into tweets (tweet, puntaje, calificacion, twitter_username,twitter_user_location,hashtags,user_id) 
         values (%(tweet)s, %(puntaje)s, %(calificacion)s, %(twitter_username)s, %(twitter_user_location)s
        , %(hashtags)s, %(user_id)s) RETURNING tweet_id"""
    cursor.execute(query, params)
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()

    content = {
        'twitter_id': id_of_new_row,
        'tweet': params['tweet'],
        'puntaje': params['puntaje'],
        'calificacion': params['calificacion'],
        'twitter_username': params['twitter_username'],
        'twitter_user_location': params['twitter_user_location'],
        'hashtags': params['hashtags'],
        'user_id': params['user_id']

    }
    return jsonify(content)

@app.route('/tweets', methods=['POST'])
@cross_origin() # new decorator
def tweets():
    cursor.execute("SELECT * from tweets")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {'tweet_id': result[0], 'tweet': result[1], 'puntaje': result[2],
                   'calificacion': result[3], 'twitter_username': result[4],
                   'twitter_user_location': result[5], 'hashtags': result[6],
                   'user_id': result[7]}
        data.append(content)
        content = {}
    return jsonify(data)

@app.route('/tweet/<id>', methods=['POST'])
@cross_origin() # new decorator
def tweet(id):
    cursor.execute("SELECT * from tweets where tweet_id="+id)
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {
            'tweet' : result[0],
            'puntaje' : result[1],
            'calificacion' : result[2],
            'twitter_username' : result[3],
            'twitter_user_location' : result[4],
            'hashtags' : result[5],
            'user_id' : result[6]

        }
        data.append(content)
        content = {}
    return jsonify(data)

@app.route('/update_tweet/<id>', methods=['POST'])
@cross_origin() # new decorator
def update_tweet(id):
    params = {
        'tweet_id' : id,
        'tweet' : request.json['tweet'],
        'puntaje' : request.json['puntaje'],
        'calificacion' : request.json['calificacion'],
        'twitter_username' : request.json['twitter_username'],
        'twitter_user_location' : request.json['twitter_user_location'],
        'hashtags' : request.json['hashtags'],
        'user_id': request.json['user_id']
    }

    query = """UPDATE tweets SET tweet = %(tweet)s, puntaje = %(puntaje)s, calificacion = %(calificacion)s, twitter_username = %(twitter_username)s, twitter_user_location = %(twitter_user_location)s, hashtags = %(hashtags)s, user_id = %(user_id)s WHERE tweet_id = %(tweet_id)s"""
    cursor.execute(query, params)
    conn.commit()

    content = {
        'twitter_id': id,
        'tweet': params['tweet'],
        'puntaje': params['puntaje'],
        'calificacion': params['calificacion'],
        'twitter_username': params['twitter_username'],
        'twitter_user_location': params['twitter_user_location'],
        'hashtags': params['hashtags'],
        'user_id': params['user_id']
    }
    return jsonify(content)

@app.route('/delete_tweet/<id>', methods = ['POST'])
@cross_origin() # new decorator
def delete_tweet(id):
    cursor.execute('DELETE FROM tweets WHERE tweet_id = ' + id + '  RETURNING tweet_id' )                                      
    conn.commit()
    tweet_id = cursor.fetchone()
    if tweet_id:
        content = {
            'tweet_id': tweet_id[0],
            'eliminado' : "True",
        }
    else:
        content = {
            'tweet_id': id,
            'eliminado' : "False",
        }
    return jsonify(content)


@app.route('/auditorias', methods=['POST'])
@cross_origin() # new decorator
def auditorias():
    cursor.execute("SELECT * from auditorias")
    #data = cursor.fetchone() # obtiene un registro
    rv = cursor.fetchall()

    data = []
    content = {}
    for result in rv:
        content = {
            'auditoria_id': result[0], 
            'user_id': result[1], 
            'fecha': result[2],
            'tweet_id' : result[3],
            'accion' : result[4],
        }

        data.append(content)
        content = {}
    return jsonify(data)

@app.route('/login', methods=['POST'])
@cross_origin() # new decorator
def login():

    print(request.json)

    params = {
        'user_name' : request.json['user_name'],
        'password' : request.json['password']
    }
    query = """SELECT user_id from users where user_name = %(user_name)s and password = %(password)s"""
    cursor.execute(query, params)
    user_id = cursor.fetchone()
    if user_id:
        content = {
            'user_id': user_id[0],
            'estado' : "True",
        }
    else:
        content = {
            'user_id': None,
            'estado' : "False",
        }

    return jsonify(content)

@app.route('/search_by_topic', methods=['POST'])
@cross_origin() # new decorator
def search_by_topic():

    print(request.json)

    params = {
        'topic' : request.json['topic'],
        'user_id' : request.json['user_id']
    }

    tweets_extraidos = []
    #content = {}
    for tweet in tweepy.Cursor(api.search, q=params['topic'], tweet_mode="extended").items(3):
        hashtag_text = ""
        hashtags = tweet._json['entities']['hashtags']
        for hashtag in hashtags:
            hashtag_text = hashtag_text + hashtag['text'] + ", "
        hashtag_text = hashtag_text[:-2]
        query_params = {
            "tweet" :  "{" + tweet._json['full_text'] + "}",
            "twitter_username" : "{" + tweet._json['user']['name'] + "}",
            "twitter_user_location" : "{" + tweet._json['user']['location'] + "}",
            "hashtags" : "{" + hashtag_text + "}",
            "user_id" : params['user_id'],
        }
        query = """insert into tweets (tweet, twitter_username, twitter_user_location,hashtags, user_id) 
         values (%(tweet)s, %(twitter_username)s, %(twitter_user_location)s
        , %(hashtags)s, %(user_id)s) RETURNING tweet_id"""
        cursor.execute(query, query_params)
        id_of_new_row = cursor.fetchone()[0]
        conn.commit()

        content = {
            'twitter_id': id_of_new_row,
            'tweet': query_params['tweet'],
            'twitter_username': query_params['twitter_username'],
            'twitter_user_location': query_params['twitter_user_location'],
            'hashtags': query_params['hashtags'],
            'user_id': query_params['user_id']

        }
        tweets_extraidos.append(content)

    return jsonify(tweets_extraidos)







if __name__ == "__main__":
    app.run(debug=True)