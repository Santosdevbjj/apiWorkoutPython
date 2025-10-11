from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_async_engine(settings.POSTGRES_DSN, future=True, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
