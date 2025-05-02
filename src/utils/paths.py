from pathlib import Path

# --- Configuração Base --- #
# Define o caminho raiz do projeto (sobe 2 níveis a partir deste arquivo)
PROJECT_ROOT = Path(__file__).parent.parent.parent

# --- Funções para Acesso a Dados --- #
def getLastestMovies() -> Path:
    """Retorna o caminho para arquivos na pasta `data/input/`.
    
    Args:
        file_name (str): Nome do arquivo (ex: 'dados.json').
    
    Returns:
        Path: Caminho absoluto até o arquivo.
    """
    return PROJECT_ROOT / "data" / "lastest_movies.json"

