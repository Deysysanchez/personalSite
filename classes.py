class Dog():
    hungry= False
    breed= ""
    dirty=False
    friends= 0

    def play(self):
        self.hungry= True
        self.dirty= True
        self.friends +=1

    def eat(self):
        self.hungry=False
    def bathe(self):
        self.dirty=False
    def walk(self):
        slef.walk=True
#-----------------------------------------

ginger_bob_ross= Dog()

ginger_bob_ross.breed="husky"
ginger_bob_ross.play()
ginger_bob_ross.eat()

print("Ginger Bob Ross:")
print("hungry?" + str(ginger_bob_ross.hungry))
print("Breed:" + ginger_bob_ross.breed)
print("Dirty?" + str(ginger_bob_ross.dirty))
print("friends" + str(ginger_bob_ross.friends))

mike= Dog()
mike.breed= "Pomeranian"
mike.play()
mike.bathe()
mike.eat()

print("\nmike:")
print("hungry?" + str(mike.hungry))
print("Breed:" + mike.breed)
print("Dirty?" + str(mike.dirty))
print("friends" + str(mike.friends))


    #def eat(self):

    #def bathe(self):


    #def walk(self):
