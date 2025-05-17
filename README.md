# 🧠 Assistente_CO2 — GPT + API para Due Diligence de Projetos de Carbono

![API Render](https://img.shields.io/badge/API%20Status-online-brightgreen?style=flat-square)
![GPT Custom](https://img.shields.io/badge/GPT%20Custom-integrado-blueviolet?style=flat-square)

**Assistente_CO2** é um sistema automatizado para avaliação técnica e due diligence de programas de créditos de carbono, com base em critérios regulatórios, geração de relatórios em PDF e integração com GPTs personalizados (ChatGPT Actions).

---

## 🚀 Funcionalidades

- 📊 Avaliação automatizada por critérios técnicos (adicionalidade, permanência, MRV, ODS, governança...)
- 📈 Benchmarking entre múltiplos projetos com ranking e recomendação
- 📄 Geração de relatórios técnicos estruturados em PDF
- 🔐 Conformidade automática com CORSIA, CSRD e ODS
- 🤖 Integração direta com ChatGPT personalizado via OpenAPI

---

## 📦 Estrutura do Projeto

assistente_co2/
├── backend_assistente_co2.py        # API FastAPI com avaliação + geração de PDF
├── app_streamlit.py                 # Painel visual em Streamlit
├── openapi_assistente_CO2_render.json # Schema OpenAPI para GPT Builder
├── requirements.txt                 # Dependências (FastAPI, FPDF, Streamlit, etc)
├── .render.yaml                     # Configuração de deploy automático (Render)
├── .env.example                     # Variável de ambiente simulada
├── .gitignore                       # Arquivos ignorados no versionamento
└── start_backend_assistente_co2.bat # Execução local rápida (Windows)

---

🧪 Testando Localmente
Instale as dependências:
pip install -r requirements.txt

Rode a API:
uvicorn backend_assistente_co2:app --reload

Acesse a documentação:
http://127.0.0.1:8000/docs

🌐 API Pública (Render)
A API está ativa em:
https://assistente-co2.onrender.com

Endpoints principais:

Método	Caminho	Descrição
POST	/avaliar	Avaliação simples por critérios técnicos
POST	/avaliar_detalhado	Avaliação + salvar com UUID e PDF
POST	/relatorio	Gera PDF técnico (via dados diretos)
POST	/comparar	Compara múltiplos projetos por score
GET	/avaliacao/{uid}	Retorna avaliação salva por UUID
GET	/relatorio/{uid}	Baixa o PDF gerado via UUID

🤖 GPT Personalizado (ChatGPT)
Você pode interagir via ChatGPT com o GPT customizado:
🔗 https://chatgpt.com/g/g-6827ebbc7e548191be3721efe77464c9-assistente-co2

Exemplos de comandos:
"Avalie um projeto com 30 anos de permanência e impacto social."

"Compare dois projetos com pontuações diferentes."

"Gere o PDF da última avaliação salva."

✅ Conformidades Suportadas
Este sistema detecta conformidade com:

🌍 CORSIA – Aviação internacional (ICAO)

🏢 CSRD – Diretiva de Relatórios de Sustentabilidade Corporativa (UE)

🎯 ODS – Objetivos de Desenvolvimento Sustentável (ONU)

📤 Deploy Automático
Deploy contínuo configurado com Render:

Arquivo .render.yaml define build e start.

GitHub + Render garantem CI/CD automático.

👨‍💻 Desenvolvido por
TechFarmBR
📬 Contato: pedroneto.f@hotmail.com
🔗 GitHub: github.com/TechFarmBR/assistente-co2

📄 Licença
Distribuído sob licença MIT.
