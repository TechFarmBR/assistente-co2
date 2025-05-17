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