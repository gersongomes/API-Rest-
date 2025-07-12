import tkinter as tk
from tkinter import messagebox
import requests

def consultar():
    resultado_text.delete("1.0", tk.END)
    try:
        dado_id = int(id_entry.get())
        resposta = requests.get(f"http://127.0.0.1:8000/dados/{dado_id}")
        if resposta.status_code == 200:
            dados = resposta.json()
            resultado_text.insert(tk.END, f"Título: {dados['titulo']}\nAutor: {dados['autor']}")
        else:
            resultado_text.insert(tk.END, "Erro: " + resposta.json().get("erro", "Erro desconhecido."))
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido.")

def limpar():
    id_entry.delete(0, tk.END)
    resultado_text.delete("1.0", tk.END)

# Janela principal
janela = tk.Tk()
janela.title("Cliente Gráfico - Consulta de Dados")
janela.geometry("400x250")
janela.resizable(False, False)

# Layout
tk.Label(janela, text="Digite o ID:", font=("Arial", 12)).pack(pady=10)
id_entry = tk.Entry(janela, font=("Arial", 12), justify="center")
id_entry.pack()

tk.Button(janela, text="Consultar", command=consultar, font=("Arial", 11), bg="#007acc", fg="white").pack(pady=5)
tk.Button(janela, text="Limpar", command=limpar, font=("Arial", 11)).pack()

resultado_text = tk.Text(janela, height=6, width=45, font=("Arial", 11))
resultado_text.pack(pady=10)

janela.mainloop()
