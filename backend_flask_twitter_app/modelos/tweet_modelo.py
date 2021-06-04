from conexion_base_de_datos.conexion import conn
from tweepy_api.tweepy_api import api
import tweepy

class TweetModel:
    def __init__(self):        
        self.cursor = conn.cursor()

    def search_tweet_by_topic(self, topic, user_id):
        params = {
            'topic' : topic,
            'user_id' : user_id
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
                "tweet" :  tweet._json['full_text'],
                "twitter_username" : tweet._json['user']['name'],
                "twitter_user_location" : tweet._json['user']['location'],
                "hashtags" : hashtag_text,
                "user_id" : params['user_id'],
            }
            query = """insert into tweets (tweet, twitter_username, twitter_user_location,hashtags, user_id) 
             values (%(tweet)s, %(twitter_username)s, %(twitter_user_location)s
            , %(hashtags)s, %(user_id)s) RETURNING tweet_id"""
            self.cursor.execute(query, query_params)
            id_of_new_row = self.cursor.fetchone()[0]
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

        return tweets_extraidos

    def get_tweet(self, id):
        params = {'id' : id}    
        self.cursor.execute("SELECT * from tweets where tweet_id=%(id)s", params)                
        rv = self.cursor.fetchall()
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
        return data

    def get_tweets(self):
        self.cursor.execute("SELECT * from tweets")  
        rv = self.cursor.fetchall()
        data = []
        content = {}
        for result in rv:
            content = {'tweet_id': result[0], 'tweet': result[1], 'puntaje': result[2],
                   'calificacion': result[3], 'twitter_username': result[4],
                   'twitter_user_location': result[5], 'hashtags': result[6],
                   'user_id': result[7]}
            data.append(content)
            content = {}
        return data

    def create_tweet(self, tweet, puntaje, calificacion, twitter_username, twitter_user_location, hashtags, user_id):
        params = {
            'tweet' : tweet,
            'puntaje' : puntaje,
            'calificacion' : calificacion,
            'twitter_username' : twitter_username,
            'twitter_user_location' : twitter_user_location,
            'hashtags' : hashtags,
            'user_id' : user_id

        }
        query = """insert into tweets (tweet, puntaje, calificacion, twitter_username,twitter_user_location,hashtags,user_id) 
         values (%(tweet)s, %(puntaje)s, %(calificacion)s, %(twitter_username)s, %(twitter_user_location)s
        , %(hashtags)s, %(user_id)s) RETURNING tweet_id"""    
        cursor = self.cursor.execute(query, params)
        id_of_new_row = self.cursor.fetchone()[0]
        conn.commit()  

        data = {
            'twitter_id': id_of_new_row,
            'tweet': params['tweet'],
            'puntaje': params['puntaje'],
            'calificacion': params['calificacion'],
            'twitter_username': params['twitter_username'],
            'twitter_user_location': params['twitter_user_location'],
            'hashtags': params['hashtags'],
            'user_id': params['user_id']

        }
        return data

    def delete_tweet(self, id):
        params = {'id' : id}      
        query = """delete from tweets where tweet_id = %(id)s RETURNING tweet_id"""    
        self.cursor.execute(query, params)
        conn.commit()

        tweet_id = self.cursor.fetchone()
        if tweet_id:
            data = {
                'tweet_id': tweet_id[0],
                'eliminado' : "True",
            }
        else:
            data = {
                'tweet_id': id,
                'eliminado' : "False",
            }
        return data

    def update_tweet(self, id, tweet, puntaje, calificacion, twitter_username, twitter_user_location, hashtags, user_id):
        params = {
            'tweet_id' : id,
            'tweet' : tweet,
            'puntaje' : puntaje,
            'calificacion' : calificacion,
            'twitter_username' : twitter_username,
            'twitter_user_location' : twitter_user_location,
            'hashtags' : hashtags,
            'user_id': user_id
        }
        query = """UPDATE tweets SET tweet = %(tweet)s, puntaje = %(puntaje)s, calificacion = %(calificacion)s, twitter_username = %(twitter_username)s, twitter_user_location = %(twitter_user_location)s, hashtags = %(hashtags)s, user_id = %(user_id)s WHERE tweet_id = %(tweet_id)s"""    
        cursor = self.cursor.execute(query, params)
        conn.commit()   

        data = {
            'twitter_id': id,
            'tweet': params['tweet'],
            'puntaje': params['puntaje'],
            'calificacion': params['calificacion'],
            'twitter_username': params['twitter_username'],
            'twitter_user_location': params['twitter_user_location'],
            'hashtags': params['hashtags'],
            'user_id': params['user_id']
        }
        return data

if __name__ == "__main__":    
    tm = TweetModel()