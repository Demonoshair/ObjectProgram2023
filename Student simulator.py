import random

class Student:
    def __init__(self, name):
        self.happy=50
        self.progress=0
        self.name=name
        self.life=True
    def to_study(self):
        print("Time to study!")
        self.progress += 0.15
        self.happy -= 5
    def to_sleep(self):
        print("Time to sleep!")
        self.happy += 5
    def to_chill(self):
        print("Time to chill!")
        self.progress -= 0.1
        self.happy += 1.5
    def to_life(self):
        if self.happy<-0.5:
            print("depression...")
            self.life=False
        if self.progress<-0.5:
            print("student is very stupid...")
            self.life=False
        if self.progress>5:
            print("Passes externally...")
            self.life=False
    def end_of_day(self):
        print(f"Happy: {self.happy}")
        print(f"Progress: {round(self.progress,2)}")
    def alife(self, den):
        den ="den "+str(den)+" of "+self.name + " life"
        print(f"{den:=^50}")
        live_cube = random.randint(1,3)

        if live_cube==1:
            self.to_study()
        if live_cube==2:
            self.to_sleep()
        if live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.to_life()
egor=Student(name="Egor")

for day in range(1, 366):
    if egor.life==False:
        break
    egor.alife(day)