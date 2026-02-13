from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.crud.users import get_all_users
from core.config import settings
from core.models import db_helper
from core.schemas.user import User

router = APIRouter(prefix=settings.api.v1.prefix, tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(db: AsyncSession = Depends(db_helper.session_getter)):
    return await get_all_users(db=db)
