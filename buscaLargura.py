from collections import deque

def bfs(grafo, inicio):
    """
    Executa o algoritmo de Busca em Largura (BFS) em um grafo.

    Args:
        grafo: Um dicionário onde as chaves são os nós e os valores são listas de seus vizinhos.
        inicio: O nó inicial para a busca.

    Returns:
        Um dicionário contendo informações sobre cada nó:
        - 'status': 'NOVO', 'VISITADO' ou 'EXPLORADO'
        - 'distancia': A distância do nó inicial.
        - 'pai': O nó pai na árvore BFS.
    """
    visitados = {node: {'status': 'NOVO', 'distancia': float('inf'), 'pai': None} for node in grafo}

    visitados[inicio]['status'] = 'VISITADO'
    visitados[inicio]['distancia'] = 0
    fila = deque([inicio])

    while fila:
        u = fila.popleft()
        for v in grafo.get(u, []):  # Garante que nós sem vizinhos não causem erro
            if visitados[v]['status'] == 'NOVO':
                visitados[v]['status'] = 'VISITADO'
                visitados[v]['distancia'] = visitados[u]['distancia'] + 1
                visitados[v]['pai'] = u
                fila.append(v)
        visitados[u]['status'] = 'EXPLORADO'  # Marca o nó como completamente explorado

    return visitados

# Exemplo de como usar a função:
if __name__ == "__main__":
    grafo_exemplo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    resultado_bfs = bfs(grafo_exemplo, 'A')

    for nó, info in resultado_bfs.items():
        print(f"Nó: {nó}, Status: {info['status']}, Distância: {info['distancia']}, Pai: {info['pai']}")