# Encurtador de URLs com Analytics

## Contexto
Aplicação web para encurtar URLs e rastrear cliques. MVP de aprendizado, não projetado para escala de produção.

## Stack
- FastAPI + Uvicorn para o servidor
- SQLAlchemy 2.0 + SQLite para dados
- Jinja2 para renderização de HTML
- Python 3.11

## Funcionalidades do MVP
1. Criar URL encurtada (sem autenticação)
2. Redirecionar para URL original ao acessar o slug
3. Contar cliques por URL
4. Página de stats mostrando: URL, slug, total de cliques, data

## Estrutura de arquivos
- `main.py`      - app FastAPI, rotas, lógica principal
- `database.py`  - modelo SQLAlchemy, sessão, criação de tabelas
- `utils.py`     - gerador de slug, validação de URL
- `/templates`   - arquivos HTML (base.html, index.html, stats.html)
- `/statistic`   - vazia (o app não monta arquivos estáticos; estilos ficam nos templates)

## Regras do repositório
- Repositório **público**: nada interno, sem credenciais, sem dados de clientes ou pessoais.
- `urls.db` não é versionado (`*.db` no `.gitignore`).

## Regras de negócio
- Slug: 6 caracteres alfanuméricos aleatórios
- URL deve começar com http:// ou https://
- Slugs são únicos (verificar antes de salvar)
- 404 para slugs inexistentes
