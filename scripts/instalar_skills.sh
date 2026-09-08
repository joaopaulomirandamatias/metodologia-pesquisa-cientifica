#!/usr/bin/env bash
# Instala o agente Metodólogo e suas skills no Claude Code (pessoal: ~/.claude). Convive com o agente Orientador do manual de IA.
set -e
AQUI="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p ~/.claude/skills ~/.claude/agents
for s in metodologo-pesquisa projeto-nbr15287 abnt-citacoes-referencias banca-simulada; do cp -r "$AQUI/.claude/skills/$s" ~/.claude/skills/; done
cp "$AQUI/.claude/agents/metodologo.md" ~/.claude/agents/
echo "instalado: $(ls ~/.claude/agents | tr '\n' ' ')"; echo "skills: $(ls ~/.claude/skills | grep -E 'metodologo|nbr15287|abnt-cit|banca' | tr '\n' ' ')"
[ -f ~/.claude/agents/orientador.md ] && echo "Orientador (manual de IA) também instalado — os dois compartilham DECISOES.md e USO_DE_IA.csv." || echo "Dica: instale também o Orientador do manual de IA: https://github.com/joaopaulomirandamatias/ia-na-pesquisa-cientifica"
echo; echo "No Claude Code, na pasta do projeto: \"Metodólogo, começar minha pesquisa\"."
