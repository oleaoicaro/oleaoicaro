#!/usr/bin/env python3
"""Build per-ROLE tailored CV PDFs (PT) from the single source of truth.

Each variant overrides ONLY the `headline` and `executive_summary` of the
PT profile to mirror the keyword cluster of a specific GRC/Compliance ROLE
(not a specific bank — the same role recurs across banks). Every other field
comes verbatim from `cv/data/profile.yaml` — nothing is invented; this is
reframing, not new content.

Which role CV to use for which bank opening is mapped in
`outreach/alvos-bancos-grc.md`.

Output: cv/output/variants/Icaro_Leao_CV_PT_<Role>.{html,pdf}

Usage:
    python cv/scripts/build_variants.py
"""
import copy
import logging
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

from build_cv import DATA, TEMPLATES, LABELS, log_fonts

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

OUTPUT = TEMPLATES.parent / "output" / "variants"
OUTPUT.mkdir(parents=True, exist_ok=True)

# Per-ROLE overrides (PT only — target market is Brazilian banks).
# slug -> {headline, executive_summary}. Each slug is a GRC/Compliance role
# archetype that recurs across banks; the bank→role mapping lives in
# outreach/alvos-bancos-grc.md.
VARIANTS = {
    "Compliance-Regulatorio": {
        "headline": (
            "Especialista em Compliance Regulatório & Controles Internos | PLD-FT · "
            "BACEN/SUSEP/CVM | Monitoramento e Testes de Conformidade · ISO 37301 · "
            "IBM OpenPages | EY FSO · CRC ativo"
        ),
        "executive_summary": (
            "Especialista em compliance regulatório e controles internos no setor "
            "financeiro (EY FSO), com atuação em PLD-FT, monitoramento e testes de "
            "conformidade (design e efetividade) sobre normas BACEN/SUSEP/CVM. "
            "Implementei programa de compliance enterprise via IBM OpenPages alinhado "
            "a SOX e ISO 37301, testando mais de 60 controles e estruturando 22 KRIs "
            "em 4 dashboards. CRC ativo (1SP336304)."
        ),
    },
    "Controles-Internos": {
        "headline": (
            "Especialista Sênior em Controles Internos (Regulatório) | SOX · COSO · "
            "ISO 37301 | BACEN/SUSEP/CMN · LGPD | Testes de Design e Efetividade · "
            "IBM OpenPages | EY FSO"
        ),
        "executive_summary": (
            "Mais de 7 anos em controles internos e compliance regulatório no setor "
            "financeiro regulado (EY FSO). Testei mais de 60 controles internos "
            "(design e efetividade), classifiquei 35 achados (15 críticos) com root "
            "cause analysis e planos de ação, e liderei conformidade SOX e BACEN. "
            "Operacionalizei a Circular SUSEP 638/2021 (gestão de riscos, controles "
            "internos e compliance), análoga a CMN 4.893/2021 e BACEN 4.557. "
            "CRC ativo (1SP336304)."
        ),
    },
    "Risco-Operacional": {
        "headline": (
            "Especialista em Risco Operacional & Compliance | ERM · KRI/KCI · "
            "Risk Reporting | IBM OpenPages · Power BI · Python | BACEN/SUSEP · LGPD | "
            "EY FSO · CRC ativo"
        ),
        "executive_summary": (
            "Especialista em risco operacional e compliance no setor financeiro regulado "
            "(EY FSO), unindo gestão de riscos (ERM, KRIs, heatmap corporativo de riscos) "
            "a automação de dados (Python, Power BI) — entreguei redução de 99% no ciclo "
            "de risk reporting (16h para 8min). Mapeei mais de 200 normas "
            "(BACEN/SUSEP/ANS/LGPD) em IBM OpenPages, alinhado a SOX e ISO 37301. "
            "CRC ativo (1SP336304)."
        ),
    },
    "Gestao-Riscos-LGPD": {
        "headline": (
            "Especialista em Gestão de Riscos & Privacidade (LGPD) | Framework de Riscos · "
            "Risco Operacional · Compliance Regulatório | BACEN 4.557 · COSO ERM · "
            "IBM OpenPages · Power BI | EY FSO · CRC ativo"
        ),
        "executive_summary": (
            "Especialista em gestão de riscos e controles no setor financeiro regulado "
            "(EY FSO). Estruturei framework de riscos e controles integrando BACEN 4.557, "
            "SOX e COSO ERM, com TPRM de mais de 50 fornecedores críticos e cobertura de "
            "LGPD em auditorias risk-based. Forte camada de dados (Power BI, Python) para "
            "risk intelligence, com 22 KRIs em 4 dashboards. CRC ativo (1SP336304)."
        ),
    },
    "Compliance-Mercado-Capitais": {
        "headline": (
            "Compliance & Risk Specialist — Banking & Mercado de Capitais | "
            "Compliance Regulatório BACEN/CVM · TPRM · ISO 37301 | IBM OpenPages · "
            "Power BI | CPA-20 (em andamento) | EY FSO · CRC ativo"
        ),
        "executive_summary": (
            "Mais de 7 anos em compliance e riscos no setor financeiro regulado (EY FSO), "
            "com programas de conformidade BACEN, TPRM de mais de 30 fornecedores críticos "
            "(cloud, core banking, pagamentos) e due diligence regulatória em mais de "
            "R$ 14bi/ano para conglomerado Top 3 BR. Une fluência regulatória a automação "
            "(Python, Power BI). CPA-20 (ANBIMA) em andamento. CRC ativo (1SP336304)."
        ),
    },
}


def build_variant(slug: str, overrides: dict) -> Path:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    cv = copy.deepcopy(data["pt"])
    cv["headline"] = overrides["headline"]
    cv["executive_summary"] = overrides["executive_summary"]

    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=False)
    tpl = env.get_template("executive.html")
    html = tpl.render(cv=cv, t=LABELS["pt"])

    html_path = OUTPUT / f"Icaro_Leao_CV_PT_{slug}.html"
    html_path.write_text(html, encoding="utf-8")

    pdf_path = OUTPUT / f"Icaro_Leao_CV_PT_{slug}.pdf"
    from weasyprint import HTML
    HTML(string=html, base_url=str(TEMPLATES) + "/").write_pdf(str(pdf_path))
    log.info("Variant built: %s", pdf_path)
    return pdf_path


if __name__ == "__main__":
    log_fonts()
    for slug, ov in VARIANTS.items():
        build_variant(slug, ov)
    print("\n✅ Variants built:")
    for slug in VARIANTS:
        pdf = OUTPUT / f"Icaro_Leao_CV_PT_{slug}.pdf"
        size = pdf.stat().st_size // 1024 if pdf.exists() else 0
        status = "✓" if size > 0 else "✗ MISSING"
        print(f"  [{slug}] PDF {status} ({size} KB)")
