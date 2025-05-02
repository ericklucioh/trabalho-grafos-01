import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .nodeModel import NodeModel


class Graph:
    def __init__(self):
        self.adjacency_list = {}

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

    def __repr__(self):
        return "\n".join(f"{node.name} ({node.node_type.value}): {[n.name for n in neighbors]}"
                         for node, neighbors in self.adjacency_list.items())
