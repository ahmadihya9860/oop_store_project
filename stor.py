from prodact import Product

class Stor:
    def __init__(self,name):
        self.name = name 
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
        print(f"the {product.name} add to the stor")
        
        
    def show_products(self):
        for i in self.products:
            print(f"{i.name} => {i.price}$")


phone = Product("iphone",500,2100)
laptob = Product("laptob",10000,200)
tv = Product("tv",210,20)
camira = Product("camira",1500,20)
# phone.show_info()
ahmad_stor = Stor("ahmad")

ahmad_stor.add_product(phone)
ahmad_stor.add_product(laptob)
ahmad_stor.add_product(tv)
ahmad_stor.add_product(camira)


ahmad_stor.show_products()

