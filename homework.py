class Makeup():
    def __init__(self, applicator, category, how_many):
        self.applicator = applicator
        self.category = category
        self.how_many = how_many

    def showDetails(self):
        print("The applicator of this product is : ", self.applicator)
        print("The category of this product is : ", self.category)
        print("User has this number of the product : ", self.how_many)

f1 = Makeup( "spoolie", "lashes", 2)
f2 = Makeup( "stick", "cheekbones", "1")

f1.showDetails()

f2.showDetails()
