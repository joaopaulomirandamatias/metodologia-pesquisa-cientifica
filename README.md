# Metodologia da pesquisa científica — manual prático (MirandasTech)

Manual em formato de slides (54) sobre metodologia da pesquisa para pós-graduação: fundamentos e ética, do tema ao problema, classificação e escolha do método, amostragem e coleta, análise quantitativa/qualitativa/mista, projeto de pesquisa (NBR 15287:2025) e comitê de ética, redação conforme ABNT (NBR 14724:2024, 10520:2023, 6023:2025, 6028:2021), ferramentas, erros típicos, checklist e glossário com popovers. Capturas de tela reais e datadas (Plataforma Brasil, Lattes, ORCID, Sucupira, Portal CAPES, BDTD, SciELO, OSF, PRISMA, Overleaf) e figura gerada por script a partir da API aberta da OpenAlex.

**Manual on-line:** https://metodologia.mirandastech.com.br/ · **PDF:** https://metodologia.mirandastech.com.br/manual.pdf

Manual irmão: **Uso de IA na pesquisa científica** — https://manual.mirandastech.com.br/

| Pasta | O que há |
|---|---|
| `manual/` | deck HTML autônomo, PDF e fonte do artefato |
| `site/` | o que o servidor serve (`index.html`, `manual.pdf`) |
| `capturas/` | capturas reais, 08/09/2026 |
| `figuras/` | script e SVG da figura por API (OpenAlex) |
| `scripts/gerar_deck.py` | regenera HTML e PDF a partir do fonte |
| `Dockerfile` · `Caddyfile` · `railway.json` | deploy estático (Caddy) |


## Automação: agente Metodólogo, skills e scripts

| Onde | O que faz |
|---|---|
| `.claude/agents/metodologo.md` | **Agente Metodólogo**: conduz o aluno decisão a decisão (pergunta → objetivos → classificação → método → amostra → instrumento → análise → ética → cronograma), controla `PROGRESSO_METODOLOGIA.md` e só marca item com evidência. Encaminha perguntas sobre uso de IA ao agente **Orientador** do manual irmão |
| `.claude/skills/metodologo-pesquisa/` | roteiro da entrevista de decisão; mapa item → slide → evidência; respostas curtas às dúvidas frequentes |
| `.claude/skills/projeto-nbr15287/` | monta ou revisa o projeto conforme a NBR 15287:2025 a partir das decisões registradas |
| `.claude/skills/abnt-citacoes-referencias/` | confere citações (NBR 10520:2023) e lista (NBR 6023:2025) com `scripts/verificar_citacoes.py` |
| `.claude/skills/banca-simulada/` | as cinco objeções mais fortes com resposta honesta; simulação da arguição |
| `scripts/iniciar_projeto.py` | cria a estrutura do projeto e o checklist; se a pasta já tem a estrutura do manual de IA, só acrescenta o que falta |
| `scripts/verificar_citacoes.py` · `tamanho_amostra.py` · `cronograma.py` | conferência ABNT; n para proporção e para duas médias; Gantt em Markdown e SVG |
| `modelos/` | `DECISOES.md`, `USO_DE_IA.csv`, `AGENTS.md`, `matriz_sintese.csv`, `buscas.csv`, `tabela_operacionalizacao.csv`, `livro_de_codigos.csv`, `cronograma.csv`, `TCLE_modelo.md` |
| `.github/workflows/verificar.yml` | CI: integridade do deck e execução dos scripts a cada push |

### Começar em três comandos
```bash
git clone https://github.com/joaopaulomirandamatias/metodologia-pesquisa-cientifica.git
bash metodologia-pesquisa-cientifica/scripts/instalar_skills.sh
python3 metodologia-pesquisa-cientifica/scripts/iniciar_projeto.py minha-pesquisa --tema "…"
```
No Claude Code, dentro de `minha-pesquisa/`: **«Metodólogo, começar minha pesquisa»**.

### Os dois agentes juntos
Instale também o **Orientador** (repositório `ia-na-pesquisa-cientifica`). Na mesma pasta de projeto, o Metodólogo cuida do método e o Orientador do uso de IA; os dois compartilham `DECISOES.md` e `USO_DE_IA.csv`, e cada um controla o próprio checklist (`PROGRESSO_METODOLOGIA.md` e `PROGRESSO_IA.md`). Perguntas trocadas de lado são encaminhadas ao outro agente.

## Como citar
MATIAS, J. P. M. *Metodologia da pesquisa científica: manual prático.* MirandasTech, v1.0, set. 2026. CC BY 4.0.

## Declaração de uso de IA
Escrito com assistência de IA (Claude, Anthropic) na estruturação, redação, scripts e capturas. Versões das normas ABNT conferidas em fontes de bibliotecas universitárias em 08/09/2026. O autor responde integralmente pelo conteúdo.
