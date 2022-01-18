#!/usr/bin/python3
from brownie import FigaNFT, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_car, OPENSEA_FORMAT


car_metadata_dic = {
    "SPORT_CAR": "https://ipfs.io/ipfs/QmeYxmXkaHFmSbuquMpaa3d88CuVvnEgJ1XksoqWpH6iLf?filename=SPORT_CAR.png",
    "HATCHBACK": "https://ipfs.io/ipfs/QmU2rdiAR7wvhxzP1P7Q9LERFz38wSHuacJSYS2SLoS5a9?filename=HATCHBACK.png",
    "SUV": "https://ipfs.io/ipfs/QmQQ8nP48gb2Z6ukMNw4tkmrGXoYdTCso3Db94J7buhLba?filename=SUV.png",
}

def main():
    print("Working on " + network.show_active())
    figa_nft = FigaNFT[len(FigaNFT) - 1]
    number_of_figa_nfts = figa_nft.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_figa_nfts)
    )
    for token_id in range(number_of_figa_nfts):
        car = get_car(figa_nft.tokenIdTocar(token_id))
        if not figa_nft.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, figa_nft,
                         car_metadata_dic[car])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
