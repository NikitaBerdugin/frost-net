from flask import Flask
from regist import regi
from im import im
from test import test
from community import community
from friends import friends
from news import news
from photos import photos
from posts import posts
from start import start


app = Flask(__name__)

start()

regi()

im()

test()

community()

friends()

news()

photos()

posts()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)