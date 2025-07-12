import subprocess
import sys

def test_cliente_cli_existente():
    process = subprocess.Popen([sys.executable, "cliente.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input="1\n")
    assert "Resultado:" in stdout

def test_cliente_cli_nao_existente():
    process = subprocess.Popen([sys.executable, "cliente.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input="999\n")
    assert "Erro:" in stdout
