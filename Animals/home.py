from animal import Animal

class Home(Animal):
    def make_sound(self):
        pass

class Dog(Home):
    def make_sound(self):
        return "Woof!"

class Cat(Home):
    def make_sound(self):
        return "Meow!"

class Hamster(Home):
    def make_sound(self):
        return "Squeak!"
