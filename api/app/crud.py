from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import and_

def get_nfts_by_user( db:Session, user_address: str, nft_on_block_count: int, skip: int = 0, limit: int = 100):
    db.query(models.NFTEntry).filter(and_(user_address == models.NFTEntry.owner_account, models.NFTEntry.token_id <= nft_on_block_count)).update({models.NFTEntry.read_available: True}, synchronize_session=False)
    nfts = db.query(models.NFTEntry).filter(user_address == models.NFTEntry.owner_account).all()
    return nfts
   

def mint_nft(db:Session, token_id: int,sender: str,  car: str):
    db_nft = models.NFTEntry(token_id=token_id, owner_account=sender, car_model=car)
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
   
    return db_nft
