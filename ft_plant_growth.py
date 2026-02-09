if __name__ == "__main__":
    class plant:
        def __init__(self , name, height ,age):
            self.name = name
            self.height = height
            self.age = age
        def grow(self):
            self.height += 1
        def age_one_day(self):
            self.age += 1
        def get_info(self):
            print(self.name + ":", self.height, "cm,", self.age, "days old")
    rose = plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    start_height = rose.height
    for day in range(7):
     rose.grow()
     rose.age_one_day()

    print("=== Day 7 ===")
    rose.get_info()
    print("Growth this week: +" + str(rose.height - start_height) + "cm")