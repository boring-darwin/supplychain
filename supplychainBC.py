import hashlib, json



blockchain = []
perv_hash = "None"
# Creating a Hash for content
def create_hash(participant):
    hash = str(hashlib.sha256(participant.__str__().encode()).hexdigest())
    return hash


def create_block(participant, type):
    
    global perv_hash
    hash = create_hash(participant)
    block = {
        "participant": participant,
        "type": type,
        "hash": hash,
        "prev_hash": perv_hash
    }
    
    
    blockchain.append(block)
    print("length"+ str(len(blockchain)))
    print(block)
    perv_hash = hash
    
    return json.dumps(block)

def send_blockchain():
    
    return json.dumps(blockchain)
def test():
    return "test"