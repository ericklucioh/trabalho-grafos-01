from graphConstructor import GraphConstructor
from meu_layout import iniciar_interface
from models.graphModel import Graph

# Variável global para armazenar o tipo de busca selecionada
tipo_busca = None

def executar_busca(graph, caminho_texto, origem, destino):
    """
    Executa a busca com base no tipo selecionado e exibe o resultado no campo caminho_texto.
    """
    caminho_texto.delete("1.0", "end")  # Limpa o campo de texto

    if tipo_busca == "BFS":
        caminho = graph.find_shortest_path(origem, destino)
        if caminho:
            comprimento = len(caminho) - 1  # Comprimento do caminho em arestas
            texto = f"Caminho mínimo entre {origem} e {destino}:\n" + " -> ".join(caminho)
            texto += f"\nComprimento: {comprimento} arestas"
        else:
            texto = f"Nenhum caminho encontrado entre {origem} e {destino}."
        caminho_texto.insert("1.0", texto)
    elif tipo_busca == "BFS6":
        caminho, total_caminhos = graph.find_max_path_within_6_edges(origem, destino)
        if caminho:
            comprimento = len(caminho) - 1  # Comprimento do caminho em arestas
            texto = f"Caminho máximo entre {origem} e {destino}:\n" + " -> ".join(node.name for node in caminho)
            texto += f"\nComprimento: {comprimento} arestas"
            texto += f"\nNúmero total de caminhos percorridos: {total_caminhos}"
        elif total_caminhos > 0:
            texto = f"Nenhum caminho encontrado entre {origem} e {destino} com no máximo 6 arestas."
            texto += f"\nNúmero total de caminhos percorridos: {total_caminhos}"
        else:
            texto = f"Erro: O número de arestas excede o limite de 6."
        caminho_texto.insert("1.0", texto)
    else:
        texto = "Nenhum tipo de busca foi selecionado."
        caminho_texto.insert("1.0", texto)

def main():
    global tipo_busca

    # Inicializa o construtor do grafo
    print(f"Projeto rodando...")
    GraphConstructor()
    graph = Graph()

    # Define o tipo de busca com base na interface gráfica
    resultado = iniciar_interface()
    if len(resultado) == 4:
        tipo_busca, caminho_texto_widget, origem, destino = resultado
        if hasattr(caminho_texto_widget, "delete"):
            caminho_texto = caminho_texto_widget
        else:
            print("Erro: caminho_texto não é um widget de texto válido.")
            return
    else:
        print("Erro: iniciar_interface() não retornou exatamente 4 valores.")
        return

    # Executa a busca com base no tipo selecionado
    executar_busca(graph, caminho_texto, origem, destino)

if __name__ == "__main__":
    main()