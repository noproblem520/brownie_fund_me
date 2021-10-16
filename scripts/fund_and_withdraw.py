from brownie import FundMe
from scripts.helpfulScripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    # print("Funding")
    # fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    fund()
    # withdraw()
