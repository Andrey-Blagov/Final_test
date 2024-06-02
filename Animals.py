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




class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.get_name()} добавлен в реестр.")

    def list_commands(self, name):
        for animal in self.animals:
            if animal.get_name() == name:
                if isinstance(animal, Pet):
                    print(f"Команды {name}: {', '.join(animal.get_commands())}")
                else:
                    print(f"{name} не является домашним животным.")
                return
        print(f"{name} не найден в реестре.")

    def teach_command(self, name, new_command):
        for animal in self.animals:
            if animal.get_name() == name:
                if isinstance(animal, Pet):
                    animal.learn_command(new_command)
                    print(f"{name} обучен команде '{new_command}'.")
                else:
                    print(f"{name} не является домашним животным.")
                return
        print(f"{name} не найден в реестре.")


def main():
    registry = AnimalRegistry()
    
    while True:
        print("1. Завести новое животное")
        print("2. Показать список команд животного")
        print("3. Обучить животное новой команде")
        print("4. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            name = input("Введите имя животного: ")
            birth_date = input("Введите дату рождения животного (DD-MM-YYYY): ")
            animal_type = input("Домашнее или Вьючное: ").strip().lower()
            
            if animal_type == "домашнее":
                commands = input("Введите команды через запятую: ").split(",")
                registry.add_animal(Pet(name, birth_date, commands))
            elif animal_type == "вьючное":
                load_capacity = input("Введите грузоподъемность: ")
                registry.add_animal(PackAnimal(name, birth_date, load_capacity))
            else:
                print("Неправильный тип животного.")
        
        elif choice == '2':
            name = input("Введите имя животного: ")
            registry.list_commands(name)

        elif choice == '3':
            name = input("Введите имя животного: ")
            new_command = input("Введите новую команду: ")
            registry.teach_command(name, new_command)
        
        elif choice == '4':
            break

        else:
            print("Неправильный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()



class CounterException(Exception):
    pass


class Counter:
    def __init__(self):
        self.count = 0
        self.closed = False

    def add(self):
        if self.closed:
            raise CounterException("Счетчик закрыт!")
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.closed = True
        if exc_type:
            raise

    def __del__(self):
        if not self.closed:
            raise CounterException("Ресурс не был закрыт!")


try:
    with Counter() as counter:
        # Если добавлено новое животное и все поля заполнены
        counter.add()
        print(f"Текущее значение счетчика: {counter.count}")
except CounterException as e:
    print(e)
