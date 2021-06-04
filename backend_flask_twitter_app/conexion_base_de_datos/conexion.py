import psycopg2
conn = psycopg2.connect(
    host="127.0.0.1",
    database="twitter_app_db",
    user="postgres",
    password="admin123",
    port="8081")
