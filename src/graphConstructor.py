import json
import os
from utils.paths import getLastestMovies
from models.movieModel import MovieModel


def GraphConstructor():
    # Caminho correto para o arquivo JSON
    file_path = getLastestMovies()

    print("test", file_path)
    
    # Abrindo o arquivo JSON
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Transformar em lista de MovieModel
    movies: list[MovieModel] = [MovieModel(**movie) for movie in data]

    # Exemplo: printar os títulos
    print(f"Projeto rodando...")
    for movie in movies:
        print(movie.title)

