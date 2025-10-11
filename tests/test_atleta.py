import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_health(async_client: AsyncClient):
    r = await async_client.get("/v1/atletas/")
    assert r.status_code in (200, 422, 303)  # depende se DB está configurado
