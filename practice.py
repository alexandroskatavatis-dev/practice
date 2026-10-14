"""class car:
    def __init__(self,brand,color):
        self.brand= brand
        self.color=color

    def show_info(self):
        return f"this car is {self.brand}{self,model}"

my_car= car("toyoto","bleu")
print(my_car.brand)"""


class robot:
    def __init__(self,name,battery_level):
        self.name=name
        self.battery_level=battery_level
        
        self.mission_completed=0
    def do_misisions_costs(self,cost):
        self.cost=cost
        if self.battery_level<=self.cost:
            return "Mission failed: Low battery!"
        else:
            self.battery_level-=self.cost
            self.mission_completed+=1
            return"Misision succsfull"
    
        
robot1=robot("alpha",50)
print(robot1.do_misisions_costs(30))
print(robot1.do_misisions_costs(30))
print(robot1.battery_level)
print(robot1.mission_completed)
print("one more time")

print(robot1.battery_level)
print(robot1.mission_completed)