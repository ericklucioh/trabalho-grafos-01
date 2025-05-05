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

    botao_bfs = tk.Button(janela, text="Executar BFS", command=executar_bfs)
    botao_bfs.pack(pady=10)

    label_caminho = tk.Label(janela, text="Caminho Mínimo:", bg="white", anchor="w")
    label_caminho.pack(pady=5)

    caminho_texto = tk.Text(janela, height=6, width=45)
    caminho_texto.pack(padx=10)

    janela.mainloop()