class Cake:
    recipe_typ = "Basic Cake"
    baking_temperature = 180
    baking_time = 30

    def __init__(self, flour, sugar, milk, eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_eggs = eggs

    def mix_ingredients(self):
        print(f"Mixing {self.cake_flour} grams of flour, {self.cake_sugar} grams of suger, {self.cake_eggs} eggs.")

    def bake(self):
        print(f"baking tha cake at {self.baking_temperature} `C for {self.baking_time} minutes.")

    def serve(self):
        print("Serving the cake with decoration.")

cake_1 = Cake(200,200,240,2)
cake_2 = Cake (200, 150, 220,2)
cake_3 = Cake (170, 170, 200, 2)

print (cake_1.cake_flour)
print (cake_2.baking_time)

