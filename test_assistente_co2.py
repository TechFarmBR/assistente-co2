import requests


BASE_URL = "https://assistente-co2.onrender.com"
API_KEY = "co2-4Zx8tA91K3rQp72N"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}


def testar_raiz():
    resp = requests.get(BASE_URL)
    assert resp.status_code == 200
    print("✅ / raiz ok")


def testar_avaliar():
    payload = {
        "programa_id": 1,
        "categoria_id": 2,
        "adicionalidade": True,
        "teste_barreiras": True,
        "permanencia_anos": 30,
        "vazamento_estimado": 5.0,
        "ods": True,
        "impacto_social": True,
        "biodiversidade": False,
        "mrv": True,
        "validação_por_terceiros": False,
        "dmrv": False,
        "governança": True,
        "transparência": True,
        "compatibilidade_net_zero": True
    }
    resp = requests.post(f"{BASE_URL}/avaliar_detalhado", json=payload, headers=HEADERS)
    assert resp.status_code == 200
    print("✅ /avaliar_detalhado funcionando")
    return resp.json()["id"]


def testar_pdf(uuid):
    resp = requests.get(f"{BASE_URL}/relatorio/{uuid}", headers=HEADERS)
    assert resp.status_code == 200
    print("✅ PDF gerado e acessível")


if __name__ == "__main__":
    print("🚀 Iniciando testes automáticos...")
    testar_raiz()
    uid = testar_avaliar()
    testar_pdf(uid)
    print("🎉 Todos os testes passaram com sucesso!")