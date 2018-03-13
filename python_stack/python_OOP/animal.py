class Animal(object):
    def __init__ (self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -=1
        print "Walked, health reduced by 1. Current Health = "+str(self.health)
        return self

    def run(self):
        self.health -=5
        print "Ran, health reduced by 5. Current Health = "+str(self.health)
        return self

    def displayHealth(self, text):
        print "--------------------------"
        print "Name: "+self.name
        print "Health: "+str(self.health)
        print "--------------------------"

class Dog(Animal):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health +=5
        print "Pet, health recovered by 5. Current Health = "+str(self.health)
        return self

class Dragon(Animal):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health -=10
        print "Flew, health decreased by 10. Current Health = "+str(self.health)
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth(text="I am a dragon")

ditto = Animal("Ditto",50)
ditto.displayHealth("An animal")

ditto.walk().walk().walk().run().run().displayHealth("An animal")

spot = Dog("Spot")

spot.walk().walk().walk().run().run().pet().displayHealth("A dog")

trogdor = Dragon("Trogdor")

trogdor.displayHealth()