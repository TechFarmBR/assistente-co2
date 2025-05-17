import streamlit as st
import requests


API_URL = "https://assistente-co2.onrender.com"
API_KEY = "SUA_CHAVE_PRIVADA"  # Substitua pela sua chave real


st.set_page_config(page_title="Assistente CO₂", page_icon="🌱")


st.title("🧠 Assistente CO₂ – Avaliação de Projetos de Carbono")
st.write("Preencha os dados do projeto abaixo para avaliar tecnicamente e gerar o relatório.")


# === Formulário de entrada ===
with st.form("formulario_avaliacao"):
    programa_id = st.number_input("ID do Programa", min_value=1)
    categoria_id = st.number_input("ID da Categoria", min_value=0)
    adicionalidade = st.checkbox("Adicionalidade comprovada")
    teste_barreiras = st.checkbox("Passa no teste de barreiras")
    permanencia_anos = st.slider("Anos de Permanência", 0, 50, 30)
    vazamento = st.slider("Vazamento estimado (%)", 0.0, 100.0, 0.0)


    st.markdown("### Critérios complementares")
    ods = st.checkbox("Contribui para ODS")
    impacto_social = st.checkbox("Possui impacto social positivo")
    biodiversidade = st.checkbox("Preserva biodiversidade")
    mrv = st.checkbox("Possui MRV robusto")
    valid_terceiros = st.checkbox("Validado por terceiros")
    dmrv = st.checkbox("Utiliza dMRV")
    governanca = st.checkbox("Boa governança")
    transparencia = st.checkbox("Transparência nos dados")
    net_zero = st.checkbox("Compatível com Net Zero")


    submit = st.form_submit_button("Avaliar Projeto")


# === Processamento ===
if submit:
    with st.spinner("Enviando dados para análise..."):
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


        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }


        response = requests.post(f"{API_URL}/avaliar", json=dados, headers=headers)


        if response.status_code == 200:
            resultado = response.json()
            st.success("✅ Avaliação concluída com sucesso!")


            st.subheader("🔎 Resultado")
            st.metric("Pontuação total", resultado["pontuacao_total"])
            st.metric("Desempenho (%)", f'{resultado["porcentagem"]}%')
            st.metric("Classificação", resultado["classificacao"])
            st.text("Conformidades: " + ", ".join(resultado["conformidades"]))


            st.subheader("📊 Pontuação por etapa")
            for etapa, score in resultado["etapas"].items():
                st.write(f"Etapa {etapa}: {score}")


            if st.button("📄 Gerar Relatório PDF"):
                r = requests.post(f"{API_URL}/relatorio", json=dados, headers=headers)
                if r.status_code == 200:
                    pdf_url = r.json().get("url")
                    st.markdown(f"[📥 Clique aqui para baixar o relatório PDF]({pdf_url})")
                else:
                    st.error("Erro ao gerar o PDF.")


        else:
            st.error("Erro ao processar a avaliação. Verifique os dados ou tente novamente.")