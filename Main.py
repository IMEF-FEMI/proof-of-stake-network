from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
import pprint
from AccountModel import AccountModel

if __name__ == '__main__':
    wallet = Wallet()
    accountModel = AccountModel()

    accountModel.addAccount(wallet.publicKeyString())
    accountModel.updateBalance(wallet.publicKeyString(), 10)
    accountModel.updateBalance(wallet.publicKeyString(), -5)
    pprint.pprint(accountModel.balances)
