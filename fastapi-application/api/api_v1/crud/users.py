from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User


async def get_all_users(db: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await db.execute(stmt)
    return result.scalars().all()
