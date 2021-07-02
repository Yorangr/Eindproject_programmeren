#import modules die nodig zijn voor de code
import random
import pygame
import sys

#Klasse kaarten om een abstracte versie van een kaart te genereren
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
    
#bestandsnaam dat bij kaart hoort genereren
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
        #de kaarten mogen niet gelijk aan elkaar zijn
        if self==other or self == another or other == another:
            return False
        #alle eigenschappen hetzelfde of allemaal verschillend
        elif (self.aantal==other.aantal==another.aantal or self.aantal!=other.aantal!=another.aantal!=self.aantal)\
            and (self.symbool==other.symbool==another.symbool or self.symbool!=other.symbool!=another.symbool!=self.symbool)\
            and (self.kleur==other.kleur==another.kleur or self.kleur!=other.kleur!=another.kleur!=self.kleur)\
            and (self.vulling==other.vulling==another.vulling or self.vulling!=other.vulling!=another.vulling!=self.vulling):
            return True
        else:
            return False
        
    #kaart weergeven in de terminal, is vooral handig voor testen    
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
    #zorgen dat de while loop wordt betreden:
    nieuw=tafelkaarten[0]
    #elke keer als nieuw al op tafel ligt, een andere kaart maken
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
                #alleen als de indices ongelijk zijn aan elkaar, checken dat het een set is met de set functie
                if i!=j!=k!=i:
                    if tafelkaarten[i].set(tafelkaarten[j],tafelkaarten[k]):
                        alle_sets.append([tafelkaarten[i],tafelkaarten[j],tafelkaarten[k]])
    return alle_sets

#één set uit een stapel van aantal kaarten
def eenset(tafelkaarten):
    for i in range(len(tafelkaarten)):
        for j in range(i+1,len(tafelkaarten)):
            for k in range(j+1,len(tafelkaarten)):
                #alleen als de indices ongelijk zijn aan elkaar, checken dat het een set is met de set functie
                if i!=j!=k!=i:
                    if tafelkaarten[i].set(tafelkaarten[j],tafelkaarten[k]):
                        #maar 1 set ipv een hele lijst zoals in allesets
                        return [tafelkaarten[i],tafelkaarten[j],tafelkaarten[k]]
     

#stapel maken
stapel=stapel()

#kaarten voor op tafel maken
tafelkaarten=tafelkaarten(12)

#pygame spel

pygame.init()

#breedte en hoogte van window
WIDTH, HEIGHT = 1250,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#naam van window
pygame.display.set_caption('set')


#kleur van achtergrond
POKERGREEN=(0,153,0)

#frames per second van spel
FPS=60

#lettertypes
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
extrafont = pygame.font.SysFont('Comic Sans MS', 17)

#rechthoek voor tekstvakje
input_rect=pygame.Rect(820,90,140,32)

#wit
color=(255,255,255)


#getallen 1 tot en met 12 voor onder de kaarten
nummers=[]
for i in range(1,13):
    nummers.append(myfont.render(str(i), False, (255, 255, 255)))


#functie voor het 'tekenen' van alle dingen die nodig zijn voor het spel
def draw_window(text_surface,invoer,submit,correct,kaart1,kaart2,kaart3,punten,compunten,text,info,tijd,kopietijd,moeilijkheid,computer,maximum):
    
    #achtergrond kleur
    WIN.fill(POKERGREEN)
    
    #stukje tekst voor onder aan het scherm
    WIN.blit(extrafont.render('(c) 2021 Tarik Tekeli en Yoran Grovenstein', False, (255,255,255)),(905,475))
    
    #aangeven tot hoeveel punten er wordt gespeeld 
    #alleen aangeven als de tijd en maximum score zijn ingevuld, dus als moeilijkheid == True
    if moeilijkheid:
        if maximum==1:
            WIN.blit(extrafont.render('De eerste die 1 punt heeft wint!', False, (255,255,255)),(820,400))
        else:
            WIN.blit(extrafont.render('De eerste die '+str(maximum)+' punten heeft wint!', False, (255,255,255)),(820,400))
    
    #timer tekst
    WIN.blit(myfont.render('Timer: '+text, True, (255, 255, 255)), (820, 200))
    
    #'helaas dat is geen set' verschijnt maar tot 75% van de tijd op het moment van invoeren
    if info =='Helaas, dat is geen set' and int(text)>int(kopietijd)*0.75:
        WIN.blit(myfont.render(info, False, (255, 255, 255)), (820, 250))
        
    #aangeven wie heeft gewonnen verschijnt niet als de tijd loopt
    elif (info =='De computer heeft gewonnen' or info == 'Je hebt gewonnen!') and int(text)>0:
        info=''
        
    #'goed gedaan, dat is een set' verschijnt alleen maar tot 75% van de tijd, het zal dus verdwijnen na een bepaalde tijd
    elif int(text)>=tijd*0.75:
        WIN.blit(myfont.render(info, False, (255, 255, 255)), (820, 250))

    #aangeven van score
    WIN.blit(myfont.render('Jouw score: '+str(punten),False,(255,255,255)),(820,300))
    WIN.blit(myfont.render('Computer score: '+str(compunten),False,(255,255,255)),(820,350))
    
    #gewenste tijd en maximum aantal punten alleen maar als moeilijkheid == False
    if not moeilijkheid:
        WIN.blit(myfont.render('Voer hier de gewenste tijd en',False,(255,255,255)),(820,10))
        WIN.blit(myfont.render('maximum aantal punten in:',False,(255,255,255)),(820,42))
    else:
        WIN.blit(myfont.render('Voer hier een set in:',False,(255,255,255)),(820,10))
    
    #tekstvakje 
    pygame.draw.rect(WIN,color,input_rect,2)
    WIN.blit(text_surface,(input_rect.x+5,input_rect.y-5))
    input_rect.w=max(100,text_surface.get_width()+10)
    
    #genereren van plaatjes voor op het scherm
    plaatjes=[]
    for i in range(len(tafelkaarten)):
        plaatjes.append(pygame.image.load(tafelkaarten[i].plaatje()))

    #kaarten op het scherm laten zien    
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

    #getallen op het scherm laten zien    
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
    
    #scherm updaten
    pygame.display.update()
    

#hoofdprogramma  
def main():
    
    #alle standaardwaardes van de gebruikte variabelen
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
    maximum=10^6
 
    #belangrijk voor de timer   
    counter, text = tijd, str(tijd).rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
 
    #FPS
    clock=pygame.time.Clock()
    
    #game loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            
            #variabelen gaan weer naar standaardwaardes als iemand heeft gewonnen
            if punten>=maximum or compunten>=maximum:
                moeilijkheid=False
                eerstekeer=False
                tijd=0
                counter, text = tijd, str(tijd).rjust(3)
                
                #info wordt aangepast
                if punten>=maximum:
                    info='Je hebt gewonnen!'
                else:
                    info='De computer heeft gewonnen'
                punten=0
                compunten=0
                maximum=10^6
                
            if event.type==pygame.QUIT:
                run=False
             
            #als een toets wordt ingedrukt, dan...
            if event.type==pygame.KEYDOWN:
                
                #als backspace wordt ingedrukt dan user_text tot één na laatste teken
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                    
                #als enter wordt ingedrukt
                elif event.key == pygame.K_RETURN:
                    
                    #als moeilijkheid ==False, dus als tijd en maximum score nog niet zijn ingevuld
                    if not moeilijkheid:
                        invoer=user_text.split(',')
                        tijd = int(invoer[0])
                        maximum=int(invoer[1])
                        moeilijkheid=True
                        
                    else:
                        submit=True
                        computer=False
                        invoer=user_text.split(',') #sla user_text op als invoer
                        
                        kopietijd=text
                        
                        #maak een kopie van de kaarten die zijn ingevuld, dit geeft anders problemen bij het veranderen van kaarten
                        kaart1=tafelkaarten[int(invoer[0])-1]
                        kaart2=tafelkaarten[int(invoer[1])-1]
                        kaart3=tafelkaarten[int(invoer[2])-1]
                        
                        #als het wel of niet een set is verander info
                        if kaart1.set(kaart2,kaart3) and int(kopietijd)!=0 and not computer:
                            info = 'Goed gedaan, dat is een set!'
                        else:
                            info ='Helaas, dat is geen set'
                            
                        #verander 3 kaarten en verhoog punten met 1, ook gaat de timer weer opnieuw
                        if tafelkaarten[int(invoer[0])-1].set(tafelkaarten[int(invoer[1])-1],tafelkaarten[int(invoer[2])-1]):
                            for i in range(3):
                                tafelkaarten[int(invoer[i])-1]=nieuwekaart(stapel,tafelkaarten)                        
                            punten+=1
                            counter, text = tijd, str(tijd).rjust(3)
                    
                    #tekstvak wordt leeg gehaald
                    user_text = ""
                else:
                    user_text+=event.unicode
                   
            #timer
            if event.type == pygame.USEREVENT and moeilijkheid: 
                counter -= 1
                if counter >= 0:
                    text = str(counter).rjust(3)
                else:                   
                    counter, text = tijd, str(tijd).rjust(3)
                    
                    #als er geen set is dan wordt info aangepast en veranderen we de eerste 3 kaarten
                    if allesets(tafelkaarten)==[]:
                        if eerstekeer:
                            info = 'Er waren geen sets'
                            for i in range(3):
                                tafelkaarten[i]=nieuwekaart(stapel,tafelkaarten)
                        eerstekeer=True
                    
                    #als de timer afloopt wordt de info aangepast, compunten verhoogt met 1.
                    else:
                        if eerstekeer:
                            info= 'Je was te langzaam'
                        
                            compunten+=1
                        
                            comset=eenset(tafelkaarten)
                            
                            #set van commputer wordt verandert naar 3 nieuwe kaarten
                            for i in range(3):                           
                                tafelkaarten[tafelkaarten.index(comset[i])]=nieuwekaart(stapel,tafelkaarten)
                            computer=True
                        eerstekeer=True
                                
        text_surface=myfont.render(user_text,True,(255,255,255)) 
        
        #draw_window aanroepen
        draw_window(text_surface,invoer,submit,correct,kaart1,kaart2,kaart3,punten,compunten,text,info,tijd,kopietijd,moeilijkheid,computer,maximum)
        
    
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
