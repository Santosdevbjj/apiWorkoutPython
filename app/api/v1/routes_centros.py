from fastapi import APIRouter

router = APIRouter(prefix="/v1/centros", tags=["Centros"])

@router.get("/")
async def list_centros():
    return {"message": "Lista de centros - implemente conforme necessário"}
