# Encurtador de URLs com Analytics

Aplicação web para encurtar URLs e rastrear cliques. MVP de aprendizado, não projetado para escala de produção.

## Stack

- FastAPI + Uvicorn
- SQLAlchemy 2.0 + SQLite
- Jinja2 (templates server-side)
- Python 3.11+

## Funcionalidades

1. Criar URL encurtada (sem autenticação)
2. Redirecionar para a URL original ao acessar o slug
3. Contar cliques por URL
4. Página de estatísticas: URL, slug, total de cliques, data de criação

## Como rodar

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

A aplicação sobe em `http://127.0.0.1:8000`. O arquivo `urls.db` (SQLite) é criado automaticamente na primeira execução.

## Estrutura de arquivos

```
main.py      - app FastAPI, rotas, lógica principal
database.py  - modelo SQLAlchemy, sessão, criação de tabelas
utils.py     - gerador de slug, validação de URL
/templates   - arquivos HTML (base.html, index.html, stats.html)
```

## Regras de negócio

- Slug: 6 caracteres alfanuméricos aleatórios
- URL deve começar com `http://` ou `https://`
- Slugs são únicos (verificados antes de salvar)
- 404 para slugs inexistentes

Mais contexto do projeto em [CLAUDE.md](CLAUDE.md).
