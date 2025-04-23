<<<<<<< HEAD
import json
import os
from model.movieModel import MovieModel
from src.main import main


def GraphConstructor():
    # Caminho correto para o arquivo JSON
    json_file_path = os.path.join(os.path.dirname(__file__), 'latest_movies.json')

    # Abrindo o arquivo JSON
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Transformar em lista de MovieModel
    movies: list[MovieModel] = [MovieModel(**movie) for movie in data]

    # Exemplo: printar os títulos
    for movie in movies:
        print(movie.title)


if __name__ == "__main__":
    main()
=======
class MovieModel:
>>>>>>> 89c3c47994aab93d3644e6953f935942be77924a
