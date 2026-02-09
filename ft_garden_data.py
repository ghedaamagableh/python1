if __name__ == "__main__":
    class Plant :
        def __init__(self , name , heigh , age) :
            self.name = name
            self.heigh = heigh
            self.age = age
        def display(self) :
                print(self.name + ":" , self.heigh , "cm" , self.age , "days old")


    print("=== Garden Plant Registry ===")
    plant1= Plant("Rose" , 25 , 30)
    plant2= Plant("Sunflower", 80, 45)
    plant3= Plant("Cactus", 15, 120)

    plant1.display()
    plant2.display()
    plant3.display()
    


