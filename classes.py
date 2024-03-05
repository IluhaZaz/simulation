from abc import ABC, abstractmethod

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, value: object) -> bool:
        return self.x == value.x and self.y == value.y

class Entity(ABC):
    def __init__(self, coord: Point, sprite: str):
        self.coord = coord
        self.sprite = sprite


class Grass(Entity):
    def __init__(self, coord: Point, sprite = "G"):
        super().__init__(coord, sprite)


class Rock(Entity):
    def __init__(self, coord: Point, sprite = "R"):
        super().__init__(coord, sprite)


class Tree(Entity):
    def __init__(self, coord: Point, sprite = "T"):
        super().__init__(coord, sprite)

class Creature:
    pass

class Map:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.creatures: list[Creature|Entity] = []
    

    def add_obj(self, obj: Creature|Entity):
        self.creatures.append[obj]
    

    def remove_obj(self, coord: Point):
        for i in range(len(self.creatures)):
            if self.creatures[i].coord == coord:
                self.creatures.pop(i)
                break



class Creature(ABC):
    def __init__(self, speed: int, hp: int, coord: Point, sprite: str):
        self.speed = speed
        self.hp = hp
        self.coord = coord
        self.sprite = sprite

    @abstractmethod
    def make_move(self, m: Map):
        pass


class Herbivore(Creature):
    def __init__(self, speed: int, hp: int, coord: Point, sprite: str = "H"):
        super().__init__(coord, speed, hp, sprite)


class Predator(Creature):
    def __init__(self, speed: int, hp: int, coord: Point, power:int,  sprite: str = "P"):
        super().__init__(coord, speed, hp, sprite)
        self.power = power

    def attack(self, obj: Herbivore, m: Map):
        obj.hp -= self.power
        if obj.hp <= 0:
            m.remove_obj(obj.coord)


class Render:
    def __init__(self, m: Map):
        self.map = m

    def draw(self):
        temp = self.map.creatures
        temp = sorted(temp, lambda obj: (obj.coord.x, obj.coord.y))

        for i in range(self.map.m):
            for j in range(self.map.n):
                

