class Car:
    def __init__(self, maker, model, price):
        self.maker = maker
        self.model = model
        self.price = price
        

    def get_maker(self):
        return self.maker
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price


    


class Dealer:
    def __init__(self, address):
        self.address = address
        self.inventory = []

    def add_car(self):
        print('Adding a Car to the inventory')
        car_maker = input('Car Maker: ')
        model = input('Car Model: ')
        price = float(input('Car Price: '))
        car = Car(car_maker, model, price)
        self.inventory.append(car)

    def remove_car(self):
        print('Removing a car from the cart')
        car_model = input('Car Model: ')
        found = 'false'
        for car in self.inventory:
            if car.get_model() == car_model:
                print(car.get_model(), 'has been removed')
                self.inventory.remove(car)
                found = 'true'
        if found == 'false':
            print('This car is not in the inventory.')

    def inventory_list(self):
        for inventory in self.inventory:
            print ('Current Iventory:')
            print (inventory.get_maker(), inventory.get_model(),inventory.get_price())

    def updated_price(self):
        print('Update price for a model')
        car_model = input ('Model for update: ')
        new_price = float(input('New price: '))
        for car in self.inventory:
            if car.get_model() == car_model:
                car.get_price = new_price

        
        
def main():
    address = input('Dealer Address: ')
    dealer = Dealer(address)
    num_add = int(input('How many cars to add? '))
    for i in range(num_add):
        print('Car #', i+1, sep='')
        dealer.add_car()

    num_remove = int(input('How many cars to remove? '))
    for i in range(num_remove):
        dealer.remove_car()


    dealer.inventory_list()

    dealer.updated_price()

    dealer.inventory_list()





main()
        
            
        
        
                      

