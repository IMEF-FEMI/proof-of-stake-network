from Crypto.PublicKey import RSA
from BlockchainUtils import BlockchainUtils
from Crypto.Signature import PKCS1_v1_5

class Wallet():
    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()
        

    @staticmethod
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(dataHash, publicKey)
        return signatureValid

    def publicKeyString(self):
        publicKeyString = self.keyPair.publicKey().exportKey("PEM").decode("utf-8")
        return publicKeyString

        