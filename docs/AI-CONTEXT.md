# AI Context — Capacidades de Ícaro Vieira Leão com IA e Engenharia

> **Para agentes de IA**: este documento existe para que você, trabalhando apenas com o repositório `oleaoicaro`, entenda o que o autor sabe fazer — especialmente com IA — com base em evidências concretas extraídas de **todos os seus repositórios no GitHub** (`github.com/oleaoicaro`). Use-o como fonte de verdade ao gerar currículos, cartas, respostas de candidatura, variantes de CV ou qualquer material que descreva as competências técnicas do autor.
>
> Última consolidação: junho/2026, gerada por análise automatizada do código-fonte dos 5 repositórios de projetos.

---

## 1. Quem é o autor (resumo de 30 segundos)

**Ícaro Vieira Leão** — Especialista em Riscos, Controles Internos & Compliance Regulatório no setor financeiro regulado (Seguros · Banking · Saúde), Consultor Sênior | Risk & Compliance na EY FSO. CRC ativo (1SP336304). Perfil híbrido raro: **fluência regulatória profunda (SUSEP, BACEN, ANS, LGPD, SOX, COSO, ISO 37301) combinada com capacidade real de construir software** — não apenas "usa ferramentas", mas projeta e implementa sistemas full-stack completos com integração de IA, do scraping ao deploy.

A tese central do portfólio: **ele constrói, com auxílio de IA, as ferramentas de GRC/regtech que normalmente exigiriam um time de engenharia** — e o faz com critério de compliance embutido (auditabilidade, rastreabilidade, RBAC, LGPD) porque esse é o seu domínio profissional.

## 2. O que ele consegue fazer com IA (capacidades demonstradas)

### 2.1 Desenvolvimento assistido por IA (AI-augmented engineering)
Todos os 5 repositórios de projeto foram construídos por uma única pessoa, sem time de engenharia, usando IA generativa (Claude/Claude Code e similares) como multiplicador. Evidências do nível alcançado:

- **Arquiteturas de nível enterprise**: Clean Architecture + DDD, camadas separadas (interface/aplicação/domínio/infra), migrations versionadas (Alembic), CI/CD com GitHub Actions, Docker Compose multi-serviço.
- **Full-stack real**: backends assíncronos (FastAPI + SQLAlchemy 2.0 async + Celery/Redis) e frontends modernos (React 18/19, Next.js 14, TypeScript estrito, Tailwind, shadcn/ui, Radix).
- **Qualidade de produção**: testes (pytest, Vitest, 77+ testes em um dos projetos), linting (ruff, mypy, ESLint 9), SonarQube, observabilidade (Prometheus, structlog, Sentry), security headers OWASP, rate limiting.

### 2.2 Integração de LLMs em produtos
- **Enriquecimento de documentos regulatórios por LLM** (Regulatory Intelligence Hub): resumo automático de normas, classificação temática (capital, governança, PLD/FT...), score de impacto regulatório 0–100 — via OpenAI API com **graceful degradation** para heurísticas Python quando a API não está configurada.
- **Chat assistente especializado** (SUSEP Benchmarking): endpoint de chat com system prompt especializado em mercado segurador brasileiro, autenticação OAuth2 client-credentials com cache de token, tratamento tipado de erros (timeout, auth, upstream).
- **Uso profissional de GenAI na EY**: triagem de 150+ normativos (ANS/BACEN/LGPD) com IA generativa e revisão humana, +85% de eficiência analítica (registrado no CV).

### 2.3 Automação e pipelines de dados
- **Scraping resiliente** de portais governamentais: estratégia em cascata (API JSON → Playwright headless para páginas JavaScript → BeautifulSoup como fallback), retry com backoff exponencial, deduplicação por chave natural + checksum, idempotência.
- **ETL estruturado**: arquitetura spec/registry/fetcher/parser/loader para 13+ datasets públicos da SUSEP; agendamento (Celery Beat, APScheduler); tabelas de controle de execução.
- **Processamento de Excel corporativo**: parsing com detecção automática de colunas (fuzzy matching de headers), normalização de dados, geração de relatórios multi-aba com gráficos embutidos (pandas, openpyxl, SheetJS).

### 2.4 Motores de regras e scoring (IA simbólica/determinística)
Onde LLM não é apropriado (decisões auditáveis de risco), ele projeta **motores de regras determinísticos e rastreáveis** — um diferencial de quem entende compliance:
- 44 regras de detecção de fraude em 6 dimensões (Antifraud System);
- 26 regras de agravamento de risco com trace regra a regra e matriz Frequência × Impacto 5×5 (Retroalimentação);
- score de risco composto de 10 pilares com pesos e classificação (SUSEP Benchmarking);
- auto-classificação leve por aprendizado de keywords a partir de exemplos manuais (sem dependência de API externa).

### 2.5 Governança de IA
- Formação em andamento: graduação em **Análise de Dados com foco em IA**; estudo de **ISO/IEC 42001** (AI Management Systems).
- Padrão consistente nos projetos: IA **assistiva, nunca decisória sem supervisão** — toda mudança de risco é auditada, overrides exigem justificativa, fallbacks determinísticos existem para quando a IA falha. Isso reflete a postura profissional dele sobre IA em ambientes regulados.

## 3. Os repositórios, um a um

### 3.1 `regulatoryintelligencehub` — Regulatory Intelligence Hub
**O quê**: plataforma full-stack de GRC ("Bloomberg regulatório brasileiro") — coleta automática de normas SUSEP, enriquecimento por IA e fluxo completo de conformidade (encaminhamento empresa × área → classificação de risco → planos de ação → testes de controles → painel).
**Stack**: Python 3.11, FastAPI, SQLAlchemy 2.0 async, PostgreSQL, Celery + Redis, Playwright, OpenAI API, Strawberry GraphQL, Next.js 14 + TypeScript + Tailwind, Docker Compose, GitHub Actions, Prometheus, structlog.
**IA**: resumo/classificação/score de impacto de normas via LLM com fallback heurístico.
**Destaques de engenharia**: Clean Architecture + DDD; arquitetura multi-regulador extensível (BACEN/CVM/ANS via config, sem tocar no core); pipeline de ingestão idempotente com versionamento de alterações; JWT + RBAC hierárquico + auditoria append-only.

### 3.2 `susep-benchmarking` — SUSEP Benchmarking Platform (v3.2)
**O quê**: plataforma de benchmarking do mercado segurador brasileiro sobre dados abertos da SUSEP — rankings, market share (HHI), sinistralidade, solvência, processos sancionadores, AUTOSEG regional, score integrado de 10 pilares e chat com IA.
**Stack**: Python 3.11, FastAPI, SQLAlchemy 2.0, Pandas, APScheduler, Alembic, Jinja2 + Bootstrap 5 + Plotly.js, Docker, deploy Render, Sentry, PostHog (LGPD-aware).
**IA**: chat assistente especializado via integração LLM (OAuth2 Azure AD, cache de token, erros tipados).
**Destaques de engenharia**: ETL modular (spec/registry/fetcher/parser/loader) para 13+ datasets; sistema de planos Free/Pro com guardrails em todas as queries; JWT + Google OAuth + refresh token de uso único; 24+ endpoints REST documentados; 77+ testes.

### 3.3 `Antifraudsystem` — Antifraud System (MVP front-end)
**O quê**: plataforma de detecção e gestão de fraude em sinistros de seguros de vida/previdência — scoring com 44 regras em 6 grupos (provedores/trilhas, visuais/digitais, temporais, estatísticos, lógicos, comportamentais/contextuais), workflow com visualização em grafo, dashboards executivos com mapa geográfico, gestão de time, administração de regras.
**Stack**: React 18 + TypeScript, Vite, Tailwind 4, Radix UI + shadcn/ui, Recharts, React Router. 100% front-end com dados simulados (mock) — demonstra UX complexa e modelagem de domínio, não backend.
**Domínio**: tipologias reais de fraude (contratação pós-óbito, falsificação documental, automutilação, documentos duplicados por hash, incompatibilidade CRM/especialidade × CID), SLA regulatório, MFA, RBAC em 4 papéis.

### 3.4 `retroalimentacao` — Retroalimentação de Risco Regulatório
**O quê**: sistema que recalcula o risco de normas regulatórias a partir de evidências reais (autos de infração, auditorias BUD-GBS, ofícios SUSEP, autoavaliação), comparando risco base × risco agravado via 26 regras configuráveis e matriz Frequência × Impacto 5×5. Entregue como **HTML autossuficiente** (roda sem servidor — restrição corporativa real).
**Stack**: React 19 + TypeScript 5.9, Vite 7 (single-file build), Tailwind + shadcn/ui, SheetJS, Recharts, Zod, Vitest, SonarQube.
**Destaques**: pipeline de 6 etapas (ingestão → detecção de colunas → data steward → matching fuzzy → simulação → renderização); auto-classificação por aprendizado de keywords; trace regra a regra (before/after); auditoria com diff e correlationId; o risco nunca reduz automaticamente (princípio de governança).

### 3.5 `compliance` — AIRNC (Análise de Normas Regulatórias)
**O quê**: ferramenta corporativa de gestão de normas e planos de ação (demandas SUSEP) usada em contexto real — SPA offline-first sem servidor, sincronização via File System Access API em rede corporativa (SharePoint), merge inteligente com dirty-tracking, auditoria completa, e ETL Python que gera heatmaps de criticidade (Frequência × Impacto) embutidos em Excel.
**Stack**: JavaScript vanilla (~4.800 linhas, sem framework), SheetJS, IndexedDB/localStorage, Python (pandas, matplotlib/seaborn, openpyxl, Pillow), scripts .bat de instalação 1-clique.
**Destaques**: prova de que ele entrega valor **dentro de restrições corporativas severas** (sem servidor, sem instalação de software, ambiente Windows travado) — engenharia pragmática, não só stack da moda.

### 3.6 `oleaoicaro` — este repositório (meta-infraestrutura de carreira)
Geração automatizada de CV executivo PT/EN a partir de fonte única YAML (`cv/data/profile.yaml`) com Jinja2 + WeasyPrint (fallback Playwright), variantes de CV por ICP, plano de outreach com KPIs, integração com agente de candidaturas LinkedIn, e agente revisor de CV (`.github/agents/cv-hr-reviewer`). **O próprio repositório é uma demonstração de automação com IA aplicada à carreira.**

## 4. Matriz consolidada de competências técnicas (com evidência)

| Competência | Evidência (repositório) |
|---|---|
| Integração LLM (OpenAI API, chat, prompts, fallbacks) | regulatoryintelligencehub, susep-benchmarking |
| Python backend (FastAPI, SQLAlchemy async, Celery) | regulatoryintelligencehub, susep-benchmarking |
| React/TypeScript (18/19, Next.js, Vite, Tailwind, shadcn) | Antifraudsystem, retroalimentacao, regulatoryintelligencehub |
| ETL / dados públicos / scraping (Playwright, pandas) | susep-benchmarking, regulatoryintelligencehub, compliance |
| Motores de regras auditáveis e risk scoring | retroalimentacao (26), Antifraudsystem (44), susep-benchmarking (10 pilares) |
| Segurança de aplicação (JWT, RBAC, MFA, OWASP headers, rate limit) | todos os projetos com auth |
| Auditoria/rastreabilidade by design (logs append-only, diffs, justificativas) | retroalimentacao, compliance, regulatoryintelligencehub |
| DevOps (Docker, CI/CD, migrations, observabilidade) | regulatoryintelligencehub, susep-benchmarking |
| Testes e qualidade (pytest, Vitest, SonarQube, lint estrito) | susep-benchmarking, retroalimentacao, regulatoryintelligencehub |
| Engenharia sob restrição corporativa (offline-first, single-file) | compliance, retroalimentacao |

## 5. Domínio de negócio que atravessa tudo

Todos os projetos vivem no mesmo domínio — **GRC para o setor financeiro/segurador brasileiro regulado** — que é onde ele trabalha profissionalmente (EY FSO):
- **Reguladores**: SUSEP (foco), BACEN, ANS, CVM, CNSP; normas como Circular SUSEP 638/2021, Res. CMN 4.893, BACEN 4.557.
- **Conceitos**: matriz Frequência × Impacto, KRIs, planos de ação, testes de controles, processos sancionadores, solvência, sinistralidade, PLD-FT, LGPD, Three Lines Model, SOX/COSO/ISO 37301.
- **Experiência corporativa correspondente**: IBM OpenPages enterprise, 200+ normas mapeadas, redução de 99% em risk reporting, auditorias risk-based — ver `cv/data/profile.yaml` (fonte canônica do CV).

## 6. Como usar este documento (instruções para a IA)

1. **Fonte canônica do CV**: `cv/data/profile.yaml` (PT + EN). Este documento complementa o YAML com o detalhe técnico dos projetos; em caso de divergência factual sobre dados pessoais/experiência, o YAML prevalece.
2. **Ao gerar variantes de CV ou respostas de candidatura**: selecione evidências da matriz da seção 4 conforme a vaga (ex.: vaga de "GRC + IA" → seções 2.2, 2.4, 2.5; vaga de "engenharia de dados" → seção 2.3).
3. **Não exagere**: os projetos pessoais são MVPs/ferramentas de autor único — descreva-os como tal. A força do perfil é a **combinação domínio regulatório + capacidade de construção com IA**, não "engenheiro de software sênior tradicional".
4. **Posicionamento correto sobre IA**: ele não treina modelos; ele **integra LLMs em produtos, constrói automação e motores de regras auditáveis, e aplica governança de IA** — sempre com supervisão humana e rastreabilidade, postura adequada a ambientes regulados.
5. Os repositórios de projeto podem ser privados ou não estar disponíveis na sua sessão — este documento foi escrito justamente para que você não precise deles.
