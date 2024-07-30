class AnimalRegistry:
    def __init__(self):
        self.domestic_animals = []
        self.working_animals = []

    def add_domestic_animal(self, animal_type, commands):
        animal = DomesticAnimal(animal_type, commands)
        self.domestic_animals.append(animal)

    def add_working_animal(self, animal_type, commands):
        animal = WorkingAnimal(animal_type, commands)
        self.working_animals.append(animal)

    def list_commands(self, animal_type):
        if animal_type.lower() == 'domestic':
            for animal in self.domestic_animals:
                print(f"{animal.animal_type}: {animal.commands}")
        elif animal_type.lower() == 'working':
            for animal in self.working_animals:
                print(f"{animal.animal_type}: {animal.commands}")
        else:
            print("Unknown animal type.")

    def train_animal(self, animal_type, new_commands):
        if animal_type.lower() == 'domestic':
            for animal in self.domestic_animals:
                animal.train(new_commands)
        elif animal_type.lower() == 'working':
            for animal in self.working_animals:
                animal.train(new_commands)
        else:
            print("Unknown animal type.")

    def menu(self):
        while True:
            print("\n=== Animal Registry Menu ===")
            print("1. Add a new domestic animal")
            print("2. Add a new working animal")
            print("3. List commands for domestic animals")
            print("4. List commands for working animals")
            print("5. Train domestic animals with new commands")
            print("6. Train working animals with new commands")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                animal_type = input("Enter animal type: ")
                commands = input("Enter commands (comma-separated): ").split(',')
                self.add_domestic_animal(animal_type, commands)
            elif choice == '2':
                animal_type = input("Enter animal type: ")
                commands = input("Enter commands (comma-separated): ").split(',')
                self.add_working_animal(animal_type, commands)
            elif choice == '3':
                self.list_commands('domestic')
            elif choice == '4':
                self.list_commands('working')
            elif choice == '5':
                animal_type = input("Enter animal type to train: ")
                new_commands = input("Enter new commands (comma-separated): ").split(',')
                self.train_animal(animal_type, new_commands)
            elif choice == '6':
                animal_type = input("Enter animal type to train: ")
                new_commands = input("Enter new commands (comma-separated): ").split(',')
                self.train_animal(animal_type, new_commands)
            elif choice == '7':
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

class Animal:
    def __init__(self, animal_type, commands):
        self.animal_type = animal_type
        self.commands = commands

    def train(self, new_commands):
        self.commands.extend(new_commands)
        print(f"{self.animal_type} has learned new commands.")

class DomesticAnimal(Animal):
    def __init__(self, animal_type, commands):
        super().__init__(animal_type, commands)

class WorkingAnimal(Animal):
    def __init__(self, animal_type, commands):
        super().__init__(animal_type, commands)

# Пример использования программы:
if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.menu()