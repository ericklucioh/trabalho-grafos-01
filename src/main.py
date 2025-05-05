from graphConstructor import GraphConstructor
from meu_layout import iniciar_interface
from models.graphModel import Graph


def main():
    # Sua lógica principal
    print(f"Projeto rodando...")
    GraphConstructor()
    graph = Graph()
    var = graph.find_shortest_path("Brad Pitt", "Angelina Jolie")
    print(var)
    with open("grafo.txt", "w", encoding="utf-8") as f:
        for node, neighbors in graph.adjacency_list.items():
            f.write(f"{node.name} ({node.node_type.value}) -> ")
            f.write(", ".join(n.name for n in neighbors) + "\n")

if __name__ == "__main__":
    main()