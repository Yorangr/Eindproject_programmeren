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
        if self==other or self == another or other == another:
            return False
        elif (self.aantal==other.aantal==another.aantal or self.aantal!=other.aantal!=another.aantal!=self.aantal)\
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
def nieuwekaart(stapel,tafelkaarten):
    nieuw=tafelkaarten[0]
    while nieuw in tafelkaarten:
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



#pygame spel:-----------------------
#------------------------------------
pygame.init()
WIDTH, HEIGHT = 1250,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('set')



POKERGREEN=(0,153,0)

FPS=60

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


input_rect=pygame.Rect(820,100,140,32)
color=(255,255,255)




nummers=[]
for i in range(1,13):
    nummers.append(myfont.render(str(i), False, (255, 255, 255)))

# plaatjes=[]
# for i in range(len(tafelkaarten)):
#     plaatjes.append(pygame.image.load(tafelkaarten[i].plaatje()))

def draw_window(text_surface,invoer,submit,correct,kaart1,kaart2,kaart3,punten,compunten,text,info,tijd,kopietijd,moeilijkheid,computer):
    WIN.fill(POKERGREEN)
    
    if punten <10 and compunten <10:
        if submit:
            
            if kaart1.set(kaart2,kaart3) and int(kopietijd)!=0 and not computer:
                info = 'Goed gedaan, dat is een set!'
                #WIN.blit(myfont.render('Goed gedaan, dat is een set!',False,(255,255,255)),(810,200))
            elif not computer:
                info ='Helaas, dat is geen set'
                #WIN.blit(myfont.render('Helaas, dat is geen set',False,(255,255,255)),(810,200))
        
        ########
        WIN.blit(myfont.render('Timer: '+text, True, (255, 255, 255)), (820, 200))
        
        if info =='Helaas, dat is geen set' and int(text)>int(kopietijd)*0.75:
            WIN.blit(myfont.render(info, False, (255, 255, 255)), (820, 250))
        elif int(text)>tijd*0.75:
            WIN.blit(myfont.render(info, False, (255, 255, 255)), (820, 250))
        ###########
        
        WIN.blit(myfont.render('Jouw score: '+str(punten),False,(255,255,255)),(820,300))
        WIN.blit(myfont.render('Computer score: '+str(compunten),False,(255,255,255)),(820,350))
        
        if not moeilijkheid:
            WIN.blit(myfont.render('Voer hier een moeilijkheid in:',False,(255,255,255)),(820,10))
        else:
            WIN.blit(myfont.render('Voer hier een set in:',False,(255,255,255)),(820,10))
        pygame.draw.rect(WIN,color,input_rect,2)
        WIN.blit(text_surface,(input_rect.x+5,input_rect.y-5))
        input_rect.w=max(100,text_surface.get_width()+10)
        
        plaatjes=[]
        for i in range(len(tafelkaarten)):
            plaatjes.append(pygame.image.load(tafelkaarten[i].plaatje()))
        
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
    else:
        if punten >=10:
            winnaar= 'Je hebt gewonnen!'
            
        else:
            winnaar= 'De computer heeft gewonnen'
        WIN.blit(myfont.render(winnaar,False,(255,255,255)),(400,200))
    pygame.display.update()
    

  
def main():
    moeilijkheid=False
    user_text=''
    invoer=''
    submit=False
    correct=False
    kaart1=''
    kaart2=''
    kaart3=''
    punten=0
    compunten=0
    info=''
    kopietijd=0
    tijd=0
    eerstekeer=False
    computer=False
    ##########
    
    counter, text = tijd, str(tijd).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    ############
    
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
                    if not moeilijkheid:
                        
                        tijd = int(user_text)
                        moeilijkheid=True
                    
                    else:
                        submit=True
                        computer=False
                        invoer=user_text.split(',') #save user_text as invoer
                        
                        kopietijd=text
                           
                        kaart1=tafelkaarten[int(invoer[0])-1]
                        kaart2=tafelkaarten[int(invoer[1])-1]
                        kaart3=tafelkaarten[int(invoer[2])-1]
                        
                        if tafelkaarten[int(invoer[0])-1].set(tafelkaarten[int(invoer[1])-1],tafelkaarten[int(invoer[2])-1]):
                            for i in range(3):
                                tafelkaarten[int(invoer[i])-1]=nieuwekaart(stapel,tafelkaarten)                        
                            punten+=1
                            counter, text = tijd, str(tijd).rjust(3)
                    user_text = ""
                else:
                    user_text+=event.unicode
                ######
            if event.type == pygame.USEREVENT and moeilijkheid: 
                counter -= 1
                if counter >= 0:
                    text = str(counter).rjust(3)
                else:                   
                    counter, text = tijd, str(tijd).rjust(3)
                    if allesets(tafelkaarten)==[]:
                        info = 'Er waren geen sets'
                        for i in range(3):
                            tafelkaarten[i]=nieuwekaart(stapel,tafelkaarten)
                    else:
                        if eerstekeer:
                            info= 'Je was te langzaam'
                        
                            compunten+=1
                        
                            comset=eenset(tafelkaarten)
                            for i in range(3):                           
                                tafelkaarten[tafelkaarten.index(comset[i])]=nieuwekaart(stapel,tafelkaarten)
                            computer=True
                        eerstekeer=True
                        
                #text = str(counter).rjust(3) if counter > 0 else 'Je bent te langzaam'
                #######
        text_surface=myfont.render(user_text,True,(255,255,255))    
        draw_window(text_surface,invoer,submit,correct,kaart1,kaart2,kaart3,punten,compunten,text,info,tijd,kopietijd,moeilijkheid,computer)
        
    
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
        
        
    pygame.quit()
    sys.exit()

if __name__=='__main__':
    main()
    pygame.quit()
