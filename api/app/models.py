from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class NFTEntry(Base):
    __tablename__ = "nft_entry"

    token_id = Column(Integer, primary_key=True, index=True)
    owner_account = Column(String, index=True)
    read_available = Column(Boolean, default=False)
    car_model = Column(String)