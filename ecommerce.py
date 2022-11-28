class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.purchases = [] #para guardar lo que ha comprado

    def purchase(self, inventory,product):
        inventory_dict = inventory.inventory
        #lo que hacemos aquí es: referenciar un objeto que ya tenemos
        #en otros puntos del código, referenciando al diccionario al que
        #pertenece.
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print('We are out of stock!')

        else:
        #si se va a poner esto, hay que evitar que esté en el mismo espacio
        #del otro else
            print("We don't have that product")

    def print_purchases(self):
        print("The customer has purchased: ")
        for item in self.purchases:
            print(item.name) #queremos saber el nombre de lo que ha comprado


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self,product,quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key,value in self.inventory.items():
            print(key.name + ':' + str(value))
        print()

######


customer = Customer('Joe','joe@gmail.com')
##print(customer.name)
##print(customer.email)

apple_watch = Product('Apple Watch', 299)
##print(apple_watch.name)
##print(apple_watch.price)

mac = Product('Mac', 1999)
##print(mac.name)
##print(mac.price)

inventory = Inventory() #habia olvidado los ()
inventory.add_product(apple_watch, 100)
##inventory.print_inventory()
inventory.add_product(mac,498)


#compras del cliente
inventory.print_inventory()
customer.purchase(inventory, apple_watch)
customer.purchase(inventory, mac)
inventory.print_inventory()
customer.print_purchases()
