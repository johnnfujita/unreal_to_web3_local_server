#!/usr/bin/python3
from brownie import FigaNFT, accounts, network, config
from metadata import sample_metadata
from scripts.helpful_scripts import get_car


def main():
    print(len(FigaNFT))
    print("Working on " + network.show_active())
    figa_nft = FigaNFT[len(FigaNFT) - 1]
    
    number_of_figa_nfts = figa_nft.tokenCounter()
    print(number_of_figa_nfts)
