import tweepy
#-----------------------------------------------------------------------#
#Tweepy (Api de Twitter)
#-----------------------------------------------------------------------#

# 4 cadenas para la autenticacion de la API de Twitter
consumer_key = "fMxiRHszmWsJRPNHg4K1C9CDZ"
consumer_secret = "XFsLbGIWV0sQaV4eenZmZlKHppHdL7u5Mv6Eg1QF26KRISydBe"
access_token = "1280587737129721857-Se7AlxQeLhwTZiGvpkCZo4pNEdUCU8"
access_token_secret = "mD62z75oJfY9Yp6eqG7Gt8QC0TpGVU1nx3juBI4SoRjlf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)