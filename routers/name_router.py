from fastapi import APIRouter
from fastapi.params import Depends

from routers.auth_router import auth_handler
from schemas.name_schemas import NameIn, NameOut
from core.agent import generate_names
from core.auth import AuthHandler

auth_handler = AuthHandler()

router = APIRouter(prefix="/name")


@router.post("/", response_model=NameOut)
async def take_ainame(
        data: NameIn,
        user_id: int = Depends(auth_handler.auth_access_dependency)):
    name_result = await generate_names(data)
    return NameOut(names=name_result.names)