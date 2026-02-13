from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas.user import UserCreate


async def get_all_users(db: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_user(db: AsyncSession, user_create: UserCreate) -> User:
    user = User(**user_create.model_dump())
    db.add(user)
    await db.commit()
    # await db.refresh(user)
    return user
