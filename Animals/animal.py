class Animal:
    def __init__(self, name):
        self.name = name
        self.commands = []

    def make_sound(self):
        pass

    def perform_command(self, command):
        if command in self.commands:
            return f"{self.name} follows the command: {command}"
        else:
            return f"{self.name} does not know the command: {command}"

    def add_command(self, new_command):
        self.commands.append(new_command)
