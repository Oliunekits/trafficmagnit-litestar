from sqlalchemy import Column, Integer, String
from app.db import Base

class OfferWall(Base):
    __tablename__ = "offer_walls"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1024), nullable=True)
