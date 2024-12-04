class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name} не стал есть {food.name}, потому что это не растение")

    def __str__(self):
        return f"Animal(name={self.name}, alive={self.alive}, fed={self.fed})"

class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

    def __str__(self):
        return f"Plant(name={self.name}, edible={self.edible})"

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)

# Создание объектов и выполнение действий согласно примеру
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
