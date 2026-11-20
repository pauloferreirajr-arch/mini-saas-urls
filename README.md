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
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn main:app --reload
```

A aplicação sobe em `http://127.0.0.1:8000`. O arquivo `urls.db` (SQLite) é criado automaticamente na primeira execução (fica fora do Git).

Não usa variáveis de ambiente nem credenciais.

## Rotas

| Rota | O que faz |
|---|---|
| `GET /` | Formulário para encurtar uma URL |
| `POST /criar` | Cria o slug e mostra o link curto |
| `GET /stats/{slug}` | Estatísticas da URL (cliques, data de criação) |
| `GET /{slug}` | Redireciona para a URL original e conta o clique |

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

## Estado atual e pendências

- **Estado:** MVP de aprendizado, funcional. Não é para produção.
- Sem autenticação, sem limite de requisições e sem testes automatizados.
- A pasta `statistic/` está vazia e o app não serve arquivos estáticos (o CSS fica nos templates).

Mais contexto do projeto em [CLAUDE.md](CLAUDE.md).
