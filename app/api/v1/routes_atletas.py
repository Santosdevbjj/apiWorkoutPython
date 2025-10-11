from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination.limit_offset import LimitOffsetPage
from fastapi_pagination import Params
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.atleta import AtletaCreate, AtletaRead
from app.repositories.atleta_repo import AtletaRepository
from app.services.atleta_service import AtletaService
from app.api.deps import get_session

router = APIRouter(prefix="/v1/atletas", tags=["Atletas"])

@router.get("/", response_model=LimitOffsetPage[AtletaRead])
async def list_atletas(
    nome: str | None = Query(None, description="Filtrar por nome (contains)"),
    cpf: str | None = Query(None, description="Filtrar por CPF exato"),
    limit: int = Query(10, ge=1, description="Quantidade máxima de itens (limit)"),
    offset: int = Query(0, ge=0, description="Offset de paginação"),
    session: AsyncSession = Depends(get_session),
):
    """
    Lista atletas com filtros opcionais (nome, cpf) e paginação via limit e offset.
    Response customizada incluirá nome, centro_treinamento e categoria.
    """
    repo = AtletaRepository(session)
    service = AtletaService(repo)
    total = await service.count(nome=nome, cpf=cpf)
    items = await service.list(nome=nome, cpf=cpf, limit=limit, offset=offset)

    # Mapeia os objetos ORM para schema AtletaRead (Pydantic com orm_mode)
    # fastapi-pagination fornece create to build LimitOffsetPage
    return LimitOffsetPage.create(items=items, total=total, params=Params(limit=limit, offset=offset))

@router.post("/", response_model=AtletaRead, status_code=201)
async def create_atleta(payload: AtletaCreate, session: AsyncSession = Depends(get_session)):
    """
    Cria um atleta. Em caso de violação de integridade (CPF duplicado),
    um IntegrityError será lançado e tratado pelo handler global, retornando status 303.
    """
    repo = AtletaRepository(session)
    service = AtletaService(repo)
    try:
        atleta = await service.create(payload)
        # prepara leitura com nome centro e categoria
        read = AtletaRead.from_orm(atleta)
        if atleta.categoria:
            read.categoria = atleta.categoria.nome
        if atleta.centro:
            read.centro_treinamento = atleta.centro.nome
        return read
    except Exception as exc:
        # IntegrityError será tratado pelo handler global; outros erros viram 400
        if hasattr(exc, "__cause__") and "IntegrityError" in str(type(exc.__cause__)):
            raise exc.__cause__
        raise HTTPException(status_code=400, detail=str(exc))
