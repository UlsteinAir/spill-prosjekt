import pygame # Importerer Pygame-biblioteket (eks: pygame.display), som brukes for å lage enkle spill og grafiske applikasjoner 


# Klasse
class Fiende: # Oppskrift på fiende
    def __init__(self, x, y, fart):
        self.ramme = pygame.rect.Rect(x, y, 17, 17)
        self.ramme.centerx = x
        self.ramme.centery = y
        self.fart = fart

    def tegn(self, vindu):
        pygame.draw.ellipse(vindu, "red", self.ramme)

    def flyt(self):
        self.ramme.centerx += self.fart
        if self.ramme.centerx > 700 or self.ramme.centerx < 300:
            self.fart = self.fart * -1
        
# 1. Oppsett
pygame.init() # Starter Pygame-modulen (setter opp pygame). Dette må kalles før du bruker andre funksjoner fra Pygame 
BREDDE = 1000 # Setter bredden på vinduet til 1000px
HOYDE = 600 # Setter høyden på vinduet til 600px
FPS = 60 # Angir antall bilder per sekund (FPS) for animasjonen
vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Oppretter et vindu med gitt bredde og høyde og lagrer det i variabelen "vindu"
klokke = pygame.time.Clock() # Oppretter en klokke-objekt som hjelper med å regulere oppdateringshastigheten
font = pygame.font.SysFont("Arial", 44)

# /Bestemmer "ramme" sin posisjon og størrelse/
ramme_x = 284
ramme_y = 179
ramme_bredde = 430
ramme_hoyde = 162

# /Bestemmer "start" sin posisjon og størrelse/ 
start_x = 284
start_y = 341
start_bredde = 45
start_hoyde = 45

# /Bestemmer "slutt" sin posisjon og størrelse/
slutt_x = 669
slutt_y = 134
slutt_bredde = 45
slutt_hoyde = 45

# /Bestemmer "spiller" sin posisjon, størrelse og fart/ 
spiller_y_start = 348
spiller_x_start = 292
spiller_y = spiller_y_start
spiller_x = spiller_x_start
spiller_HOYDE = 26
spiller_BREDDE = 26
spiller_fart = 2

# Brukes til å holde styr på om spilleren er innenfor hovedområdet, startområdet eller sluttområdet
innenfor_hoved = False
innenfor_start = False
innenfor_slutt = False

# En liste med fiender blir opprettet med forskjellige startposisjoner og hastigheter
fiender = [
    Fiende(300, 200, 5),
    Fiende(700, 240, -5),
    Fiende(700, 320, -5),
    Fiende(300, 280, 5)
]

# Samler inn posisjon og størrelse for hvert område i en variabel (hoved, start og slutt)
hoved = ramme_x, ramme_y, ramme_bredde, ramme_hoyde
start = start_x, start_y, start_bredde, start_hoyde  
slutt = slutt_x, slutt_y, slutt_bredde, slutt_hoyde  

while True: # Starter en evig løkke, som er vanlig i spillprogrammering for å oppdatere og gjengi scenen hele tiden
    # 2. Håndter input
    for hendelse in pygame.event.get(): # Går gjennom alle hendelser i hendelseskøen
        if hendelse.type == pygame.QUIT: # Sjekker om en av hendelsene er av typen "QUIT" (for eksempel vinduet lukkes)
            pygame.quit() # Avslutter Pygame-modulen
            raise SystemExit # Avslutter programmet
        
    taster = pygame.key.get_pressed() # Henter tilstanden til alle tastene på tastaturet
    spiller_rektangel = pygame.Rect(spiller_x, spiller_y, spiller_BREDDE, spiller_HOYDE) # Oppretter et rektangel for spilleren

    # /Sjekker om spilleren kolliderer med hoved-, start- eller sluttområdet/
    if spiller_rektangel.colliderect(hoved):
        innenfor_hoved = True
    else:
        innenfor_hoved = False
        
    # /Sjekker om spilleren kolliderer med hoved-, start- eller sluttområdet/
    if spiller_rektangel.colliderect(start):
        innenfor_start = True
    else:
        innenfor_start = False

    # /Sjekker om spilleren kolliderer med hoved-, start- eller sluttområdet/
    if spiller_rektangel.colliderect(slutt):
        innenfor_slutt = True
    else:
        innenfor_slutt = False
    
    if innenfor_hoved: # Håndter bevegelser innenfor hovedområdet
        if taster[pygame.K_UP] and spiller_y - spiller_fart > ramme_y:
            print("Pil opp")
            spiller_y -= spiller_fart
        elif taster[pygame.K_UP] and spiller_x >= 669:
            print("Pil opp")
            spiller_y -= spiller_fart
        if taster[pygame.K_LEFT] and spiller_x - spiller_fart > ramme_x:
            print("Pil venstre")
            spiller_x -= spiller_fart
        if taster[pygame.K_RIGHT] and spiller_x + spiller_fart + spiller_BREDDE < ramme_x + ramme_bredde:
            print("Pil høyre")
            spiller_x += spiller_fart
        if taster[pygame.K_DOWN] and spiller_y + spiller_fart + spiller_HOYDE < ramme_y + ramme_hoyde:
            print("Pil ned")
            spiller_y += spiller_fart

    elif innenfor_start: # Håndter bevegelser innenfor startområdet
        if taster[pygame.K_UP]:
            print("Pil opp")
            spiller_y -= spiller_fart
        if taster[pygame.K_LEFT] and spiller_x - spiller_fart > start_x:
            print("Pil venstre")
            spiller_x -= spiller_fart
        if taster[pygame.K_RIGHT] and spiller_x + spiller_fart + spiller_BREDDE < start_x + start_bredde:
            print("Pil høyre")
            spiller_x += spiller_fart
        if taster[pygame.K_DOWN] and spiller_y + spiller_fart + spiller_HOYDE < start_y + start_hoyde:
            print("Pil ned")
            spiller_y += spiller_fart

    elif innenfor_slutt: # Håndter bevegelser innenfor sluttområdet
        print("Gratulerer, du har nådd målet!")
        pygame.quit()
        raise SystemExit
    
    else: # Håndter bevegelser utenfor alle områder
        if taster[pygame.K_UP] and spiller_y - spiller_fart > 0:
            print("Pil opp")
            spiller_y -= spiller_fart
        if taster[pygame.K_LEFT] and spiller_x - spiller_fart > 0:
            print("Pil venstre")
            spiller_x -= spiller_fart
        if taster[pygame.K_RIGHT] and spiller_x + spiller_fart + spiller_BREDDE < BREDDE:
            print("Pil høyre")
            spiller_x += spiller_fart
        if taster[pygame.K_DOWN] and spiller_y + spiller_fart + spiller_HOYDE < HOYDE:
            print("Pil ned")
            spiller_y += spiller_fart
    
    # 3. Oppdater spill
    for fiende in fiender: # oppdaterer fiendens posisjon ved å kalle "flyt-metoden"
        fiende.flyt() 
        if spiller_rektangel.colliderect(fiende.ramme): # sjekker om spilleren kolliderer med en fiende.
            spiller_x = spiller_x_start
            spiller_y = spiller_y_start
    
    # 4. Tegn
    vindu.fill("light blue") # Fyller vinduet med en bakgrunns farge (husk riktig rekkefølge)

    pygame.draw.rect(vindu, "grey", (ramme_x, ramme_y, ramme_bredde, ramme_hoyde)) # hoved
    pygame.draw.rect(vindu, "green", (start_x, start_y, start_bredde, start_hoyde)) # start
    pygame.draw.rect(vindu, "green", (slutt_x, slutt_y, slutt_bredde, slutt_hoyde)) # slutt

    pygame.draw.rect(vindu, "blue", (spiller_x, spiller_y, spiller_BREDDE, spiller_HOYDE)) # Tegner spilleren

    for fiende in fiender:
        fiende.tegn(vindu) # Tegner fiende
    
    tekst_world = font.render("World Trend", True, "black") # Lager teksten "World Trend" med den spesifiserte fonten
    vindu.blit(tekst_world, (420, 50)) # Teksten blir plassert på vinduet på koordinat (420, 50)

    pygame.display.flip() # Oppdaterer skjermen med endringene som er gjort i hver gjentakelse av løkken
    klokke.tick(FPS) # Kontrollerer oppdateringshastigheten ved å vente til det har gått riktig antall millisekunder siden forrige klokkesyklus. Dette sikrer at løkken kjører med riktig FPS
    