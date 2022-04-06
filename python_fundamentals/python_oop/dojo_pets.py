class Pet: 
    def __init__(self, name, type1, tricks, health, energy):
            self.name = name
            self.type1 = type1
            self.tricks = tricks
            self.health = health
            self.energy = energy
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self.energy, self.health

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("WOOF!")


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food): 
            self.first_name = first_name
            self.last_name = last_name
            self.pet = pet
            self.treats = treats
            self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self


tom = Pet('Tom', 'Cat', 'Spin', 0, 0)
kevin = Ninja('Kevin','Yu', tom, 'Candy', 'Chicken')

kevin.walk()
kevin.feed()
kevin.bathe()
print(tom.health)
print(tom.energy)