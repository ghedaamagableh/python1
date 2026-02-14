if __name__ == "__main__":

    class Plant:
        def __init__(self, name: str, height: int, age: int) -> None:
            self.name: str = name
            self.height: int = height
            self.age: int = age

    class Flower(Plant):
        def __init__(self, name: str, height: int, age: int, color: str) -> None:
            super().__init__(name, height, age)
            self.color: str = color

        def bloom(self) -> None:
            print(f"{self.name} is blooming beautifully!")

    class Tree(Plant):
        def __init__(self, name: str, height: int, age: int, trunk_diameter: float) -> None:
            super().__init__(name, height, age)
            self.trunk_diameter: float = trunk_diameter

        def produce_shade(self) -> None:
            shade_area: float = self.trunk_diameter * 1.5
            print(f"{self.name} provides {shade_area} square meters of shade")

    class Vegetable(Plant):
        def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
        ) -> None:
            super().__init__(name, height, age)
            self.harvest_season: str = harvest_season
            self.nutritional_value: str = nutritional_value

        def describe(self) -> None:
            print(f"{self.name} is rich in {self.nutritional_value}")

    print("=== Garden Plant Types ===")

    rose: Flower = Flower("Rose", 25, 30, "red")
    tulip: Flower = Flower("Tulip", 20, 25, "yellow")

    oak: Tree = Tree("Oak", 500, 1825, 50)
    pine: Tree = Tree("Pine", 400, 1500, 40)

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot: Vegetable = Vegetable("Carrot", 30, 60, "spring", "vitamin A")

    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()

    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()

    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.describe()


                 