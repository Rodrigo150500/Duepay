import sys
import os

def path_finder(path: str) -> str:
    """
    Retorna o caminho absoluto baseado em:
    - O diretório do executável (se empacotado com PyInstaller).
    - O diretório do arquivo Python (se rodando na IDE).

    Args:
        path (str): Caminho relativo a ser resolvido.

    Returns:
        str: Caminho absoluto correspondente.
    """
    if getattr(sys, 'frozen', False):
        # Empacotado com PyInstaller
        base_path = os.path.dirname(sys.executable)
    else:
        # Executado na IDE ou interpretador Python
        base_path = os.path.dirname(os.path.abspath(__file__))

    # Retorna o caminho absoluto do arquivo/diretório
    return os.path.abspath(os.path.join(base_path, path))
