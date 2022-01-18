#!/usr/bin/python3
from brownie import FigaNFT
from scripts.helpful_scripts import fund_with_link


def main():
    figa_nft = FigaNFT[len(FigaNFT) - 1]
    fund_with_link(figa_nft.address)
