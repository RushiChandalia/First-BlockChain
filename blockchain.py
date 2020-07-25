import datetime
import hashlib
import json

# initializing blockchain


class Blockchain:

    def __init__(self):
        self.chain = []
        self.createBlock(proof=1, previous_hash=0)

    # function for creating a block afer mining
    def createBlock(self, proof, previous_hash):
        block = {
            "index": len(self.chain + 1),
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "previoushash": previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):  # getting last block for previous hash
        return self.chain[-1]

# mining the block
