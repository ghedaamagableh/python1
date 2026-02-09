if __name__ == "__main__":

    class Plant:
        def __init__(self, name, height, age):
            self.name = name
            self.height = height   # ← تصحيح الاسم
            self.age = age

        def get_info(self):
            print("Created:", self.name, "(" + str(self.height) + "cm,", str(self.age) + "days)")

    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []

    print("=== Plant Factory Output ===")

    for i in range(len(plants_data)):
        name, height, age = plants_data[i]
        plant = Plant(name, height, age)
        plants.append(plant)
        plant.get_info()

    print("Total plants created:", len(plants))


