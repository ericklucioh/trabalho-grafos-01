
from .nodeModel import NodeModel, NodeType
from collections import deque


class Graph:
    _instance = None  # Atributo de classe para armazenar a única instância

    def __new__(cls):
        """Controla a criação da instância."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False  # Flag para evitar reinicialização
        return cls._instance
    

    def __init__(self):
        """Inicializa a instância única (executado apenas uma vez)."""
        if self._initialized:
            return
        self._initialized = True
        
        self.adjacency_list = {}  # Dados do grafo
        print("Grafo singleton inicializado!")  # Para debug

    def add_node(self, node: NodeModel):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, from_node: NodeModel, to_node: NodeModel):
        # Garante que os dois nós estão no grafo
        self.add_node(from_node)
        self.add_node(to_node)
        # Adiciona a conexão (assumindo grafo não-direcionado, ou seja, bidirecional)
        self.adjacency_list[from_node].append(to_node)
        self.adjacency_list[to_node].append(from_node)


    def find_shortest_path(self, start_actor: str, target_actor: str) -> list[str]:
        """
        Encontra o menor caminho entre dois atores, passando por filmes.
        
        Args:
            start_actor: Nome do ator de partida.
            target_actor: Nome do ator de destino.
        
        Returns:
            Lista com os nomes dos nós (atores e filmes) no caminho mais curto.
            Ex: ["Actor X", "Movie 1", "Actor Y", "Movie 2", "Actor Z"]
        """
        # Encontra os nós iniciais e finais
        start_node = next(
            (node for node in self.adjacency_list 
             if node.node_type == NodeType.ACTOR and node.name == start_actor),
            None
        )
        target_node = next(
            (node for node in self.adjacency_list 
             if node.node_type == NodeType.ACTOR and node.name == target_actor),
            None
        )

        if not start_node or not target_node:
            return []  # Um dos atores não existe no grafo

        # BFS para encontrar o caminho mais curto
        queue = deque()
        queue.append((start_node, [start_node.name]))
        visited = set()

        while queue:
            current_node, path = queue.popleft()

            if current_node == target_node:
                return path  # Caminho encontrado!

            for neighbor in self.adjacency_list[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor.name]))

        return []  # Não há caminho
    def get_actors(self) -> list[str]:
        """Retorna todos os nomes dos nós do tipo ator."""
        return [node.name for node in self.adjacency_list if node.node_type == NodeType.ACTOR]

    def get_movies(self) -> list[str]:
        """Retorna todos os nomes dos nós do tipo filme."""
        return [node.name for node in self.adjacency_list if node.node_type == NodeType.MOVIE]

    def __repr__(self):
        return "\n".join(f"{node.name} ({node.node_type.value}): {[n.name for n in neighbors]}"
                         for node, neighbors in self.adjacency_list.items())
