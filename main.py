from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import URL, SessionLocal, criar_tabelas
from utils import gerar_slug, validar_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    criar_tabelas()
    yield


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def gerar_slug_unico(db: Session) -> str:
    while True:
        slug = gerar_slug()
        if not db.query(URL).filter(URL.slug == slug).first():
            return slug


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/criar")
def criar(request: Request, url_original: str = Form(...), db: Session = Depends(get_db)):
    if not validar_url(url_original):
        return templates.TemplateResponse(
            request,
            "index.html",
            {"erro": "URL inválida. Deve começar com http:// ou https:// e conter um domínio válido."},
        )

    slug = gerar_slug_unico(db)
    url = URL(slug=slug, url_original=url_original)
    db.add(url)
    db.commit()

    return RedirectResponse(url=f"/stats/{slug}", status_code=303)


@app.get("/stats/{slug}")
def stats(slug: str, request: Request, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.slug == slug).first()
    if not url:
        raise HTTPException(status_code=404, detail="Slug não encontrado")

    return templates.TemplateResponse(request, "stats.html", {"url": url})


@app.get("/{slug}")
def redirecionar(slug: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.slug == slug).first()
    if not url:
        raise HTTPException(status_code=404, detail="Slug não encontrado")

    url.total_cliques += 1
    db.commit()

    return RedirectResponse(url=url.url_original, status_code=307)
