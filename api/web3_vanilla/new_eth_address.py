from eth_account import Account
import secrets

def create_account():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print("Game specific private key... this is for an optional wallet for you not to worry on exposing your assets from other wallets\n")
    print(f"pk: {private_key}")

    acct = Account.from_key(private_key)
    print("Address:", acct.address)
    return (private_key, acct.address)
create_account()