from PIL import Image
import random
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
    
    def plaatje(self): #plaatje dat bij de kaart hoort openen
        gifje = '../kaarten/'
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

#stapel van alle mogelijke 81 kaarten
stapel=[]
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                stapel.append(Kaarten(i,j,k,l))

twaalf_kaarten=random.sample(stapel, 12) #12 random kaarten


print(twaalf_kaarten)
print(stapel[0].vulling)
stapel[0].plaatje()
print(stapel[0].set(stapel[1],stapel[2]))