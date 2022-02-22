# Import classes from my brand new package
from animals import Mammals
from animals import Birds

# Create an object of Mammals class & call a method from it
myMammal = Mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method from it
myBird = Birds()
myBird.printMembers()