from sqlalchemy.exc import IntegrityError
from app.repositories.atleta_repo import AtletaRepository
from app.models.atleta import Atleta
from app.schemas.atleta import AtletaCreate

class AtletaService:
    def __init__(self, repo: AtletaRepository):
        self.repo = repo

    async def list(self, nome: str | None = None, cpf: str | None = None, limit: int = 10, offset: int = 0):
        return await self.repo.list(nome=nome, cpf=cpf, limit=limit, offset=offset)

    async def count(self, nome: str | None = None, cpf: str | None = None):
        return await self.repo.count(nome=nome, cpf=cpf)

    async def create(self, payload: AtletaCreate):
        atleta = Atleta(nome=payload.nome, cpf=payload.cpf, categoria_id=payload.categoria_id, centro_id=payload.centro_id)
        try:
            return await self.repo.create(atleta)
        except IntegrityError as ex:
            # relança e será tratado pelo handler global
            raise ex
