#!/usr/bin/python3
from brownie import FigaNFT, accounts, network, config
from scripts.helpful_scripts import fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract


def main():

    
    
    ###########

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:

        dev = accounts.add(config["wallets"]["from_key"])
        
        
        # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
        publish_source = True
        figa_nft = FigaNFT.deploy(
            {"from": dev},
            publish_source=publish_source,
        )
        # fund_with_link(figa_nft.address)
    
    else:
        figa_nft = FigaNFT.deploy(
           
            {"from": get_account()},
        )
        
        
    return figa_nft
