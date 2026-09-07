import random
import re
import string

CARACTERES = string.ascii_letters + string.digits
PADRAO_URL = re.compile(r"^https?://[^\s/]+\.[^\s/]+")


def gerar_slug(tamanho: int = 6) -> str:
    return "".join(random.choices(CARACTERES, k=tamanho))


def validar_url(url: str) -> bool:
    return bool(PADRAO_URL.match(url))


if __name__ == "__main__":
    print(gerar_slug())
    print(gerar_slug(10))

    testes = [
        ("http://exemplo.com", True),
        ("https://exemplo.com/pagina", True),
        ("https://sub.exemplo.com.br", True),
        ("ftp://exemplo.com", False),
        ("exemplo.com", False),
        ("https://semponto", False),
        ("", False),
    ]

    for url, esperado in testes:
        resultado = validar_url(url)
        status = "OK" if resultado == esperado else "FALHOU"
        print(f"[{status}] validar_url({url!r}) = {resultado} (esperado {esperado})")
