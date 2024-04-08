class Drzava:
    def __init__(self, povrsina,ukupanBrojStanovnika):
        self.povrsina=povrsina
        self.ukupanBrojStanovnika=ukupanBrojStanovnika
    def IzracunajGustinu(self):
        return self.povrsina/self.ukupanBrojStanovnika
Drzava1 = Drzava(200000,210000)
Drzava2 = Drzava(2045000,223000)
Drzava3 = Drzava(120000,210356)

Gustina1 = Drzava1.IzracunajGustinu()
Gustina2 = Drzava2.IzracunajGustinu()
Gustina3 = Drzava3.IzracunajGustinu()
print("Gustina Drzave1 Je:",Gustina1)
print("Gustina Drzave2 Je:",Gustina2)
print("Gustina Drzave3 Je:",Gustina3)
print("A Najveca Gustina Je:",max(Gustina1,Gustina2,Gustina3))
