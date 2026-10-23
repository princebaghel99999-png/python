class car:
    def __init__(self,brand,model):
        self.model = model
        self.brand = brand

    def __str__(self):
        return f"{self.brand} {self.model}"


c1 = car("bmw","abc")
print(c1)