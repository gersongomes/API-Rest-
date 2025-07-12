from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

dados_ficticios = {
    1: {"titulo": "A Eternidade é um Saco, Mas Alguém Tem Que Viver", "autor": "Gerson D. L. Gomes"},
    2: {"titulo": "Ser Pai é Mais Difícil que Ser Imortal", "autor": "Ary D. C. Tolentino"},
    3: {"titulo": "Dois Milênios: Memórias do Imortal", "autor": "Jerry P. R. Delgado"}
    }

@app.get("/dados/{id}")
def get_dado(id: int):
    if id in dados_ficticios:
        return dados_ficticios[id]
    return JSONResponse(status_code=404, content={"erro": "Dado não encontrado"})
