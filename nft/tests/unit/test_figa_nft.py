import pytest
from brownie import network, FigaNFT
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def test_can_create_figa_nft(
    get_keyhash,
    chainlink_fee,
):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    figa_nft = FigaNFT.deploy(
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        get_keyhash,
        {"from": get_account()},
    )
    get_contract("link_token").transfer(
        figa_nft.address, chainlink_fee * 3, {"from": get_account()}
    )
    # Act
    transaction_receipt = figa_nft.createCollectible(
        "None", {"from": get_account()}
    )
    requestId = transaction_receipt.events["requestedCollectible"]["requestId"]
    assert isinstance(transaction_receipt.txid, str)
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, 777, figa_nft.address, {"from": get_account()}
    )
    # Assert
    assert figa_nft.tokenCounter() > 0
    assert isinstance(figa_nft.tokenCounter(), int)
