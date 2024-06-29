class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spots = [big, medium, small]
        

    def addCar(self, carType: int):
        if self.spots[(carType - 1)] - 1 >= 0:
            self.spots[(carType - 1)] -= carType
            return True
        else:
            return False

        
  

# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1,1,0)

#1 = big, 2 = med, 3 = small
param_1 = obj.addCar(2)

print(param_1)