from Crypto.Hash import SHA256
import json

class BlockchainUtils():

    @staticmethod
    def hash(data):
        datastring = json.dumps(data)
        dataBytes = datastring.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash