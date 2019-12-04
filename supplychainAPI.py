from flask import Response, json, Flask, request
import supplychain as sc, supplychainBC as bc
import supplychainUtility as scUtil
app = Flask(__name__)

grower = []
importer = []
shipper = []
trader_list = []
commodity_list =[]


@app.route('/add-trader', methods = ['POST'])
def create_participant():
    
    req_data = request.get_json()
    participant = sc.Participant(req_data['name'],req_data['balance'],req_data['type'])   
    
    if(participant.type == "grower"):
        trader_list.append(participant)
    
    if(participant.type == "importer"):
        trader_list.append(participant)
    
    if(participant.type == "shipper"):
        trader_list.append(participant)
    
    trader = scUtil.participant_to_json(participant)
    # print(bc.create_block(participant))
    # print(scUtil.search_participant(grower, "ashok"))
    
    return Response(bc.create_block(trader, "Added Participant"),status=201)

@app.route('/add-asset', methods = ['POST'])
def asset():
    
    req_data = request.get_json()  
    
    commodity = sc.Commodity(req_data['price'],req_data['quantity'],req_data['temp'],req_data['owner'])
    commodity_list.append(commodity)
    
    asset = scUtil.commodity_to_json(commodity)    
    
    return Response(bc.create_block(asset, "Added Asset") ,status=201)

@app.route('/transaction', methods = ['POST'])
def transaction():
    
    req_data = request.get_json()    
    # print(req_data['trader1'])
    trader1 = scUtil.search_participant(trader_list, req_data['trader1'])
    trader2 = scUtil.search_participant(trader_list, req_data['trader2'])
    commidity = scUtil.search_commodity(commodity_list, req_data['commodity'])    
    contract = sc.Contract(trader1, trader2, commidity, req_data['contract_name'])
    trader1_updated, trader2_updated = contract.rules()
    
    scUtil.update_participant(trader_list, req_data['trader1'], trader1_updated)
    scUtil.update_participant(trader_list, req_data['trader2'], trader2_updated)
    transfered_asset = scUtil.transfer_asset(commodity_list, req_data['commodity'], trader2_updated.id)
    bc.create_block(scUtil.commodity_to_json(transfered_asset), "Asset Transferred")
    print("trader1 -> "+ str(trader1_updated.balance))
    print("trader2 -> "+ str(trader2_updated.balance))   
    
    
    transaction = scUtil.transaction_to_json(sc.Transaction(req_data['trader1'], req_data['trader2'], req_data['commodity'], contract.id))    
    
    return Response(bc.create_block(transaction, "Added Transaction"), status=201)


@app.route('/fetch-asset', methods = ['GET'])
def fetch_asset():
    
    id = request.args.get("id") 
    print(id)
    result = scUtil.commodity_to_json(scUtil.search_commodity(commodity_list, id))
    
    return Response(result, status = 200) 


@app.route('/fetch-trader', methods = ['GET'])
def fetch_participant():
    
    id = request.args.get("id")
    # print(id)
    # print(scUtil.search_participant(trader_list, str(id)))
    result = scUtil.participant_to_json(scUtil.search_participant(trader_list, id))
    return Response(result, status = 200)    

@app.route('/fetch-blockchain', methods = ['GET'])
def fetch_blockchain():
    
    return Response(bc.send_blockchain(), status = 200)
    

if __name__ == '__main__':
    app.run(debug=True, port=8080) 