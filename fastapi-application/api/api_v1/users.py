from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.user import User, UserCreate
from .crud import users as users_crud

router = APIRouter(prefix=settings.api.v1.prefix, tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(
    # db: AsyncSession = Depends(db_helper.session_getter),
    db: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await users_crud.get_all_users(db=db)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    db: Annotated[AsyncSession, Depends(db_helper.session_getter)],  # modern approach
    # db: AsyncSession = Depends(
    #     db_helper.session_getter,
    # )
):
    return await users_crud.create_user(db=db, user_create=user_create)
