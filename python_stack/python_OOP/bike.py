class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        self.logged = False

    def displayInfo(self):
        print "MSRP: $"+str(self.price)+"\n"+"Max Speed: "+str(self.max_speed)+"mph\n"+"Mileage: "+str(self.miles)+" miles"

    def ride(self):
        print("Riding...")
        self.miles += 10
        return self

    def reverse(self):
        if self.miles <5:
            print("Can't go back any further...")
            return self
        else:
            print("Reversing...")
            self.miles +- 5
            return self  


bike1 = Bike(2100, 5)
bike2 = Bike(1000, 5)
bike3 = Bike(50, 5)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()