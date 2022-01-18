#!/usr/bin/python3
from brownie import FigaNFT, accounts, config,network
from scripts.helpful_scripts import get_car, fund_with_link
import time
import random

car_metadata_dic = {
    "SPORT_CAR": "https://ipfs.io/ipfs/QmeYxmXkaHFmSbuquMpaa3d88CuVvnEgJ1XksoqWpH6iLf?filename=SPORT_CAR.png",
    "HATCHBACK": "https://ipfs.io/ipfs/QmU2rdiAR7wvhxzP1P7Q9LERFz38wSHuacJSYS2SLoS5a9?filename=HATCHBACK.png",
    "SUV": "https://ipfs.io/ipfs/QmQQ8nP48gb2Z6ukMNw4tkmrGXoYdTCso3Db94J7buhLba?filename=SUV.png",
}


def main():
    network.connect('kovan')
    dev = accounts.add(config["wallets"]["from_key"])
    figa_nft = FigaNFT[len(FigaNFT) - 1]
    print("contract number: ",figa_nft.address)
    # fund_with_link(figa_nft.address) no need anymore
    car_model_number = random.randint(0,2)
    
    transaction = figa_nft.createCollectible(car_metadata_dic[car_model_number], car_model_number, {"from": dev})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    time.sleep(1)
    token_id = transaction.events["requestedCollectible"]["tokenId"]
    print("tokenid",token_id)
    car = get_car(car_model_number)
    print(" car of tokenId {} is {}".format(token_id, car))
