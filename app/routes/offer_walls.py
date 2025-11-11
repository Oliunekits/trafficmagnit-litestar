from typing import Any, Dict, List, Optional

from litestar import Router, get, post, patch, delete, Response
from litestar.di import Provide
from litestar.status_codes import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import async_session
from app.models import OfferWall


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


def ow_to_dict(obj: OfferWall) -> Dict[str, Any]:
    return {
        "id": obj.id,
        "title": obj.title,
        "description": obj.description,
    }


@get("/api/offer-walls", dependencies={"session": Provide(get_session)})
async def list_offer_walls(session: AsyncSession) -> List[Dict[str, Any]]:
    result = await session.execute(select(OfferWall))
    rows = result.scalars().all()
    return [ow_to_dict(row) for row in rows]


@get(
    "/api/offer-walls/{offer_wall_id:int}",
    dependencies={"session": Provide(get_session)},
)
async def get_offer_wall(
    offer_wall_id: int, session: AsyncSession
) -> Dict[str, Any] | Response:
    obj = await session.get(OfferWall, offer_wall_id)
    if not obj:
        return Response(
            content={"detail": "Not found"},
            status_code=HTTP_404_NOT_FOUND,
            media_type="application/json",
        )
    return ow_to_dict(obj)


@post(
    "/api/offer-walls",
    dependencies={"session": Provide(get_session)},
    status_code=HTTP_201_CREATED,
)
async def create_offer_wall(
    data: Dict[str, Any], session: AsyncSession
) -> Dict[str, Any]:
    title: Optional[str] = data.get("title")
    description: Optional[str] = data.get("description")

    obj = OfferWall(title=title, description=description)
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return ow_to_dict(obj)


@patch(
    "/api/offer-walls/{offer_wall_id:int}",
    dependencies={"session": Provide(get_session)},
)
async def update_offer_wall(
    offer_wall_id: int,
    data: Dict[str, Any],
    session: AsyncSession,
) -> Dict[str, Any] | Response:
    obj = await session.get(OfferWall, offer_wall_id)
    if not obj:
        return Response(
            content={"detail": "Not found"},
            status_code=HTTP_404_NOT_FOUND,
            media_type="application/json",
        )

    if "title" in data:
        obj.title = data["title"]
    if "description" in data:
        obj.description = data["description"]

    session.add(obj)
    await session.commit()
    await session.refresh(obj)

    return ow_to_dict(obj)


@delete(
    "/api/offer-walls/{offer_wall_id:int}",
    dependencies={"session": Provide(get_session)},
    status_code=HTTP_204_NO_CONTENT,
)
async def delete_offer_wall(
    offer_wall_id: int,
    session: AsyncSession,
) -> None:
    obj = await session.get(OfferWall, offer_wall_id)
    if obj:
        await session.delete(obj)
        await session.commit()
    return None


router = Router(
    path="/",
    route_handlers=[
        list_offer_walls,
        get_offer_wall,
        create_offer_wall,
        update_offer_wall,
        delete_offer_wall,
    ],
)
