from random import randint

class Car () :
 
    def start(self):
        print ("vroom vroom")
    def __init__ (self, year, CP):
        self.year = year
        self.CP = CP
    # def __repr__(self) -> str:
        # return "CP: "+str(self.CP)+" Year: "+str(self.year)
       
    
def factory ():
    ls = []
    for nr in range (100):
        CP = randint (90, 200)
        year = randint (1990, 2024)
        car = Car(year, CP)
        ls.append(car)
    return ls

factory()[2].start()
for nr in factory():
    print(nr)