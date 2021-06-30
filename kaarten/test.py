import random
import pygame
import sys


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
    
#plaatje dat bij de kaart hoort 
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

        return gifje
    
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

#x random kaarten voor op tafel
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
print(nieuwekaart(stapel).plaatje())


#pygame spel:-----------------------
#------------------------------------

WIDTH, HEIGHT = 1200,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('set')



POKERGREEN=(0,153,0)

FPS=60

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

user_text=''
input_rect=pygame.Rect(820,10,140,32)
color=pygame.Color('gray13')




nummers=[]
for i in range(1,13):
    nummers.append(myfont.render(str(i), False, (255, 255, 255)))

plaatjes=[]
for i in range(len(tafelkaarten)):
    plaatjes.append(pygame.image.load(tafelkaarten[i].plaatje()))

def draw_window(text_surface,invoer,submit):
    WIN.fill(POKERGREEN)
    
    if submit:
        if tafelkaarten[int(invoer[0])-1].set(tafelkaarten[int(invoer[1])-1],tafelkaarten[int(invoer[2])-1]):
            WIN.blit(myfont.render('Goed gedaan, dat is een set!',False,(255,255,255)),(810,200))
    
    pygame.draw.rect(WIN,color,input_rect,2)
    WIN.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    input_rect.w=max(100,text_surface.get_width()+10)

    WIN.blit(plaatjes[0], (10, 10))
    WIN.blit(plaatjes[1], (150,10))
    WIN.blit(plaatjes[2], (290,10))
    WIN.blit(plaatjes[3], (430,10))
    WIN.blit(plaatjes[4], (570,10))
    WIN.blit(plaatjes[5], (710,10))
    WIN.blit(plaatjes[6], (10,250))
    WIN.blit(plaatjes[7], (150,250))
    WIN.blit(plaatjes[8], (290, 250))
    WIN.blit(plaatjes[9], (430,250))
    WIN.blit(plaatjes[10], (570,250))
    WIN.blit(plaatjes[11], (710,250))
    
    WIN.blit(nummers[0],(50,205))
    WIN.blit(nummers[1],(190,205))
    WIN.blit(nummers[2],(330,205))
    WIN.blit(nummers[3],(470,205))
    WIN.blit(nummers[4],(610,205))
    WIN.blit(nummers[5],(750,205))
    WIN.blit(nummers[6],(50,450))
    WIN.blit(nummers[7],(190,450))
    WIN.blit(nummers[8],(330,450))
    WIN.blit(nummers[9],(470,450))
    WIN.blit(nummers[10],(610,450))
    WIN.blit(nummers[11],(750,450))
    pygame.display.update()


def main(user_text):
    invoer=''
    submit=False
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():          
            if event.type==pygame.QUIT:
                run=False
            ##    
            
            if event.type==pygame.KEYDOWN:
                
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    submit=True
                    invoer=user_text.split(',') #save user_text as invoer
                    user_text = ""
                else:
                    user_text+=event.unicode
            ##
        text_surface=myfont.render(user_text,True,(255,255,255))    
        draw_window(text_surface,invoer,submit)
        
    
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        
        
    pygame.quit()
    sys.exit()

if __name__=='__main__':
    main(user_text)
    pygame.quit()
