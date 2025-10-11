import re
from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

async def integrity_error_handler(request: Request, exc: IntegrityError):
    """
    Trata IntegrityError e retorna:
    status_code: 303
    detail: "Já existe um atleta cadastrado com o cpf: x"
    Onde x é extraído da mensagem de erro quando possível.
    """
    raw = ""
    try:
        raw = str(exc.orig) if exc.orig is not None else str(exc)
    except Exception:
        raw = str(exc)

    # Tenta extrair padrão PostgreSQL: Key (cpf)=(123456) already exists.
    cpf_value = None
    match = re.search(r"Key\s*\((?P<col>[^)]+)\)=\((?P<val>[^)]+)\)", raw)
    if match:
        col = match.group("col")
        val = match.group("val")
        if "cpf" in col.lower():
            cpf_value = val

    if not cpf_value:
        # tenta encontrar um trecho que pareça com CPF no texto
        m2 = re.search(r"(\d{9,14})", raw)
        if m2:
            cpf_value = m2.group(1)

    if cpf_value:
        msg = f"Já existe um atleta cadastrado com o cpf: {cpf_value}"
    else:
        msg = "Violação de integridade de dados."

    return JSONResponse(status_code=303, content={"detail": msg})
