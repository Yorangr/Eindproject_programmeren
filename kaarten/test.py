from PIL import Image
import random
import pygame

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
    
#plaatje dat bij de kaart hoort openen   
    def plaatje(self): 
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
    
#checken of een kaart een set is met twee andere kaarten
    def set(self,other,another):  
        if (self.aantal==other.aantal==another.aantal or self.aantal!=other.aantal!=another.aantal!=self.aantal)\
            and (self.symbool==other.symbool==another.symbool or self.symbool!=other.symbool!=another.symbool!=self.symbool)\
            and (self.kleur==other.kleur==another.kleur or self.kleur!=other.kleur!=another.kleur!=self.kleur)\
            and (self.vulling==other.vulling==another.vulling or self.vulling!=other.vulling!=another.vulling!=self.vulling):
            return True
        else:
            return False
        
    def __str__(self):
        return str((self.aantal,self.symbool,self.kleur,self.vulling))
    
    def __repr__(self):
        return str((self.aantal,self.symbool,self.kleur,self.vulling))

#stapel van alle mogelijke 81 kaarten
def stapel():
    stapel=[]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    stapel.append(Kaarten(i,j,k,l))
    return stapel

#nieuwe kaart trekken uit stapel
def nieuwekaart(stapel):
    nieuw=random.choice(stapel)
    return nieuw

#random kaarten voor op tafel
def tafelkaarten(x):
    tafelkaarten=random.sample(stapel, x)
    return tafelkaarten

#alle mogelijke sets van een stapel van aantal kaarten
def allesets(tafelkaarten):
    alle_sets=[] 
    for i in range(len(tafelkaarten)):
        for j in range(i+1,len(tafelkaarten)):
            for k in range(j+1,len(tafelkaarten)):
                if i!=j!=k!=i:
                    if tafelkaarten[i].set(tafelkaarten[j],tafelkaarten[k]):
                        alle_sets.append([tafelkaarten[i],tafelkaarten[j],tafelkaarten[k]])
    return alle_sets

#één set uit een stapel van aantal kaarten
def eenset(tafelkaarten):
    for i in range(len(tafelkaarten)):
        for j in range(i+1,len(tafelkaarten)):
            for k in range(j+1,len(tafelkaarten)):
                if i!=j!=k!=i:
                    if tafelkaarten[i].set(tafelkaarten[j],tafelkaarten[k]):
                        return [tafelkaarten[i],tafelkaarten[j],tafelkaarten[k]]
     
#test spel: -----------------------
#----------------------------------

stapel=stapel()
tafelkaarten=tafelkaarten(12)

print(stapel) 
print(nieuwekaart(stapel))  
print(allesets(tafelkaarten))
print(eenset(tafelkaarten))

#pygame spel:-----------------------
#------------------------------------
WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    
    run = True
    while run:
        for event in pygame.get():
            if event.type==pygame.QUIT:
                run=False
                
    pygame.quit()

if __name__=='__main__':
    main()