import brownie.project as project
from brownie import network, accounts, config
import random
import time

from sqlalchemy.orm import Session
from app import models, schemas



def get_car(car_number):
    switch = {0: "SPORT_CAR", 1: "HATCHBACK", 2: "SUV"}
    return switch[car_number]

car_metadata_dic = {
    0: "https://ipfs.io/ipfs/QmeYxmXkaHFmSbuquMpaa3d88CuVvnEgJ1XksoqWpH6iLf?filename=SPORT_CAR.png",
    1: "https://ipfs.io/ipfs/QmU2rdiAR7wvhxzP1P7Q9LERFz38wSHuacJSYS2SLoS5a9?filename=HATCHBACK.png",
    2: "https://ipfs.io/ipfs/QmQQ8nP48gb2Z6ukMNw4tkmrGXoYdTCso3Db94J7buhLba?filename=SUV.png",
}

def prepare_contract_and_config():
    print("initializing")

    nft = project.load("../nft")
    print("project loaded")
    print(dict(nft))
    print("loading configs")
    FigaNFT = nft.FigaNFT
    print(FigaNFT)
    nft.load_config()
    
    print("config successfully loaded")


    ## Right after we choose a network the contract can map to deployments
    network.connect("kovan")
    print(f"connected on the {network.show_active()} network")

    print("accessing the latest deployment for this contract")
    print("at the address: ", FigaNFT[-1])
    print(dir(FigaNFT[-1]))
    figa_nft = FigaNFT[-1]
    return figa_nft


def get_user_account():
    prepare_contract_and_config()
    sender = accounts.add(config["wallets"]["from_key"])
    return sender


def create_a_collectible(car_model_number: int):
    try:
        print("initializing")

        nft = project.load("../nft")
        print("project loaded")
        print(dict(nft))
        print("loading configs")
        FigaNFT = nft.FigaNFT
        print(FigaNFT)
        nft.load_config()

        print("config successfully loaded")


        ## Right after we choose a network the contract can map to deployments
        network.connect("kovan")
        print(f"connected on the {network.show_active()} network")

        print("accessing the latest deployment for this contract")
        print("at the address: ", FigaNFT[-1])
        print(dir(FigaNFT[-1]))
        figa_nft = FigaNFT[-1]
        
        
        
        # get sender account
        sender = accounts.add(config["wallets"]["from_key"])

        # car_model_number = random.randint(0,2) randomized version
        print(car_model_number)
        transaction = figa_nft.createCollectible(car_metadata_dic[car_model_number], car_model_number, {"from": sender})
        print("Waiting on second transaction...")
        # wait for the 2nd transaction
        transaction.wait(1)
        time.sleep(1)
        token_id = transaction.events["requestedCollectible"]["tokenId"]
        print("tokenid",token_id)
        print(car_model_number)
        car = get_car(car_model_number)
        print(" car of tokenId {} is {}".format(token_id, car))
        network.disconnect()
        nft.close()
        return (sender, token_id, car)
        
    except Exception:
        print("could not create the collectible")
    
    
def check_minted_nfts():
    print("initializing")

    nft = project.load("../nft")
    print("project loaded")
    print(dict(nft))
    print("loading configs")
    FigaNFT = nft.FigaNFT
    print(FigaNFT)
    nft.load_config()
    print("config successfully loaded")
    ## Right after we choose a network the contract can map to deployments
    network.connect("kovan")
    print(f"connected on the {network.show_active()} network")
    print("accessing the latest deployment for this contract")
    print("at the address: ", FigaNFT[-1])
    print(dir(FigaNFT[-1]))
    figa_nft = FigaNFT[-1]
        
    sender = accounts.add(config["wallets"]["from_key"])
    
    number_of_figa_nfts = figa_nft.tokenCounter()
    network.disconnect()
    nft.close()
    return number_of_figa_nfts, sender.address

#def sync_db_entry(db: Session, db_index: int, figa_nft):
#    
#    number_of_figa_nfts = figa_nft.tokenCounter()
#    nft = db.query(models.NFTEntry).get(db_index)
#    owner = 0
#    while db_index < number_of_figa_nfts:
#        sync_db_entry(db_index)
#        
#        time.sleep(10)
#    nft.read_available = True
#    db.commit()
#    db.refresh(nft)
#    network.disconnect()
    
    

        
