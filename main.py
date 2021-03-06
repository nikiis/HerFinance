from flask import Flask, render_template, url_for
import json
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resources")
def resources():
    with open('articles.json', mode="r") as f:
        info = json.load(f)

    with open('playlist.json', mode="r") as f:
        playlist = json.load(f)

    return render_template("resources.html", info=info, playlist=playlist)


@app.route("/faqs")
def faqs():
    return render_template("faqs.html")


@app.route("/forum")
def forum():
    return render_template("forum.html")


if __name__ == "__main__":
    # For deployment followed this guide:
    # https://stackabuse.com/deploying-a-flask-application-to-heroku/
    
    app.run(threaded=True, port=5000)
