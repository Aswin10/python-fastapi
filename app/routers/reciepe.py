from fastapi import APIRouter



router = APIRouter()


@router.get("/receipe/", tags=["receipe"])
async def get_receipe():
    return [{"receipe": "Sambaar"}, {"receipe": "Chatnee"}]