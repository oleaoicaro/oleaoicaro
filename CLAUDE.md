# Instruções para agentes de IA

Este é o repositório **público** de portfólio e infraestrutura de carreira de
Ícaro Vieira Leão.

## Comece por aqui

1. **`docs/AI-CONTEXT.md`** — consolidação das capacidades técnicas e dos
   projetos do portfólio. Leia antes de gerar qualquer material de carreira.
2. **`cv/data/profile.yaml`** — fonte canônica dos dados do CV (PT + EN).
   Em divergência factual, o YAML prevalece.
3. **`docs/roadmap-carreira-si.md`** — roadmap de carreira 2026–2031
   (versão canônica) e **`docs/visao-2036.md`** — horizonte estendido.

## Regras

- **Este repositório é público.** Nunca adicione, cite ou referencie aqui
  conteúdo de repositórios privados do autor (planos pessoais, finanças,
  saúde) — nem por link. O fluxo é de lá para cá, nunca o contrário, e
  somente conteúdo já público.
- Ao gerar CV, cartas ou respostas de candidatura: siga as instruções da
  seção 6 do `docs/AI-CONTEXT.md` (não exagerar, posicionamento correto
  sobre IA, cliente EY nunca nomeado).
- O status do `outreach/` é lido no topo de `outreach/README.md` antes de
  usar os templates.
- Para regenerar o currículo: `python cv/scripts/build_cv.py`
  (dependências em `cv/scripts/requirements.txt`; WeasyPrint precisa de
  Pango/Cairo — ver Quickstart no README).
