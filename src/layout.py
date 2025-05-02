import tkinter as tk

import tkinter as tk
from tkinter import ttk
import json
import os

from utils.paths import getLastestMovies


# Carrega os dados do arquivo JSON
file_path = getLastestMovies()


if not os.path.exists(file_path):
    raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

movies = [(movie.get("title")) for movie in data]

# Cria a janela principal
root = tk.Tk()
root.title("Trabalho Grafo - 01")

# Define o tamanho da janela
root.geometry("400x400")

# Adiciona um rótulo
label = tk.Label(root, text="Trabalho de Busca em Largura de Filmes!")
label.pack(pady=20)

# Adiciona um campo de seleção de filmes
movie_label1 = tk.Label(root, text="Selecione um filme:")
movie_label1.pack(pady=5)

movie_entry1 = ttk.Combobox(root, values=movies, state="readonly")
movie_entry1.pack(pady=5)

# Adiciona um campo de entrada para atores (desabilitado inicialmente)
actor_label1 = tk.Label(root, text="Selecione o nome de um ator:")
actor_label1.pack(pady=5)

actor_origin = ttk.Combobox(root, state="disabled")
actor_origin.pack(pady=5)

# Adiciona um campo de seleção de filmes
movie_label2 = tk.Label(root, text="Selecione outro filme:")
movie_label2.pack(pady=5)

movie_entry2 = ttk.Combobox(root, values=movies, state="readonly")
movie_entry2.pack(pady=5)

# Adiciona um campo de entrada para atores (desabilitado inicialmente)
actor_label2 = tk.Label(root, text="Selecione o nome de outro ator:")
actor_label2.pack(pady=5)

actor_destiny = ttk.Combobox(root, state="disabled")
actor_destiny.pack(pady=5)

# Função para habilitar o campo de atores com sugestões
def on_movie1_select(*_):
    selected_movie = movie_entry1.get()
    for movie in data:
        if selected_movie == movie.get("title"):
            # Habilita o campo de entrada de atores e preenche com os atores do filme selecionado
            actors = movie.get("cast", [])
            actor_origin["values"] = actors if actors else ["Nenhum ator encontrado"]
            actor_origin["state"] = "readonly"
            break

movie_entry1.bind("<<ComboboxSelected>>", on_movie1_select)

# Função para habilitar o campo de atores com sugestões
def on_movie2_select(*_):
    selected_movie = movie_entry2.get()
    for movie in data:
        if selected_movie == movie.get("title"):
            # Habilita o campo de entrada de atores e preenche com os atores do filme selecionado
            actors = movie.get("cast", [])
            actor_destiny["values"] = actors if actors else ["Nenhum ator encontrado"]
            actor_destiny["state"] = "readonly"
            break

movie_entry2.bind("<<ComboboxSelected>>", on_movie2_select)

# Cria uma janela de detalhes
def expand_frame(*_):
    if actor_origin.get() and actor_destiny.get():
        root = tk.Tk()
        root.title("Trabalho Grafo - 01")

        root.geometry("400x200")

        label = tk.Label(root, text="Trabalho de Busca em Largura de Filmes!")
        label.pack(pady=20)
    else:
        # Mostra uma mensagem de erro se o filme não for encontrado
        root = tk.Tk()
        root.title("Trabalho Grafo - 01")

        root.geometry("350x100")

        error_label = tk.Label(root, text="Atores não encontrados!", fg="red")
        error_label.pack(pady=20)

# Adiciona um botão
button = tk.Button(root, text="Clique aqui", command=expand_frame)
button.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()