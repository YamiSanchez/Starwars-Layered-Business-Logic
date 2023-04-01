import os
from flask import Flask
from services import star_wars_service

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)



@app.route("/", methods=['GET'])
def list_movies():
    movies = star_wars_service.list_movies()
    return jsonify(movies)

@app.route("/character", methods=['GET'])
def list_characters():
    movies = star_wars_service.characters_movies()
    return jsonify(movies)
   




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
