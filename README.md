# 🧠 Assistente_CO2 — GPT + API para Due Diligence de Projetos de Carbono

![API Render](https://img.shields.io/badge/API%20Status-online-brightgreen?style=flat-square)
![GPT Custom](https://img.shields.io/badge/GPT%20Custom-integrado-blueviolet?style=flat-square)

Assistente_CO2 é um projeto de análise automatizada para avaliação técnica de programas de créditos de carbono com base em critérios regulatórios, benchmarks e geração de relatórios estruturados.

Este projeto combina:

- ✅ API FastAPI (hospedada na Render)
- ✅ Integração via OpenAPI com ChatGPT (GPTs personalizados)
- ✅ Avaliação, comparação e geração de relatórios em PDF

---

## 🚀 Funcionalidades

- 📊 **Avaliação por critérios** como adicionalidade, permanência, vazamento, ODS, MRV, governança, entre outros.
- 📈 **Benchmarking** entre múltiplos projetos com recomendação automatizada.
- 📄 **Relatórios em PDF** com score por etapa e classificação final.
- 🔗 **Conformidade automática** com padrões como CORSIA, CSRD e ODS.
- 🤖 **Integração direta com GPT personalizado** (ChatGPT Actions).

---

## 📦 Estrutura do projeto

assistente_co2/
├── backend_assistente_co2.py # FastAPI com lógica de avaliação e geração de relatórios
├── openapi_assistente_CO2_render.json # Schema OpenAPI usado pelo GPT Builder
├── requirements.txt # Dependências (FastAPI, fpdf, sqlite3)
├── .render.yaml # Configuração de deploy automático no Render
├── start_backend_assistente_co2.bat # Atalho para rodar localmente

---

## 🧪 Como testar localmente

### 1. Instale as dependências

```bash
pip install -r requirements.txt

uvicorn backend_assistente_co2:app --reload
Acesse em: http://127.0.0.1:8000/docs

🌐A API está publicada e acessível via HTTPS:
https://assistente-co2.onrender.com

⚙️Endpoints principais
| Método | Caminho      | Descrição                                 |
| ------ | ------------ | ----------------------------------------- |
| POST   | `/avaliar`   | Avalia tecnicamente um projeto de carbono |
| POST   | `/relatorio` | Gera relatório técnico em PDF             |
| POST   | `/comparar`  | Compara múltiplos projetos por pontuação  |

🤖GPT Personalizado
Você pode interagir com o assistente via ChatGPT:

🔗 https://chatgpt.com/g/g-6827ebbc7e548191be3721efe77464c9-assistente-co2
Exemplos de comandos:
Avalie um projeto com 30 anos de permanência e governança forte.

Gere o relatório em PDF da última avaliação.

Compare dois projetos com perfis diferentes de impacto e MRV.

Conformidades suportadas
Este projeto verifica alinhamento automático com:

🌍 CORSIA – Carbon Offsetting and Reduction Scheme for International Aviation

📊 CSRD – Corporate Sustainability Reporting Directive

🎯 ODS – Objetivos de Desenvolvimento Sustentável (ONU)

📤Deploy automático
A infraestrutura é integrada à plataforma Render.com com deploy contínuo via .render.yaml.

👨‍💻 Desenvolvido por
TechFarmBR
Contato: pedroneto.f@hotmail.com
Repositório oficial: github.com/TechFarmBR/assistente-co2

📄 Licença
Este projeto está licenciado sob os termos da MIT License.



