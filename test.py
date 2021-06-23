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
        gifje = '._'
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


kaart1 = Kaarten(0, 2, 1, 2)
kaart2 = Kaarten(1, 2, 2, 2)
kaart3 = Kaarten(2, 0, 1, 1)

print(kaart1.vulling)
print(kaart1.bestandsnaam())