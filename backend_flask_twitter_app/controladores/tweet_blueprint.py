from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify

from flask_cors import CORS, cross_origin # para que no genere errores de CORS al hacer peticiones

from modelos.tweet_modelo import TweetModel

tweet_blueprint = Blueprint('tweet_blueprint', __name__)

model = TweetModel()

@tweet_blueprint.route('/create_tweet', methods=['POST'])
@cross_origin()
def create_tweet():
    content = model.create_tweet(
        request.json['tweet'],
        request.json['puntaje'],
        request.json['calificacion'],
        request.json['twitter_username'],
        request.json['twitter_user_location'],
        request.json['hashtags'],
        request.json['user_id'])
    return jsonify(content)
@tweet_blueprint.route('/update_tweet/<id>', methods=['POST'])
@cross_origin()
def update_tweet(id):
    content = model.update_tweet(id,
        request.json['tweet'],
        request.json['puntaje'],
        request.json['calificacion'],
        request.json['twitter_username'],
        request.json['twitter_user_location'],
        request.json['hashtags'],
        request.json['user_id'])
    return jsonify(content)

@tweet_blueprint.route('/delete_tweet/<id>', methods = ['POST'])
@cross_origin()
def delete_tweet(id):
    return jsonify(model.delete_tweet(int(id)))

@tweet_blueprint.route('/tweet/<id>', methods=['POST','GET'])
@cross_origin()
def tweet(id):
    return jsonify(model.get_tweet(int(id)))

@tweet_blueprint.route('/tweets', methods=['POST','GET'])
@cross_origin()
def tweets():
    return jsonify(model.get_tweets())

@tweet_blueprint.route('/search_by_topic', methods=['POST'])
@cross_origin() # new decorator
def search_by_topic():
    content = model.search_tweet_by_topic(
        request.json['topic'],
        int(request.json['user_id']))
    return jsonify(content)