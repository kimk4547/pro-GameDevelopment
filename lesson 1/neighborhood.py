#nok is number of kids
class Neighborhood():
    def __init__(self, nok, sport, hoa):
        self.nok = nok
        self.sport = sport
        self.hoa = hoa
        self.intro = " "

    def showDetails(self):
        print("The details of this family are : ")
        print("Number of Kids : ", self.nok)
        print("Sports : ", self.sport)
        print("Are the on the HOA? : ", self.hoa)
        print()

    def introNeighborhood(self):
        self.intro = input("Please introduce yourself : ")
        print(self.intro)

f1 = Neighborhood( 2, "volleyball and basketball", "yes")
f2 = Neighborhood( 0, "none", "no")

f1.showDetails()
f1.introNeighborhood()

f2.showDetails()
f2.introNeighborhood()
