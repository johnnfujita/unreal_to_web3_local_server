#!/usr/bin/python3
import os
import requests
import json
from brownie import FigaNFT, network
from metadata import sample_metadata
from scripts.helpful_scripts import get_car
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

car_to_image_uri = {
    "SPORT_CAR": "https://ipfs.io/ipfs/QmeYxmXkaHFmSbuquMpaa3d88CuVvnEgJ1XksoqWpH6iLf?filename=SPORT_CAR.png",
    "HATCHBACK": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=HATCHBACK.png",
    "SUV": "https://ipfs.io/ipfs/QmU2rdiAR7wvhxzP1P7Q9LERFz38wSHuacJSYS2SLoS5a9?filename=HATCHBACK",
}


def main():
    print("Working on " + network.show_active())
    figa_nft = FigaNFT[len(FigaNFT) - 1]
    number_of_figa_nfts = figa_nft.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_figa_nfts)
    )
    write_metadata(number_of_figa_nfts, figa_nft)


def write_metadata(token_ids, nft_contract):
    for token_id in range(token_ids):
        collectible_metadata = sample_metadata.metadata_template
        car = get_car(nft_contract.tokenIdTocar(token_id))
        metadata_file_name = (
            "./metadata/{}/".format(network.show_active())
            + str(token_id)
            + "-"
            + car
            + ".json"
        )
        if Path(metadata_file_name).exists():
            print(
                "{} already found, delete it to overwrite!".format(
                    metadata_file_name)
            )
        else:
            print("Creating Metadata file: " + metadata_file_name)
            collectible_metadata["name"] = get_car(
                nft_contract.tokenIdTocar(token_id)
            )
            collectible_metadata["description"] = "An amazing {} model!".format(
                collectible_metadata["name"]
            )
            image_to_upload = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_path = "./img/{}.png".format(
                    car)
                image_to_upload = upload_to_ipfs(image_path)
            image_to_upload = (
                car_to_image_uri[car] if not image_to_upload else image_to_upload
            )
            collectible_metadata["image"] = image_to_upload
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)

# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = (
            os.getenv("IPFS_URL")
            if os.getenv("IPFS_URL")
            else "http://localhost:5001"
        )
        response = requests.post(ipfs_url + "/api/v0/add",
                                 files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = "https://ipfs.io/ipfs/{}?filename={}".format(
            ipfs_hash, filename)
        print(image_uri)
    return image_uri
