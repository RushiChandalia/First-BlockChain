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
            "previous_hash": previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):  # getting last block for previous hash
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2-previous_proof**2).encode).hexdigest
            if(hash_operation[:4]=='0000'):
                check_proof = True
            else:
                new_proof+=1
        return new_proof

    def hash_block(self,block):
        encoded_block = json.dumps(block, sort_keys=True).encode
        return hashlib.sha256(encoded_block).hexdigest

    def block_is_valid(self,chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if(block['previous_hash'] != self.hash_block(previous_block)):
                return False
            


    
# mining the block

