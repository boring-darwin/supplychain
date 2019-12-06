# supplychain
Supplychain using blockchain

This application demonstrates how blockchain can be used in supply-chain.

Trader: Who will buy or sell an asset.
Asset: Entity which will be transferred from one trader to another after the successful execution of the smart-contract.
Transaction: Contains information about the traders, asset.
Blockchain: Contains all the transactions related to the supply chain.

To run the code:
1. RUN supplychainAPI file using py supplychainAPI.py command
2. Use postman or insomnia to make an HTTP request to the app.

Add 1st trader:
POST: http://localhost:8080/add-trader
{
    "name": "jhon",
    "balance": 0,
    "type": "grower"
}

Add 2nd trader:
POST: http://localhost:8080/add-trader
{
    "name": "smith",
    "balance": 1000,
    "type": "importer"
}

Add an asset:
POST: http://localhost:8080/add-asset
{    
    "price":10,
    "quantity": 10,
    "temp": 20,
    "owner": "Trader-bf00"
}

Add a transaction
POST: http://localhost:8080/transaction
{
    "trader1":"Trader-bf00",
    "trader2":"Trader-3ab3",
    "commodity": "Asset-8f15",
    "contract_name":"test"    
}

Fetch Trader using Trader-id
GET: http://localhost:8080/fetch-trader?id=Trader-bf00

Fetch Asset using Asset-id
GET: http://localhost:8080/fetch-asset?id=Asset-8f15

Fetch Blockchain
GET: http://localhost:8080/fetch-blockchain
