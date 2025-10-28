

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantitiy = quantity
    
    
    def show_info(self):
        print(f"name {self.name}\nprice {self.price}\nquantity {self.quantitiy}")
    
    
    def buy(self,amount,quantity):
        
        if quantity > self.quantitiy:
            print(f"error we have just {self.quantitiy} {self.name}")
        
        elif amount < self.price:
            print(f"error your amount is short the price is {self.price}")
        
        else:
            
            print(f"you are buy the {self.name} by {self.price}")
            # print(f"the quantty is {self.quantitiy - quantity}")

