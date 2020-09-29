

class Fish:
    def __Init__(self, name="Fish"):
        self.name = name
        

    def swin(self):
        print("the fish can swim.")

class Trout(Fish):
    habitat = "Lake"
    Diet = "insects"



class Shark(Fish):
    bones = False
    eyesight = "excellent"


print(Fish)
