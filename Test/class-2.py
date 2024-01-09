
class Player :
    def __init__ (self) :
        self.fname = ""
        self.lname = ""
        self.number = ""

class Player2 :
    def __init__ (self, fname, lname, number) :
        self.fname = fname
        self.lname = lname
        self.number = number


p1 = Player()
p1.fname = "Woranuch"
p1.lname = "Pluengnuch"
p1.number = 11

p2 = Player()
p2.fname = "Phanu"
p2.lname = "Pluengnuch"
p2.number = 12 

p1a = Player2("Woranuch", "Pluengnuch", 11)
print(p1a.fname)
print(p1a.lname)
print(p1a.number)

print(p2.fname)



