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
            st.markdown(f"[📥 Baixar Relatório PDF]({API_URL}/relatorio/{uuid})")

        else:
            st.error("Erro ao processar a avaliação. Verifique os dados ou tente novamente.")
