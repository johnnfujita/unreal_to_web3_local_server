#!/usr/bin/python3
from brownie import FigaNFT, accounts, network, config, interface
import json


def main():
    flatten()


def flatten():
    file = open("./FigaNFT_flattened.json", "w")
    json.dump(FigaNFT.get_verification_info(), file)
    file.close()
