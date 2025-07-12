import requests

def main():
    try:
        dado_id = int(input("Digite o ID para consulta: "))
        resp = requests.get(f"http://127.0.0.1:8000/dados/{dado_id}")
        if resp.status_code == 200:
            print("Resultado:", resp.json())
        else:
            print("Erro:", resp.json().get("erro"))
    except ValueError:
        print("Erro: entrada inválida.")

if __name__ == "__main__":
    main()
