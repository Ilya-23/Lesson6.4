class Figure:
    sides_count = 0
    color1 = True
    sides1 = False
    def __init__(self, __color, *args):
        self.__color = [*__color]
        self.filled = True
        self.__sides = []
        if len(args) == self.sides_count:
            for i in range(self.sides_count):
                self.__sides.append(args[i])
        elif len(args) == 1:
            for i in range(self.sides_count):
                self.__sides.append(args[0])
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and isinstance(r, int) is True\
            and isinstance(g, int) is True and isinstance(b, int) is True:
            self.color1 = True
        else:
            self.color1 = False

    def set_color(self, r, g, b):
        Figure.__is_valid_color(self, r, g, b)
        if self.color1 is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in range(len(args)):
                if isinstance(args[i], int) is True and args[i] > 0:
                    self.sides1 = True
                else:
                    self.sides1 = False
                    break
        else:
            self.sides1 = False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = sum(self.__sides)
        return P

    def set_sides(self, *new_sides):
        Figure.__is_valid_sides(self,*new_sides)
        if self.sides1 is True:
            for i in range(len(new_sides)):
                self.__sides[i] = new_sides[i]

class Circle(Figure):
    sides_count = 1

    def __radius(self):
        R = (self._Figure__sides[0])/(2 * 3.14)
        return R

    def get_square(self):
        S = 3.14 * (Circle.__radius(self) ** 2)
        return S

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = sum(self._Figure__sides) / 2
        S = (p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2])) ** 0.5
        return S

class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        V = self._Figure__sides[0] ** 3
        return V


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())








