class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color: str = flower_color
        self.is_blooming: bool = True

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.flower_color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, flower_color: str, prize_points: int) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points: int = prize_points

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.flower_color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.total_growth: int = 0
        self.plants_added: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.plants_added += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(plant.get_info())
        print(
            f"Plants added: {self.plants_added}, "
            f"Total growth: {self.total_growth}cm"
        )


class GardenManager:
    gardens: list[Garden] = []

    class GardenStats:
        @staticmethod
        def validate_height(height: int) -> bool:
            return height > 0

        @staticmethod
        def calculate_score(garden: Garden) -> int:
            score: int = 0
            for plant in garden.plants:
                score += plant.height
            return score

        @staticmethod
        def count_plant_types(garden: Garden) -> tuple[int, int, int]:
            regular: int = 0
            flowering: int = 0
            prize: int = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    def add_garden(self, garden: Garden) -> None:
        GardenManager.gardens.append(garden)

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {len(cls.gardens)}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager: GardenManager = GardenManager()

    garden1: Garden = Garden("Alice")
    garden2: Garden = Garden("Bob")

    garden1.add_plant(Plant("Oak Tree", 100))
    garden1.add_plant(FloweringPlant("Rose", 25, "red"))
    garden1.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    garden1.grow_all()
    garden1.report()








