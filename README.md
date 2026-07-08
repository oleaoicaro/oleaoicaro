# Ícaro Leão — Portfólio

> Repositório pessoal de **Ícaro Vieira Leão** — geração automatizada de currículo executivo (PT/EN), plano de outreach de carreira e integração com agente de candidaturas no LinkedIn.

[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Node.js 18+](https://img.shields.io/badge/Node.js-18%2B-339933.svg)](https://nodejs.org/)

## Sobre

Sou **Information Security Analyst III no Bradesco**, atuando em segurança da informação no maior ecossistema bancário privado do país. Chego à área de Security com uma base de mais de **7 anos em gestão de riscos, controles internos e compliance regulatório** no setor financeiro (EY FSO — seguradoras Top 5, conglomerado bancário Top 3 e saúde), onde liderei a implementação do GRC corporativo (**IBM OpenPages**) de uma seguradora Top 5, com mais de **200 normas mapeadas** (SUSEP, BACEN, ANS, ANPD). Trabalho com frameworks de segurança e controle (**ISO 27001, NIST CSF, COBIT 2019, LGPD, CMN 4.893/Cibersegurança**) e integro essa leitura regulatória com **automação em dados e IA** (Python, Power BI). Trajetória anterior em auditoria governamental (TCE-PI) e contabilidade (**CRC ativo**, 1SP336304), além de projetos próprios em **fintech / regtech**.

Este repositório é a **infraestrutura** que sustenta meu reposicionamento profissional: o currículo é gerado a partir de dados estruturados (YAML) com templates Jinja2 + WeasyPrint, e o outreach segue um plano operacional com KPIs semanais.

- 💼 **LinkedIn** — [linkedin.com/in/oleaoicaro](https://www.linkedin.com/in/oleaoicaro)
- ✉️ **E-mail** — icaro.vl@outlook.com
- 🐙 **GitHub** — [github.com/oleaoicaro](https://github.com/oleaoicaro)

## 👤 Para Recrutadores — comece por aqui

Tudo que você precisa para avaliar minha aderência a uma vaga está em **um único diretório**: [`cv/`](cv/).

| Material | Arquivo | Descrição |
|---|---|---|
| 📄 Currículo (PT) | [`cv/output/Icaro_Leao_CV_PT.pdf`](cv/output/Icaro_Leao_CV_PT.pdf) | CV executivo em português |
| 📄 Currículo (EN) | [`cv/output/Icaro_Leao_CV_EN.pdf`](cv/output/Icaro_Leao_CV_EN.pdf) | Executive CV in English |
| 🎓 Cursos & Certificações | [`cv/Cursos_e_Certificacoes.md`](cv/Cursos_e_Certificacoes.md) | **284 treinamentos (2022–2026)** organizados por área temática — destaques em GenAI, AML, LGPD, Banking & Insurance |
| 📊 Planilha de cursos | [`cv/Cursos_e_Certificacoes.csv`](cv/Cursos_e_Certificacoes.csv) | Mesma listagem, filtrável em Excel/Google Sheets |

> **Em uma frase**: Information Security Analyst III no **Bradesco**, com 15 anos de trajetória profissional e 7+ em gestão de riscos, compliance e auditoria interna no setor financeiro regulado (EY FSO — Top 5 seguradoras, Top 3 conglomerado bancário BR e saúde) — liderança na implementação de GRC corporativo (**IBM OpenPages**, 200+ normas SUSEP/BACEN/ANS/ANPD), track record em **ISO 27001, NIST CSF, LGPD, SOX, COSO e ISO 37301**, com automação (Python · Power BI) e governança de IA (ISO/IEC 42001). CRC ativo (1SP336304); rota de certificações 2026–2029: **CRISC → CISA → CISSP → CISM**.

## O que mais tem aqui

O restante deste repositório é **infraestrutura** que sustenta o portfólio acima — código que gera o CV, plano de outreach e integração com agente de candidaturas. Não é necessário para avaliação de aderência:

| Diretório | Conteúdo | README |
|---|---|---|
| [`cv/`](cv/) | Materiais para recrutador (acima) **+** geração automatizada do CV (PT/EN, HTML + PDF) a partir de `profile.yaml` com Jinja2 + WeasyPrint. | [cv/README.md](cv/README.md) |
| [`outreach/`](outreach/) | Plano de outreach de 4 semanas com templates de mensagens (connection request, InMail, follow-up, pós-entrevista) por ICP. | [outreach/README.md](outreach/README.md) |
| [`ai-job-agent/`](ai-job-agent/) | Submódulo: agente externo de candidaturas no LinkedIn ([AkbarDevop/ai-job-agent](https://github.com/AkbarDevop/ai-job-agent)). | [docs/AI-JOB-AGENT.md](docs/AI-JOB-AGENT.md) |
| [`config/`](config/) | Templates de configuração para o agente (credenciais, perfil, banco de respostas) — arquivos reais ficam fora do git. | — |
| [`docs/`](docs/) | Documentação operacional + `archive/` com histórico do projeto e dados-fonte dos cursos. | [docs/archive/README.md](docs/archive/README.md) |
| [`docs/AI-CONTEXT.md`](docs/AI-CONTEXT.md) | **Contexto para agentes de IA**: consolidação das capacidades técnicas e de IA demonstradas em todos os repositórios do portfólio (`regulatoryintelligencehub`, `susep-benchmarking`, `Antifraudsystem`, `retroalimentacao`, `compliance`) — permite que uma IA trabalhando só com este repositório entenda o portfólio completo. | [docs/AI-CONTEXT.md](docs/AI-CONTEXT.md) |

## Quickstart — Gerar o currículo

```bash
# 1. Pré-requisitos do sistema (Ubuntu/Debian — WeasyPrint precisa de Pango/Cairo)
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libpangocairo-1.0-0 \
                 libharfbuzz0b libfontconfig1 libcairo2

# 2. Dependências Python
pip install -r cv/scripts/requirements.txt

# 3. Build (gera HTML + PDF em PT e EN)
python cv/scripts/build_cv.py
```

Saída em [`cv/output/`](cv/output/). Detalhes (paleta, fontes, fallback Playwright, personalização) em [cv/README.md](cv/README.md).

## Stack

| Camada | Tecnologia |
|---|---|
| Dados do CV | YAML (fonte única PT + EN) |
| Templates | Jinja2 |
| Render PDF | WeasyPrint (primário) · Playwright/Chromium (fallback) |
| Tipografia | Liberation Serif + Inter (fontes locais bundled) |
| Agente LinkedIn | Node.js 18+ (submódulo `ai-job-agent`) |
| Scripting auxiliar | Python 3.11+ |

## Licença

[MIT](LICENSE) — sinta-se livre para usar a estrutura como referência para o seu próprio portfólio. Conteúdo do `profile.yaml` (dados pessoais, histórico profissional) é meu e não está sob a licença MIT.

---

## About (English)

Personal repository of **Ícaro Vieira Leão** — Information Security Analyst III at **Bradesco**, building on 7+ years in risk management, internal controls and regulatory compliance across Brazil's regulated financial sector (EY FSO — Top 5 insurers, a Top 3 banking conglomerate and health operators), where he led the corporate GRC implementation (IBM OpenPages) at a Top 5 insurer, mapping 200+ regulations (SUSEP, BACEN, ANS, ANPD). Works with security and control frameworks (ISO 27001, NIST CSF, COBIT 2019, LGPD) combined with data and AI automation (Python, Power BI). Active CRC. Hosts an automated executive CV builder (PT/EN, HTML + PDF) driven by a single YAML source, a 4-week outreach playbook, and a LinkedIn auto-apply agent integration.

Generated CV (English): [`cv/output/Icaro_Leao_CV_EN.pdf`](cv/output/Icaro_Leao_CV_EN.pdf) · Courses & Certifications (PT, 284 trainings 2022–2026): [`cv/Cursos_e_Certificacoes.md`](cv/Cursos_e_Certificacoes.md) · LinkedIn: [linkedin.com/in/oleaoicaro](https://www.linkedin.com/in/oleaoicaro)
