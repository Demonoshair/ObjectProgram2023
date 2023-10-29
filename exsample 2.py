class vor:
    def __init__(self, name="Dio", dob="Televisor", ):
        self.name=name
        self.dob=dob
    def say_status(self):
        print(f"Hello, my name is {self.name}, and I stole {self.dob}")

vor1=vor("Egor", "Iphone")
vor2=vor()
vor3=vor("Kira", "Hand")

vor1.say_status()
vor2.say_status()
vor3.say_status()