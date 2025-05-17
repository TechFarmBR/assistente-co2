from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import JSONResponse


app = FastAPI(title="API Assistente CO2", version="1.0.1")


class ProjetoCarbono(BaseModel):
    programa_id: int
    categoria_id: Optional[int] = None
    adicionalidade: bool
    teste_barreiras: Optional[bool] = False
    permanencia_anos: Optional[int] = 0
    vazamento_estimado: Optional[float] = 0.0
    ods: Optional[bool] = False
    impacto_social: Optional[bool] = False
    biodiversidade: Optional[bool] = False
    mrv: Optional[bool] = False
    validação_por_terceiros: Optional[bool] = False
    dmrv: Optional[bool] = False
    governança: Optional[bool] = False
    transparência: Optional[bool] = False
    compatibilidade_net_zero: Optional[bool] = False


class ResultadoAvaliacao(BaseModel):
    pontuacao_total: float
    porcentagem: float
    classificacao: str
    etapas: dict
    conformidades: List[str]


class ResumoRanking(BaseModel):
    programa_id: int
    pontuacao_ponderada: float
    percentual: float
    classificacao: str


@app.post("/avaliar", response_model=ResultadoAvaliacao)
def avaliar_projeto(dados: ProjetoCarbono):
    etapas = {"1": 2.8, "3": 2.0, "4": 2.6, "5": 3.2}
    total = sum(etapas.values())
    percentual = round((total / 13.8) * 100, 1)
    classificacao = (
        "Alta Integridade" if percentual >= 85 else
        "Média Integridade" if percentual >= 60 else
        "Baixa Integridade"
    )
    conformidades = []
    if dados.adicionalidade and dados.teste_barreiras:
        conformidades.append("CORSIA")
    if dados.transparência and dados.governança:
        conformidades.append("CSRD")
    if dados.ods or dados.impacto_social:
        conformidades.append("ODS")
    return ResultadoAvaliacao(
        pontuacao_total=total,
        porcentagem=percentual,
        classificacao=classificacao,
        etapas=etapas,
        conformidades=conformidades
    )


@app.post("/relatorio")
def gerar_relatorio_pdf(dados: ProjetoCarbono):
    return {"url": "https://api.exemplo.com/downloads/relatorio_final.pdf"}


@app.post("/comparar", response_model=List[ResumoRanking])
def comparar_projetos(projetos: dict):
    rankings = []
    for i, proj in enumerate(projetos["projetos"]):
        score = 10 + i
        pct = round((score / 13.8) * 100, 1)
        classificacao = "Alta Integridade" if pct >= 85 else "Média Integridade"
        rankings.append({
            "programa_id": proj["programa_id"],
            "pontuacao_ponderada": score,
            "percentual": pct,
            "classificacao": classificacao
        })
    return JSONResponse(content=rankings)

# ========= 🧩 Extensão: salvar e recuperar avaliações =========

import os
from fastapi.middleware.cors import CORSMiddleware

# Habilita CORS se for usar Streamlit externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restringir se necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "carbono.db"

def salvar_avaliacao_no_banco(projeto: dict, resultado: dict) -> str:
    uid = str(uuid.uuid4())
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes_salvas (
            id TEXT PRIMARY KEY,
            dados TEXT,
            resultado TEXT,
            criado_em TEXT
        )
    """)
    c.execute("INSERT INTO avaliacoes_salvas VALUES (?, ?, ?, ?)",
              (uid, json.dumps(projeto), json.dumps(resultado), datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return uid

@app.post("/avaliar_detalhado")
def avaliar_e_salvar(projeto: ProjetoCarbono, auth: bool = Depends(validar_chave)):
    projeto_dict = projeto.dict()
    resultado = avaliar(projeto_dict)
    uid = salvar_avaliacao_no_banco(projeto_dict, resultado)
    return {
        "id": uid,
        "resultado": resultado,
        "link_resultado": f"/avaliacao/{uid}",
        "link_pdf": f"/relatorio/{uid}"
    }

@app.get("/avaliacao/{uid}")
def consultar_avaliacao(uid: str, auth: bool = Depends(validar_chave)):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT resultado FROM avaliacoes_salvas WHERE id = ?", (uid,))
    row = c.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="ID não encontrado")
    return json.loads(row[0])

@app.get("/relatorio/{uid}")
def gerar_pdf_por_id(uid: str, auth: bool = Depends(validar_chave)):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT resultado FROM avaliacoes_salvas WHERE id = ?", (uid,))
    row = c.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="ID inválido")

    resultado = json.loads(row[0])
    nome_arquivo = f"relatorio_{uid}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Relatório Técnico CO₂", ln=True, align='C')
    pdf.set_font("Arial", "", 11)
    pdf.ln(10)
    for etapa, valor in resultado["etapas"].items():
        pdf.cell(0, 10, f"Etapa {etapa}: {valor}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, f"Pontuação Final: {resultado['pontuacao_total']}", ln=True)
    pdf.cell(0, 10, f"Classificação: {resultado['classificacao']}", ln=True)
    pdf.cell(0, 10, f"Conformidades: {', '.join(resultado['conformidades'])}", ln=True)

    pdf.output(nome_arquivo)
    return FileResponse(nome_arquivo, media_type="application/pdf", filename=nome_arquivo)
