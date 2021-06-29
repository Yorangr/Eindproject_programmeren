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

WIDTH, HEIGHT = 850,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('set')

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = myfont.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = myfont.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, WIN):
        # Blit the text.
        WIN.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(WIN, self.color, self.rect, 2)

POKERGREEN=(0,153,0)

FPS=60

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

nummers=[]
for i in range(1,13):
    nummers.append(myfont.render(str(i), False, (255, 255, 255)))

plaatjes=[]
for i in range(len(tafelkaarten)):
    plaatjes.append(pygame.image.load(tafelkaarten[i].plaatje()))

# nieuwekaart=nieuwekaart(stapel).plaatje()
# plaatje=pygame.image.load(nieuwekaart)
def draw_window():
    WIN.fill(POKERGREEN)

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


def main():
    clock=pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():          
            if event.type==pygame.QUIT:
                run=False
                
        draw_window()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        WIN.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(WIN)

        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()

if __name__=='__main__':
    main()
    pygame.quit()
