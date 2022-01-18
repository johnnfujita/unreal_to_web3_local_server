from fastapi import FastAPI, Depends, BackgroundTasks
from app.config import get_settings, Settings
from app.web3_interfacer import create_a_collectible, get_car, get_user_account, check_minted_nfts
from web3_vanilla.new_eth_address import create_account
from app import models, schemas, crud
from app.database import SessionLocal, engine
from typing import List
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



app = FastAPI()



@app.get("/mint_token/{nft_identifier}", response_model=schemas.NFTEntry)
def mint(nft_identifier: int, getsettings: Settings = Depends(get_settings), db: Session = Depends(get_db)):
    sender, token_id, car = create_a_collectible(nft_identifier)
    sender = sender.address
    if not token_id:
        raise Exception("no value returned")
    nft_token = crud.mint_nft(db, token_id=token_id, sender=sender, car=car)
    
    
    return nft_token

@app.get("/get_all_my_nft", response_model=List[schemas.NFTEntry])
def get_all_my_nft(settings: Settings = Depends(get_settings), db: Session = Depends(get_db)):
    
   
    nft_on_block_count, sender = check_minted_nfts()
    nfts_from_user = crud.get_nfts_by_user(db, user_address=sender, nft_on_block_count=nft_on_block_count)
    
    return nfts_from_user

@app.get("/generate_ethereum_address")
async def generate_eth_address(settings: Settings = Depends(get_settings)):
    pk, address = create_account()
    
    return {"data": 
        [
            {
            "pk": pk,
            "address": address,
            }
        ]
    }

