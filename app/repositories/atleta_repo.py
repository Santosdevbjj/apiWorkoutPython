from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.atleta import Atleta

class AtletaRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_cpf(self, cpf: str) -> Atleta | None:
        q = select(Atleta).where(Atleta.cpf == cpf).options(selectinload(Atleta.categoria), selectinload(Atleta.centro))
        result = await self.session.execute(q)
        return result.scalars().first()

    async def list(self, nome: str | None = None, cpf: str | None = None, limit: int = 10, offset: int = 0) -> list[Atleta]:
        q = select(Atleta).options(selectinload(Atleta.categoria), selectinload(Atleta.centro))
        if nome:
            q = q.where(Atleta.nome.ilike(f"%{nome}%"))
        if cpf:
            q = q.where(Atleta.cpf == cpf)
        q = q.limit(limit).offset(offset)
        result = await self.session.execute(q)
        return result.scalars().all()

    async def count(self, nome: str | None = None, cpf: str | None = None) -> int:
        q = select(func.count()).select_from(Atleta)
        if nome:
            q = q.where(Atleta.nome.ilike(f"%{nome}%"))
        if cpf:
            q = q.where(Atleta.cpf == cpf)
        result = await self.session.execute(q)
        return result.scalar_one()

    async def create(self, atleta: Atleta) -> Atleta:
        self.session.add(atleta)
        await self.session.commit()
        await self.session.refresh(atleta)
        return atleta
