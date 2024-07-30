from animal import Animal

class Pack(Animal):
    def make_sound(self):
        pass

class Horse(Pack):
    def make_sound(self):
        return "Neigh!"

class Camel(Pack):
    def make_sound(self):
        return "Groan!"

class Donkey(Pack):
    def make_sound(self):
        return "Hee-haw!"
