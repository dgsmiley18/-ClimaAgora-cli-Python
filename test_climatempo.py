import pytest
import subprocess
from climatempo import pegar_tempo_info

def teste_cidade_nome():
    cidade_nome = "SP"
    assert pegar_tempo_info(cidade_nome)["temperatura"] is not None

def teste_ajuda():
    output = subprocess.check_output(["python", "climatempo.py", "--help"])
    assert b"especifique um local" in output