import requests

movie_url = "https://swapi.dev/api/films/"

def characters_movies():
    data = requests.get(movie_url).json()
    movies = []
    for movie in data["results"]:
        charactersURL=movie["characters"]

        characters = []
        for url in charactersURL:
            data = requests.get(url).json()
            characters.append(data["name"])

        movies.append({
            "name": movie["title"],
            "characters": characters
        })

    return movies

def list_movies():
    data = requests.get(movie_url).json()
    movies = []
    for movie in data["results"]:
        movies.append({
            "id": movie["episode_id"],
            "name": movie["title"]            
        })
    movies.sort(key=id)

    return movies