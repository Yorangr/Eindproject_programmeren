from PIL import Image
#test
class Kaarten:
    def __init__(self, aantal, symbool, kleur, vulling):
        self.aantal = aantal
        self.symbool = symbool
        self.kleur = kleur
        self.vulling = vulling

    # kleur: 0 = red, 1 = green, 2 = purple
    # symbool: 0 = diamond, 1 = squiggle, 2 = oval
    # vulling: 0 = empty, 1 = filled, 2 = shaded
    # aantal: 0 = 1, 1 = 2, 2 = 3
    
    def bestandsnaam(self): #bestandsnaam van plaatje dat bij de kaart hoort
        gifje = ''
        if self.kleur == 0:
            gifje += 'red'
        elif self.kleur == 1:
            gifje += 'green'
        else:
            gifje += 'purple'
        if self.symbool == 0:
            gifje += 'diamond'
        elif self.symbool == 1:
            gifje += 'squiggle'
        else:
            gifje += 'oval'
        if self.vulling == 0:
            gifje += 'empty'
        elif self.vulling == 1:
            gifje += 'filled'
        else:
            gifje += 'shaded'
        if self.aantal == 0:
            gifje += '1'
        elif self.aantal == 1:
            gifje += '2'
        else:
            gifje += '3'
        gifje += '.gif'

        im = Image.open(gifje) 
        

        return im.show()

    def set(self,other,another):  #checken of een kaart een set is met twee andere kaarten    
        if (self.aantal==other.aantal==another.aantal or self.aantal!=other.aantal!=another.aantal)\
            and (self.symbool==other.symbool==another.symbool or self.symbool!=other.symbool!=another.symbool)\
            and (self.kleur==other.kleur==another.kleur or self.kleur!=other.kleur!=another.kleur)\
            and (self.vulling==other.vulling==another.vulling or self.vulling!=other.vulling!=another.vulling):
            return True
        else:
            return False

kaart1 = Kaarten(0, 0, 0, 0)
kaart2 = Kaarten(2, 2, 2, 2)
kaart3 = Kaarten(1, 1, 1, 1)

print(kaart1.vulling)
print(kaart1.bestandsnaam())
print(kaart1.set(kaart2,kaart3))