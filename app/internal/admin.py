from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_admin_db = {"admin": {"name": "Aswin"}}


@router.get("/")
async def read_admin():
    return fake_admin_db


@router.get("/{user_id}")
async def read_admin(user_id: str):
    if user_id not in fake_admin_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": fake_admin_db[user_id]["name"], "user_id": user_id}


@router.put(
    "/{user_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(user_id: str):
    if user_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the user: plumbus"
        )
    return {"user_id": user_id, "name": "The great Plumbus"}