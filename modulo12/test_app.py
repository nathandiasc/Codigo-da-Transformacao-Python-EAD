import pytest
from app import app

@pytest.fixture
def client():
    # Configura o Flask para modo de teste e cria o cliente simulado
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Teste de sucesso para a rota /somar
def test_rota_somar_sucesso(client):
    resposta = client.post('/somar', json={'a': 5, 'b': 10})
    assert resposta.status_code == 200
    assert resposta.get_json() == {'resultado': 15}

# Teste de validação para entradas inválidas na API
def test_rota_somar_dados_invalidos(client):
    resposta = client.post('/somar', json={'a': 5})
    assert resposta.status_code == 400
    assert 'erro' in resposta.get_json()