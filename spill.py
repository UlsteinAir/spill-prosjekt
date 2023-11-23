import pygame # Importerer Pygame-biblioteket (eks: pygame.display), som brukes for å lage enkle spill og grafiske applikasjoner 

# Klasse
class Fiende: # Oppskrift på fiende 
    def __init__(self, x, y, fart):
        self.ramme = pygame.rect.Rect(x,y,17,17)
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

#rute_bredde = 35
#rute_hoyde = 35
spiller_y_start = 348
spiller_x_start = 292
spiller_y = spiller_y_start
spiller_x = spiller_x_start
spiller_HOYDE = 26
spiller_BREDDE = 26
spiller_fart = 2

fiender = [
    Fiende(300, 200, 5),
    Fiende(700, 240, -5),
    Fiende(700, 320, -5),
    Fiende(300, 280, 5)
]


while True: # Starter en evig løkke, som er vanlig i spillprogrammering for å oppdatere og gjengi scenen hele tiden
    # 2. Håndter input
    for hendelse in pygame.event.get(): # Går gjennom alle hendelser i hendelseskøen
        if hendelse.type == pygame.QUIT: # Sjekker om en av hendelsene er av typen "QUIT" (for eksempel vinduet lukkes)
            pygame.quit() # Avslutter Pygame-modulen
            raise SystemExit # Avslutter programmet
        
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("Pil opp")
        spiller_y -= spiller_fart
    if taster [pygame.K_LEFT]:
        print("Pil venstre")
        spiller_x -= spiller_fart
    if taster [pygame.K_RIGHT]:
        print("Pil høyre")
        spiller_x += spiller_fart
    if taster [pygame.K_DOWN]:
        print("Pil ned")
        spiller_y += spiller_fart
        
    # 3. Oppdater spill
    spiller_rektangel = pygame.Rect(spiller_x, spiller_y, spiller_BREDDE, spiller_HOYDE)
    for fiende in fiender:
        fiende.flyt()

        if spiller_rektangel.colliderect(fiende.ramme):
            spiller_x = spiller_x_start
            spiller_y = spiller_y_start

    # 4. Tegn
    vindu.fill("light blue") # fyller vinduet med en hvit bakgrunn (husk riktig rekefølge)
    
    # i liste:                         # (x, y, b, h)
    pygame.draw.rect(vindu, "grey", (284, 179, 430, 162))
    pygame.draw.rect(vindu, "green", (284,341,45,45)) # start
    pygame.draw.rect(vindu, "green", (669,134,45,45)) # slutt
    

    pygame.draw.rect(vindu, "blue", (spiller_x, spiller_y, spiller_BREDDE, spiller_HOYDE)) # Tegner spilleren

    for fiende in fiender: 
        fiende.tegn(vindu) # Tegner fiende

    tekst_world = font.render("World Trend", True, "black")
    vindu.blit(tekst_world, (420, 50))

    pygame.display.flip() # Oppdaterer skjermen med endringene som er gjort i hver gjentakelse av løkken
    klokke.tick(FPS) # Kontrollerer oppdateringshastigheten ved å vente til det har gått riktig antall millisekunder siden forrige klokkesyklus. Dette sikrer at løkken kjører med riktig FPS