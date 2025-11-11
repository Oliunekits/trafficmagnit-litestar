from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models import OfferWall
from app.schemas import OfferWallCreate, OfferWallUpdate

async def get_offer_walls(session: AsyncSession) -> List[OfferWall]:
    result = await session.execute(select(OfferWall))
    return result.scalars().all()

async def get_offer_wall(session: AsyncSession, pk: int) -> Optional[OfferWall]:
    return await session.get(OfferWall, pk)

async def create_offer_wall(session: AsyncSession, obj_in: OfferWallCreate) -> OfferWall:
    obj = OfferWall(**obj_in.model_dump())
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj

async def update_offer_wall(session: AsyncSession, db_obj: OfferWall, obj_in: OfferWallUpdate) -> OfferWall:
    for field, value in obj_in.model_dump(exclude_unset=True).items():
    setattr(db_obj, field, value)
    session.add(db_obj)
    await session.commit()
    await session.refresh(db_obj)
    return db_obj

async def delete_offer_wall(session: AsyncSession, db_obj: OfferWall) -> None:
    await session.delete(db_obj)
    await session.commit()