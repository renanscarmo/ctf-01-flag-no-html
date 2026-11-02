# CTF 01: Flag no HTML

Projeto criado a partir do [template-seguranca](https://github.com/renanscarmo/template-seguranca)
para testar a estrutura base de segurança (Bandit + pip-audit).

## Objetivo

Encontrar a flag escondida no código HTML da página e depois corrigir a falha.

## O que já vem pronto (do template)

- Pipeline no GitHub Actions
- SAST com Bandit
- SCA com pip-audit
- .gitignore protegendo senhas e arquivos locais

 ## O que aprendi

- Tudo que o servidor envia ao navegador pode ser lido, inclusive comentários HTML
- Ferramentas automáticas (Bandit e pip-audit) não pegam todos os erros
- Remover um segredo do código não basta: ele continua no histórico do Git
- Segredos devem ficar no servidor, fora do HTML



