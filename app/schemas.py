from typing import Optional
from pydantic import BaseModel


class OfferWallBase(BaseModel):
    title: str
    description: Optional[str] = None


class OfferWallCreate(OfferWallBase):
    pass


class OfferWallUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class OfferWallRead(OfferWallBase):
    id: int

    class Config:
        # pydantic v2
        from_attributes = True
