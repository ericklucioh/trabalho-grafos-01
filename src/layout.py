import tkinter as tk
from tkinter import ttk

from models.graphModel import Graph

def iniciar_interface():
    grafo = Graph()
    atores = grafo.get_actors()

    janela = tk.Tk()
    janela.title("TD 01")
    janela.geometry("400x400")
    janela.configure(bg="white")

    # Variável para armazenar o tipo de busca selecionado
    tipo_busca = tk.StringVar(janela, value="")

    def executar_bfs():
        tipo_busca.set("BFS")
        caminho_texto.delete("1.0", tk.END)  # Limpa o campo de texto
        origem = select_origem.get()
        destino = select_destino.get()

        if not origem or not destino:
            caminho_texto.insert(tk.END, "Por favor, selecione os atores de origem e destino.")
            return

        caminho = grafo.find_shortest_path(origem, destino)
        if caminho:
            texto = f"Caminho mínimo entre {origem} e {destino}:\n" + " -> ".join(caminho)
            texto += f"\nComprimento: {len(caminho) - 1} arestas"
        else:
            texto = f"Nenhum caminho encontrado entre {origem} e {destino}."
        caminho_texto.insert(tk.END, texto)

    def executar_bfs6():
        tipo_busca.set("BFS6")
        caminho_texto.delete("1.0", tk.END)  # Limpa o campo de texto
        origem = select_origem.get()
        destino = select_destino.get()

        if not origem or not destino:
            caminho_texto.insert(tk.END, "Por favor, selecione os atores de origem e destino.")
            return

        caminho, total_caminhos = grafo.find_max_path_within_6_edges(origem, destino)
        if caminho:
            texto = f"Caminho máximo entre {origem} e {destino}:\n" + " -> ".join(node.name for node in caminho)
            texto += f"\nComprimento: {len(caminho) - 1} arestas"
            texto += f"\nNúmero total de caminhos percorridos: {total_caminhos}"
        elif total_caminhos > 0:
            texto = f"Nenhum caminho encontrado entre {origem} e {destino} com no máximo 6 arestas."
            texto += f"\nNúmero total de caminhos percorridos: {total_caminhos}"
        else:
            texto = f"Erro: O número de arestas excede o limite de 6."
        caminho_texto.insert(tk.END, texto)

    titulo = tk.Label(janela, text="6 GRAUS DE NETWORK", font=("Helvetica", 16, "bold"), bg="white")
    titulo.pack(pady=10)

    frame_inputs = tk.Frame(janela, bg="white")
    frame_inputs.pack(pady=10)

    label_origem = tk.Label(frame_inputs, text="Ator de Origem:", bg="white", anchor="w")
    label_origem.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    select_origem = ttk.Combobox(frame_inputs, values=atores)
    select_origem.grid(row=0, column=1, padx=5, pady=5)

    label_destino = tk.Label(frame_inputs, text="Ator de Destino:", bg="white", anchor="w")
    label_destino.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    select_destino = ttk.Combobox(frame_inputs, values=atores)
    select_destino.grid(row=1, column=1, padx=5, pady=5)

    frame_botoes = tk.Frame(janela, bg="white")
    frame_botoes.pack(pady=10)

    botao_bfs = tk.Button(frame_botoes, text="Executar BFS", command=executar_bfs)
    botao_bfs.grid(row=0, column=0, padx=5)

    botao_bfs6 = tk.Button(frame_botoes, text="Executar BFS de 6 Arestas", command=executar_bfs6)
    botao_bfs6.grid(row=0, column=1, padx=5)

    label_caminho = tk.Label(janela, text="Resultado da Busca:", bg="white", anchor="w")
    label_caminho.pack(pady=5)

    caminho_texto = tk.Text(janela, height=8, width=43, state="normal")
    caminho_texto.pack(padx=10)

    janela.mainloop()

    # Retorna o tipo de busca selecionado
    return tipo_busca.get()