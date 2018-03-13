class Product(object):
    def __init__ (self, price, item_name, weight, brand):

        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def display(self):
        print "--------"+str(self.item_name)+"--------"
        print "Price: $"+str(self.price)
        print "Weight: "+str(self.weight)+" lbs"
        print "Brand: "+self.brand
        print "Status: "+self.status

    def sell(self):
        if self.status == "sold":
            print "!!Item has already been sold.!!"
        elif self.status == "defective":
            print "!!We can't sell this item because it has been deemed defective.!!"
        else:
            self.status = "sold"
            print "!!Item successfully sold!!"
        return self

    def add_tax(self, tax):
        self.tax = tax
        self.price *= 1+self.tax

        print "!!The price including sales tax is: $"+str(self.price)+"!!"

        return self

    def returns(self, reason):
        self.reason = reason

        if self.reason == "defective":
            self.price = 0
            self.status = "defective"
        elif self.reason == "unopened":
            self.status = "for sale"
        else:
            self.status = "used"
            self.price *= 0.8

        print "!!Item has been successfully returned as "+self.status+"!!"
        return self

bike = Product(3000,"Specialized SL2 Roubaix 2010 Dura-Ace",12,"Specialized")

bike.display()
bike.add_tax(0.1).returns("unopened").sell().display()