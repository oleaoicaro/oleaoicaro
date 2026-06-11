# Alvos — Bancos BR · Riscos & Compliance (GRC)

Painel de ataque para vagas de **Especialista em Riscos e Compliance / Compliance Regulatório (GRC)** nos maiores bancos brasileiros, mirando posições **híbridas/remotas de R$ 12k+**.

> ⚠️ **Datado de jun/2026.** Vagas mudam diariamente — os links abaixo apontam para os portais/buscas, não para um anúncio específico congelado. Reconfirme a vaga antes de aplicar.

## Reality check — 5 alvos laterais vs. 2 por concurso

| Banco | Como se entra para GRC | Atacar agora? |
|---|---|---|
| **Itaú · Bradesco · Santander · BTG · Safra** | Contratação lateral direta (portal/LinkedIn). Títulos "Especialista / Sênior / Coordenador" pagam R$ 12k+ | ✅ **Foco** |
| **Banco do Brasil** | Concurso público. O de 2026 (em organização) é p/ Escriturário/Gerente; inicial ~R$ 6,3k — sem vaga lateral de Especialista GRC | ⚠️ Só via concurso |
| **Caixa** | Concurso. Aberturas recentes foram p/ engenharia/nível superior técnico; GRC é preenchido internamente | ⚠️ Só via concurso |

**Conclusão:** o alvo de R$ 12k+ híbrido mora nos **5 bancos privados**. BB/Caixa só fazem sentido pela via concurso (perfil e faixa salarial diferentes).

## CV único + ênfase por vaga

O repositório mantém **um CV mestre** (PT/EN) em [`cv/output/`](../cv/output/). Ao aplicar, use-o e **ajuste o topo (headline + resumo)** conforme a ênfase da vaga — abaixo, o que destacar para cada arquétipo de vaga GRC:

| Tipo de vaga | Ênfase no topo do CV | Pontos a puxar para cima |
|---|---|---|
| Compliance (Regulatório) | PLD-FT · BACEN/SUSEP/CVM · monitoramento e testes de conformidade | 60+ controles testados · SUSEP 638/2021 · 22 KRIs · IBM OpenPages |
| Controles Internos (Regulatório) | controles internos · SOX · COSO · design & efetividade | 60+ controles testados · análise de causa-raiz · SOX |
| Risco Operacional | risco operacional · ERM · KRI · automação de dados | heatmap de riscos · 16h→8min · 200+ normas · Power BI |
| Gestão de Riscos / LGPD | gestão de riscos · framework de riscos · LGPD/privacidade | BACEN 4.557 · TPRM · LGPD · 22 KRIs |
| Compliance — Banking & Mercado de Capitais | BACEN/CVM · TPRM · due diligence | TPRM · due diligence regulatória · CPA-20 (em andamento) |

## Lista-alvo (banco → vaga)

| # | Banco | Vaga (tipo encontrado) | Senioridade | Aderência | Ênfase no topo | Onde aplicar |
|---|---|---|---|---|---|---|
| 1 | **Safra** | Especialista em Compliance (PLD/FT, BACEN/CVM, controles internos, testes de conformidade) | Especialista | 🟢 Altíssima | Compliance Regulatório | [trabalhe-conosco](https://www.safra.com.br/trabalhe-conosco.htm) · [Gupy](https://venhasersafra.gupy.io/) |
| 2 | **Santander** | Controles Internos SR (Regulatório) / Especialista Compliance / Gerente Risco e Compliance | Sênior/Esp. | 🟢 Alta | Controles Internos | [carreiras](https://www.santander.com.br/hotsite/carreiras/) · [LinkedIn](https://br.linkedin.com/company/grupo-santander-brasil/jobs) |
| 3 | **Itaú** | Analista de Riscos e Compliance Pleno + "oportunidades dirigidas" p/ Especialista | Pleno→Esp. | 🟡 Alta | Risco Operacional | [vaga Pleno](https://carreiras.itau.com.br/vaga/sao-paulo/analista-de-riscos-e-compliance-pleno/35299/90292046880) · [busca](https://carreiras.itau.com.br/busca-de-vagas) |
| 4 | **Bradesco** | Especialista de Riscos / Analista de Riscos PL – LGPD (processo c/ 384 vagas, Osasco-SP) | PL/Esp. | 🟡 Alta | Gestão de Riscos / LGPD | [carreiras](https://banco.bradesco/) |
| 5 | **BTG Pactual** | Compliance (mín. 2 anos) / Riscos — banco de investimento | Pleno/Sr. | 🟡 Média-alta | Compliance — Banking & Mercado de Capitais | [carreiras.btgpactual.com/vagas](https://carreiras.btgpactual.com/vagas) |

> ⚠️ **Itaú:** a vaga concreta encontrada é **Pleno** — confirmar faixa salarial; se < R$ 12k, mirar as "oportunidades dirigidas" de Especialista no portal.

**Buscas-mercado de apoio:** [Especialista em Risco – SP](https://br.linkedin.com/jobs/especialista-em-risco-vagas-s%C3%A3o-paulo) · [Analista Compliance Regulatório – SP](https://br.linkedin.com/jobs/analista-de-compliance-regulat%C3%B3rio-vagas-s%C3%A3o-paulo) · [Controles Internos e Compliance](https://br.linkedin.com/jobs/controles-internos-e-compliance-vagas)

## Funil & próximos passos

1. **Aplicar** com o CV mestre ([`cv/output/`](../cv/output/)), ajustando o topo conforme a tabela de ênfase acima.
2. **Outreach** logo após aplicar — usar `outreach/templates/02_inmail_pos_aplicacao.md` (ICP "Seguradora / Banco tradicional") com o recruiter/gestor da vaga.
3. **Follow-up D+7** sem resposta — `outreach/templates/03_followup_7dias.md`.
4. **Regerar o CV** após editar `cv/data/profile.yaml`: `python cv/scripts/build_cv.py`.
