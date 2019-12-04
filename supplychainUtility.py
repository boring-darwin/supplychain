import json


def search_participant(participantlist, search_id):
    
    for i in range(len(participantlist)):
        if  participantlist[i].id == str(search_id):
            return participantlist[i]

def update_participant(participantlist, update_id, trader):
    
    for i in range(len(participantlist)):
        if  participantlist[i].id == str(update_id):
            participantlist[i] = trader
            return participantlist[i]

def transfer_asset(commoditylist,asset_id, new_owner_id):
    for i in range(len(commoditylist)):        
        if  commoditylist[i].id == asset_id:
            commoditylist[i].owner = new_owner_id
            
            return commoditylist[i]
    
def search_commodity(commoditylist, id):
    
    for i in range(len(commoditylist)):        
        if  commoditylist[i].id == id:
            return commoditylist[i]
            # print("true")    


def participant_to_json(participant):
    
    dump = {
        "id": participant.id,
        "name": participant.name,
        "type": participant.type,
        "balance": participant.balance       
    }
    
    return json.dumps(dump)

def transaction_to_json(transaction):
    
    dump = {
        "id": transaction.id,
        "trader1": transaction.participant1,
        "trader2": transaction.participant2,
        "commodity": transaction.commodity,
        "contract": transaction.contract      
    }
    
    return json.dumps(dump)

def commodity_to_json(commodity):
    
    dump = {
        "id": commodity.id,
        "price": commodity.price,
        "quantity": commodity.quantity,
        "temp": commodity.temp,
        "owner": commodity.owner       
    }
    
    return json.dumps(dump)