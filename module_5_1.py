import random

class HOUSE:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print('Жилищный комплекс: ', self.name, '. Нужный этаж: ', new_floor)
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print('Этаж: ', floor)

h1 = HOUSE('ЖК Горский', 18)
h2 = HOUSE('Домик в деревне', 50)
h3 = HOUSE('ЖК Знак', 12)

h1.go_to(random.randint(0,60))
h2.go_to(random.randint(0,60))
h3.go_to(random.randint(0,60))