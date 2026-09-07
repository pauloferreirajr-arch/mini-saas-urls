from datetime import datetime

from sqlalchemy import String, Integer, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

engine = create_engine("sqlite:///urls.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class URL(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(String(6), unique=True, nullable=False, index=True)
    url_original: Mapped[str] = mapped_column(String(2048), nullable=False)
    criado_em: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    total_cliques: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


def criar_tabelas():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    criar_tabelas()
