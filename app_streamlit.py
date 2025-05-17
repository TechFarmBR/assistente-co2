import streamlit as st
import requests

# ======== CONFIGURAÇÃO ========
API_URL = "https://assistente-co2.onrender.com"
API_KEY = "co2-4Zx8tA91K3rQp72N"

st.set_page_config(page_title="Assistente CO₂", layout="centered")
st.title("🌱 Avaliação de Projetos de Crédito de Carbono")
st.markdown("Preencha os dados do projeto e receba uma análise automatizada com relatório PDF.")

# ======== FORMULÁRIO ========
with st.form("formulario"):
    programa_id = st.number_input("ID do Programa", min_value=1)
    categoria_id = st.number_input("ID da Categoria", min_value=0, value=0)
    adicionalidade = st.checkbox("Possui Adicionalidade?")
    teste_barreiras = st.checkbox("Passou no Teste de Barreiras?")
    permanencia_anos = st.slider("Permanência (anos)", 0, 100, 30)
    vazamento = st.slider("Vazamento Estimado (%)", 0.0, 100.0, 5.0)

    st.markdown("### 🌍 Co-benefícios e Padrões")
    ods = st.checkbox("Alinha-se com ODS?")
    impacto_social = st.checkbox("Tem Impacto Social?")
    biodiversidade = st.checkbox("Protege Biodiversidade?")
    mrv = st.checkbox("Tem MRV?")
    valid_terceiros = st.checkbox("Validação por Terceiros?")
    dmrv = st.checkbox("Tem dMRV?")
    governanca = st.checkbox("Boa Governança?")
    transparencia = st.checkbox("É Transparente?")
    net_zero = st.checkbox("Compatível com Net Zero?")

    submit = st.form_submit_button("🔎 Avaliar Projeto")

# === Processamento atualizado com UUID ===
if submit:
    with st.spinner("Enviando dados para análise..."):
        headers = {"Authorization": f"Bearer {API_KEY}"}
        dados = {
            "programa_id": programa_id,
            "categoria_id": categoria_id,
            "adicionalidade": adicionalidade,
            "teste_barreiras": teste_barreiras,
            "permanencia_anos": permanencia_anos,
            "vazamento_estimado": vazamento,
            "ods": ods,
            "impacto_social": impacto_social,
            "biodiversidade": biodiversidade,
            "mrv": mrv,
            "validação_por_terceiros": valid_terceiros,
            "dmrv": dmrv,
            "governança": governanca,
            "transparência": transparencia,
            "compatibilidade_net_zero": net_zero
        }

        response = requests.post(f"{API_URL}/avaliar_detalhado", json=dados, headers=headers)

        if response.status_code == 200:
            retorno = response.json()
            resultado = retorno["resultado"]
            uuid = retorno["id"]

            st.success("✅ Avaliação concluída com sucesso!")

            st.subheader("🔎 Resultado")
            st.metric("Pontuação total", resultado["pontuacao_total"])
            st.metric("Desempenho (%)", f'{resultado["porcentagem"]}%')
            st.metric("Classificação", resultado["classificacao"])
            st.text("Conformidades: " + ", ".join(resultado["conformidades"]))

            st.subheader("📊 Pontuação por etapa")
            for etapa, score in resultado["etapas"].items():
                st.write(f"Etapa {etapa}: {score}")

            st.subheader("📎 Links salvos")
            st.code(f"{API_URL}/avaliacao/{uuid}", language="bash")
            st.markdown(f"[📥 Baixar Relatório PDF]({API_URL}/relatorio/{uuid})", unsafe_allow_html=True)

        else:
            st.error("Erro ao processar a avaliação. Verifique os dados ou tente novamente.")
