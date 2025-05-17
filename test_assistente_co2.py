import requests

API_URL = "https://assistente-co2.onrender.com"
API_KEY = "co2-4Zx8tA91K3rQp72N"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def test_root():
    res = requests.get(f"{API_URL}/")
    assert res.status_code == 200
    print("🟢 Teste / raiz OK")


def test_avaliar():
    payload = {
        "programa_id": 1,
        "adicionalidade": True
    }
    res = requests.post(f"{API_URL}/avaliar", json=payload)
    assert res.status_code == 200
    print("🟢 Teste /avaliar OK")


def test_avaliar_detalhado():
    payload = {
        "programa_id": 1,
        "categoria_id": 2,
        "adicionalidade": True,
        "teste_barreiras": True,
        "permanencia_anos": 20,
        "vazamento_estimado": 4.5,
        "ods": True,
        "impacto_social": True,
        "biodiversidade": True,
        "mrv": True,
        "validação_por_terceiros": True,
        "dmrv": False,
        "governança": True,
        "transparência": True,
        "compatibilidade_net_zero": True
    }
    res = requests.post(f"{API_URL}/avaliar_detalhado", json=payload, headers=HEADERS)
    assert res.status_code == 200
    retorno = res.json()
    print("🟢 Teste /avaliar_detalhado OK")

    # Verifica os links
    assert "id" in retorno
    assert "link_resultado" in retorno
    assert "link_pdf" in retorno


def run_all():
    test_root()
    test_avaliar()
    test_avaliar_detalhado()
    print("✅ Todos os testes foram executados com sucesso!")


if __name__ == "__main__":
    run_all()
