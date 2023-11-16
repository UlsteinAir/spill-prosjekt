import pygame # Importerer Pygame-biblioteket (eks: pygame.display), som brukes for å lage enkle spill og grafiske applikasjoner 

# 1. Oppsett
pygame.init() # Starter Pygame-modulen (setter opp pygame). Dette må kalles før du bruker andre funksjoner fra Pygame 
BREDDE = 600 # Setter bredden på vinduet til 600px
HOYDE = 600 # Setter høyden på vinduet til 600px
FPS = 60 # Angir antall bilder per sekund (FPS) for animasjonen
vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Oppretter et vindu med gitt bredde og høyde og lagrer det i variabelen "vindu"
klokke = pygame.time.Clock() # Oppretter en klokke-objekt som hjelper med å regulere oppdateringshastigheten

while True: # Starter en evig løkke, som er vanlig i spillprogrammering for å oppdatere og gjengi scenen hele tiden
    # 2. Håndter input
    for hendelse in pygame.event.get(): # Går gjennom alle hendelser i hendelseskøen
        if hendelse.type == pygame.QUIT: # Sjekker om en av hendelsene er av typen "QUIT" (for eksempel vinduet lukkes)
            pygame.quit() # Avslutter Pygame-modulen
            raise SystemExit # Avslutter programmet
        
    # 3. Oppdater spill
    # 4. Tegn
    
    pygame.display.flip() # Oppdaterer skjermen med endringene som er gjort i hver gjentakelse av løkken
    klokke.tick(FPS) # Kontrollerer oppdateringshastigheten ved å vente til det har gått riktig antall millisekunder siden forrige klokkesyklus. Dette sikrer at løkken kjører med riktig FPS