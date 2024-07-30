from home import Dog, Cat, Hamster
from pack import Horse, Camel, Donkey

class AnimalManager:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def change_animal_subclass(self, animal):
        print(f"Текущий класс для {animal.name}: {type(animal).__name__}")

        if isinstance(animal, Home):
            print("Текущая категория Home (Домашние животные)")
            new_subclass = input("Введите класс животного (dog, cat, hamster): ")

            if new_subclass == "dog":
                new_animal = Dog(animal.name)
            elif new_subclass == "cat":
                new_animal = Cat(animal.name)
            elif new_subclass == "hamster":
                new_animal = Hamster(animal.name)
            else:
                print(f"Несуществующий тип {new_subclass}.")
                return
        else:
            print("Текущая категория Pack (Вьючные животные)")
            new_subclass = input("Введите класс животного (horse, camel, donkey): ")

            if new_subclass == "horse":
                new_animal = Horse(animal.name)
            elif new_subclass == "camel":
                new_animal = Camel(animal.name)
            elif new_subclass == "donkey":
                new_animal = Donkey(animal.name)
            else:
                print(f"Недопустимый тип {new_subclass}.")
                return

        self.animals.remove(animal)
        self.add_animal(new_animal)
        print(f"{animal.name} был изменен на {new_subclass}.")

    def list_commands(self, animal):
        print(f"Доступные команды для {animal.name}:")
        if animal.commands:
            for command in animal.commands:
                print(command)
        else:
            print(f"{animal.name} не знает ни одной команды.")

    def train_animal(self, animal, new_command):
        print(f"Обучаем {animal.name} выполнять команду: {new_command}")
        animal.add_command(new_command)

    def display_menu(self):
        while True:
            print("\nМеню:")
            print("1. Добавить новое животное")
            print("2. Введите тип животного")
            print("3. Cписок команд, которое выполняет животное")
            print("4. Обучить животное новым командам")
            print("5. Выход")
            choice = input("Выберете пункт меню: ")

            if choice == "1":
                name = input("Введите кличку животного: ")
                animal_type = input("Введите категорию животного (Home or Pack):")
                if animal_type == "Home":
                    animal_subclass = input("Введите тип животного(dog, cat, hamster): ")
                    if animal_subclass == "dog":
                        animal = Dog(name)
                    elif animal_subclass == "cat":
                        animal = Cat(name)
                    elif animal_subclass == "hamster":
                        animal = Hamster(name)
                    else:
                        print("Несуществующий класс.")
                        continue
                elif animal_type == "Pack":
                    animal_subclass = input("Введите тип животного(horse, camel, donkey): ")
                    if animal_subclass == "horse":
                        animal = Horse(name)
                    elif animal_subclass == "camel":
                        animal = Camel(name)
                    elif animal_subclass == "donkey":
                        animal = Donkey(name)
                    else:
                        print("Несуществующий тип.")
                        continue
                else:
                    print("Несуществующий тип.")
                    continue
                self.add_animal(animal)
                print(f"{name} было добавлено как {animal_type} ({animal_subclass})")

            elif choice == "2":
                name = input("Введите кличку животного: ")
                for animal in self.animals:
                    if animal.name == name:
                        self.change_animal_subclass(animal)
                        break
                else:
                    print("Животное не найдено.")

            elif choice == "3":
                name = input("Введите кличку животного: ")
                for animal in self.animals:
                    if animal.name == name:
                        self.list_commands(animal)
                        break
                else:
                    print("Животное не найдено.")

            elif choice == "4":
                name = input("Введите кличку животного: ")
                new_command = input("Введите новую команду: ")
                for animal in self.animals:
                    if animal.name == name:
                        self.train_animal(animal, new_command)
                        break
                else:
                    print("Животное не найдено.")

            elif choice == "5":
                break

            else:
                print("Неверный выбор. Пожалуйста, выберите допустимый вариант.")

if __name__ == "__main__":
    manager = AnimalManager()
    manager.display_menu()
