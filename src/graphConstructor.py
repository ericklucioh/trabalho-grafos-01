import json
import os
from models.graphModel import Graph
from models.nodeModel import NodeModel, NodeType
from utils.paths import getLastestMovies
from models.movieModel import MovieModel


def GraphConstructor():
    # Caminho correto para o arquivo JSON
    file_path = getLastestMovies()
    
    # Abrindo o arquivo JSON
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        movies: list[MovieModel] = json.load(file)  # Tipo inferido automaticamente
        
    build_graph_from_movies(movies)

def build_graph_from_movies(movies: list[MovieModel]) -> Graph:
    """Transforma uma lista de filmes (com atores) em um grafo."""
    graph = Graph()
    node_id_counter = 0
    actor_cache = {}  # Dicionário para armazenar atores já criados: {nome_ator: nó}

    for movie in movies:
        # Cria nó do filme
        movie_node = NodeModel(
            node_id=node_id_counter,
            node_type=NodeType.MOVIE,
            name=movie["title"]
        )
        node_id_counter += 1

        for actor_name in movie["cast"]:
            # Verifica no cache (O(1) por consulta)
            if actor_name not in actor_cache:
                actor_cache[actor_name] = NodeModel(
                    node_id=node_id_counter,
                    node_type=NodeType.ACTOR,
                    name=actor_name
                )
                node_id_counter += 1
            
            actor_node = actor_cache[actor_name]
            graph.add_edge(movie_node, actor_node)

    return graph