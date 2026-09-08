#!/usr/bin/env python3
"""Cria (ou complementa) a estrutura de um projeto de pesquisa conforme o manual de Metodologia.

    python3 scripts/iniciar_projeto.py <pasta> --tema "..." [--metodo "..."]

Se a pasta já tiver a estrutura do manual de IA (PROGRESSO_IA.md, AGENTS.md, USO_DE_IA.csv, DECISOES.md),
nada é sobrescrito: só o que falta é acrescentado, e os dois agentes passam a compartilhar DECISOES.md e USO_DE_IA.csv.
"""
import argparse, shutil, subprocess, sys
from datetime import date
from pathlib import Path
AQUI = Path(__file__).resolve().parent.parent; MODELOS = AQUI / "modelos"
PASTAS = ["00_projeto", "01_revisao/fichas", "02_instrumentos", "03_etica", "04_dados_FORA_DO_GIT", "05_analise", "06_texto"]
ITENS = [
 ("Pergunta","Pergunta clara, delimitada, empírica e viável; tabela vazia do resultado","7"),
 ("Objetivos","Objetivo geral = pergunta em ação; específicos geram resultado, não etapa","8"),
 ("Justificativa","Lacuna apontada com revisões; relevância; contribuição verificável","9"),
 ("Revisão","Buscas registradas; matriz de síntese; fichas com página","10–11"),
 ("Classificação","Natureza, abordagem, objetivo e procedimento — uma resposta por eixo","12"),
 ("Método","Frase «escolhi X porque…; descartei Y porque…» registrada","14"),
 ("Amostra","População, unidade, amostragem, n calculado e obtido","16"),
 ("Instrumento","Tabela de operacionalização; juízes; pré-teste registrado","18"),
 ("Ética","Parecer do CEP com CAAE antes da coleta; TCLE arquivado; LGPD","6, 27"),
 ("Análise","Técnica decidida antes; pressupostos; efeito com IC; categorias com trecho","21–22"),
 ("Reprodutibilidade","Dados, scripts, ambiente e decisões guardados; figura por script","24"),
 ("Estrutura","NBR 14724:2024 / 15287:2025 e modelo do programa","25, 28"),
 ("Citações","NBR 10520:2023; diretas com página; sem paráfrase próxima","30"),
 ("Referências","NBR 6023:2025 via gerenciador; DOI resolvido; texto ↔ lista","31"),
 ("Texto","Números batem com tabelas; conclusão por objetivo; limites explícitos","32"),
 ("Defesa","Cinco objeções com resposta; ensaio; material à mão","34"),
]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pasta"); ap.add_argument("--tema", default="(a definir)"); ap.add_argument("--metodo", default="(a definir)")
    a = ap.parse_args(); raiz = Path(a.pasta).resolve(); raiz.mkdir(parents=True, exist_ok=True)
    for p in PASTAS: (raiz / p).mkdir(parents=True, exist_ok=True)
    def copia(src, dst):
        if not dst.exists(): shutil.copy(src, dst); print("  +", dst.relative_to(raiz))
    copia(MODELOS / "DECISOES.md", raiz / "DECISOES.md"); copia(MODELOS / "USO_DE_IA.csv", raiz / "USO_DE_IA.csv"); copia(MODELOS / "AGENTS.md", raiz / "AGENTS.md")
    copia(MODELOS / "matriz_sintese.csv", raiz / "01_revisao/matriz_sintese.csv"); copia(MODELOS / "buscas.csv", raiz / "01_revisao/buscas.csv")
    copia(MODELOS / "tabela_operacionalizacao.csv", raiz / "02_instrumentos/tabela_operacionalizacao.csv"); copia(MODELOS / "livro_de_codigos.csv", raiz / "05_analise/livro_de_codigos.csv")
    copia(MODELOS / "TCLE_modelo.md", raiz / "03_etica/TCLE.md"); copia(MODELOS / "cronograma.csv", raiz / "00_projeto/cronograma.csv")
    dm = raiz / "00_projeto/DECISOES_METODO.md"
    if not dm.exists(): dm.write_text(f"# Decisões de método — {a.tema}\n\nRegistro da entrevista de decisão com o Metodólogo (uma seção por pergunta, com data).\n\n## Tema delimitado\n\n## Problema e lacuna\n\n## Pergunta e tabela vazia do resultado\n\n## Objetivos\n\n## Hipóteses / pressupostos e variáveis\n\n## Justificativa e delimitação\n\n## Classificação (4 eixos)\n\n## Desenho — «escolhi … porque …; descartei … porque …»\n\n## População, amostra, n\n\n## Técnicas e instrumentos\n\n## Análise\n\n## Ética\n\n## Cronograma e orçamento\n", encoding="utf-8"); print("  +", dm.relative_to(raiz))
    prog = raiz / "PROGRESSO_METODOLOGIA.md"
    if not prog.exists():
        L = [f"# Progresso (metodologia) — {a.tema}", "", f"**Método provável:** {a.metodo} · **Início:** {date.today().isoformat()} · Manual: repositório metodologia-pesquisa-cientifica", "",
             "Regra: um item só é marcado `[x]` pelo Metodólogo depois de conferir a evidência.", "", "| # | Área | Item | Slides | Estado | Data | Evidência conferida |", "|---|---|---|---|---|---|---|"]
        for i, (ar, it, sl) in enumerate(ITENS, 1): L.append(f"| {i} | {ar} | {it} | {sl} | [ ] | | |")
        prog.write_text("\n".join(L) + "\n", encoding="utf-8"); print("  +", prog.relative_to(raiz))
    gi = raiz / ".gitignore"
    if not gi.exists(): gi.write_text("04_dados_FORA_DO_GIT/\ndados_restritos_FORA_DO_GIT/\n*.xlsx\n*.xls\n.env\n", encoding="utf-8")
    elif "04_dados_FORA_DO_GIT" not in gi.read_text(encoding="utf-8"): gi.write_text(gi.read_text(encoding="utf-8").rstrip("\n") + "\n04_dados_FORA_DO_GIT/\n", encoding="utf-8")
    if not (raiz / ".git").exists(): subprocess.run(["git", "init", "-q"], cwd=raiz, check=False)
    ia = (raiz / "PROGRESSO_IA.md").exists()
    print(f"projeto pronto em {raiz}" + (" — estrutura do manual de IA detectada; os dois agentes compartilham DECISOES.md e USO_DE_IA.csv" if ia else ""))
    return 0
if __name__ == "__main__": sys.exit(main())
