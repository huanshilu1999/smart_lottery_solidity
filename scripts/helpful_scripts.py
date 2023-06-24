from brownie import (
    accounts,
    network,
    config,
    MockV3Aggregator,
    Contract,
    VRFCoordinatorMock,
    LinkToken,
    interface
)
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["development", "mainnet-fork-dev"]
DECIMALS = 8
INITIAL_VALUE = 200000000000
# STARTING_PRICE = 200000000000


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


""" def depoly_mocks():
    print(f"Contract network is {network.show_active()}")
        #print(f"Contract deploy to {fund_me.address}")
    print("Deploying Mocks..... ")
    if len(MockV3Aggregator) <= 0:
         MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE,"ether"), {"from": get_account()}
        )
    print("Mocks Deployed! ") """
contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "vrf_coordinator": VRFCoordinatorMock,
    "link_token": LinkToken,
}


def get_contract(contract_name):
    """This function will grab the contract address from the brownie config
    if defined,otherwise,it will deploy a mock version of that contract,and
    return that mock contract.

    Args:
        contract_name(string)
    Returns:
        brownie.network.contract.ProjectContract: The most recently deployed
        version of this contract.
    """

    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks(decimals=DECIMALS, initial_value=INITIAL_VALUE):
    account = get_account()
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": account}
    )
    link_token = LinkToken.deploy({"from":account})
    VRFCoordinatorMock.deploy(link_token.address,{"from": account})
    print("Deployed!")

def fund_with_link(contract_address,account=None,link_token=None,amount=100000000000000000):#0.25
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")
    tx = link_token.transfer(contract_address,amount,{"from": account})
    #link_token_contract = interface.LinkTokenInterface(link_token.address)
    #tx = link_token_contract.transfer(contract_address,amount,{"from": account})
    tx.wait(1)
    print("Fund contract!")
    return tx

    


def main():
    get_account()
