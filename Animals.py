class Animal:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date


class Pet(Animal):
    def __init__(self, name, birth_date, commands):
        super().__init__(name, birth_date)
        self.__commands = commands

    def get_commands(self):
        return self.__commands

    def learn_command(self, new_command):
        self.__commands.append(new_command)


class PackAnimal(Animal):
    def __init__(self, name, birth_date, load_capacity):
        super().__init__(name, birth_date)
        self.__load_capacity = load_capacity

    def get_load_capacity(self):
        return self.__load_capacity

