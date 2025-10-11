from app.db.session import engine
from app.db.base import Base
import asyncio

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def run():
    asyncio.run(init_models())

if __name__ == "__main__":
    run()
