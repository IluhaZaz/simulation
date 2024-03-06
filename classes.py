from abc import ABC, abstractmethod
from random import randint
from math import floor


MAX_STAT: int = 10

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
        self.creatures.append(obj)
    

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
        super().__init__(speed, hp, coord, sprite)

    def make_move(self, m: Map):
        pass


class Predator(Creature):
    def __init__(self, speed: int, hp: int, coord: Point, power:int,  sprite: str = "P"):
        super().__init__(speed, hp, coord, sprite)
        self.power = power

    def attack(self, obj: Herbivore, m: Map):
        obj.hp -= self.power
        if obj.hp <= 0:
            m.remove_obj(obj.coord)

    def make_move(self, m: Map):
        pass


class Render:
    def __init__(self, m: Map):
        self.map = m

    def draw(self):
        temp: list[Creature] = self.map.creatures
        temp = sorted(temp, key=lambda obj: (obj.coord.x, -1*obj.coord.y))

        for i in range(self.map.m):
            for j in range(self.map.n):
                if temp:
                    if Point(j, i) == temp[0].coord:
                        print(f"|{temp[0].sprite}|", end="")
                        temp.pop(0)
                        continue
                print("| |", end="")
            print("")
                

class Actions:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

                    
class Simulation:
    def __init__(self, width: int, height: int):
        self.map = Map(width, height)
        self.count = 0
        self.render = Render(self.map)

        self.init_actions = []
        self.turn_actions = []

    
    def next_turn(self) -> bool:
        self.count += 1
        flag: bool = 0
        for entity in self.map.creatures:
            if issubclass(entity.__class__, Creature):
                entity.make_move(self.map)
                flag = 1
        return flag
    
    @staticmethod
    def rand_point(m: int, n: int):
        return Point(randint(0, m), randint(0, n))
    

    def start_simulation(self):
        square: int = self.map.m*self.map.n
        #rock spawn
        for i in range(floor(square*0.1)):
            new_coord = self.rand_point(self.map.m - 1, self.map.n - 1)
            coords = [creature.coord for creature in self.map.creatures]
            if new_coord in coords:
                continue
            self.map.creatures.append(Rock(new_coord))

        #tree spawn
        for i in range(floor(square*0.15)):
            new_coord = self.rand_point(self.map.m - 1, self.map.n - 1)
            coords = [creature.coord for creature in self.map.creatures]
            if new_coord in coords:
                continue
            self.map.creatures.append(Tree(new_coord))

        #grass spawn
        for i in range(floor(square*0.2)):
            new_coord = self.rand_point(self.map.m - 1, self.map.n - 1)
            coords = [creature.coord for creature in self.map.creatures]
            if new_coord in coords:
                continue
            self.map.creatures.append(Grass(new_coord))
        
        #predator spawn
        for i in range(floor(square*0.1)):
            new_coord = self.rand_point(self.map.m - 1, self.map.n - 1)
            coords = [creature.coord for creature in self.map.creatures]
            if new_coord in coords:
                continue
            self.map.creatures.append(Predator(randint(1, floor(MAX_STAT/3)), randint(1, floor(MAX_STAT)), new_coord, randint(1, floor(MAX_STAT/2))))


        #while(self.next_turn()):
        #    continue

    def pause_simulation(self):
        pass  

s = Simulation(14, 14)
s.start_simulation()
s.render.draw()
