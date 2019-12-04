import uuid

class Participant:
    
    id = None
    name = None
    type = None
    balance = None

    def __init__(self, name, balance, type):
        
        self.id =  "Trader-" + str(uuid.uuid4().hex[:4])
        self.name = name
        self.balance = balance
        self.type = type

    def __str__(self):
        return str(self.id)+" "+str(self.balance)+" "+str(self.type)


class Commodity:

    id = None
    price = None
    quantity = None
    temp = None
    owner = None

    def __init__(self, price, quantity, temp, trader_id):

        self.id = "Asset-"+str(uuid.uuid4().hex[:4])
        self.price = price
        self.quantity = quantity
        self.temp = temp
        self.owner = trader_id

    def __str__(self):
        return str(self.id)+" "+str(self.price)+" "+str(self.quantity)


class Contract:

    id = None
    trader1 = Participant
    trader2 = Participant
    commodity = Commodity
    contractName = None

    def __init__(self, trader1, trader2, commodity, contract_name):

        self.id = "Contract-"+str(uuid.uuid4().hex[:4])
        self.trader1 = trader1
        self.trader2 = trader2
        self.commodity = commodity
        self.contractName = contract_name

    def rules(self):
        
        if self.contractName == "test":

            if self.commodity.temp >= 10 and self.commodity.temp <= 25:
                amount = self.commodity.price * self.commodity.quantity
                self.trader2.balance -= amount
                self.trader1.balance += amount
                print("Done with balance transfer")

            else:
                amount = self.commodity.price * self.commodity.quantity * 0.50
                self.trader2.balance -= amount
                self.trader1.balance += amount
                print("Done with balance transfer")
        
        return self.trader1, self.trader2
    def __str__(self):
        return str(self.id)+" "+str(self.trader1.name)+" "+str(self.trader2.name) + " "+str(self.commodity.owner)


class Transaction:

    id = None
    participant1 = None
    participant2 = None
    commodity = None
    contract = None

    def __init__(self, participant1_id, participant2_id, commodity_id, contract_id):

        self.id = "Transaction-"+ str(uuid.uuid4().hex[:4])
        self.participant1 = participant1_id
        self.participant2 = participant2_id
        self.contract = contract_id
        self.commodity = commodity_id

        def __str__(self):

            return str(self.id)+" "+str(self.participant1.id)+" "+str(self.participant2.name) +" "+str(self.commodity.id) +" "+ str(self.contract.id)

# par1 = Participant("abc", 0, "dist")
# par2 = Participant("xyz", 2000, "Producer")

# com = Commodity(300, 390, 10, par1)

# print(par1.id)

# trans = Transaction(par1, par2, 300, 2, "buying")

# par1, par2 = trans.contract_excecution()

# print(par1, par2)
