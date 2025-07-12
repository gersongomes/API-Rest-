# Projeto Grupo 4: Comunicação Cliente-Servidor

## Descrição
Este projeto implementa uma API REST em FastAPI para consulta de dados fictícios (como livros), além de um cliente CLI que interage com essa API.

## Endpoints
- GET /dados/{id} → retorna um objeto JSON com dados ou erro se não existir.

## Instruções

1. Instale dependências:
```
pip install -r requirements.txt
```

2. Execute a API:
```
uvicorn api:app --reload
```

3. Em outro terminal, execute o cliente:
```
python cliente.py
```

## Testes
Execute com pytest:
```
pytest test_api.py
pytest test_integracao.py
```

## Estrutura
- api.py: lógica da API
- cliente.py: cliente CLI
- test_api.py: testes unitários e de API
- test_integracao.py: integração entre cliente e API
