class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(1, "Частный дом")
building2 = Building(1, "Частный дом")
building3 = Building(9, "Многоэтажный дом")

print(building1 == building2)
print(building1 == building3)
