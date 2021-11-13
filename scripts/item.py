class item:
    def __init__(self, name, effect, info):
        self.name = name
        self.effect = effect
        self.info = info
        self.weapon = False

    #getters and setters:
    def get_name(self):
        return self.name

    def haveEffect(self, player):
        self.effect(player)
        
    
    def getInfo(self):
        return self.info

    def isWeapon(self):
        return self.weapon



######
# Make Map items:
####

#Map item use callback functions:
####Constitution:
def showConstitution(player):
    print("The Dems just laugh...")
####VaxCard:
def showVaxCard(player):
    print("This should fool 'em!")
    


####Vitamin D
def takeVitamins(player):
    if player.get_health()<80:
        player.takeDamage(-20)
    else:
        player.set_health(100)
    print("This has been shown to lower severity of COVID-19 symptoms. \nIt might help fight the vaccine too...")
    print(f"Your health is now: {player.get_health()}")

    
#### Mask:
def maskUp(player):
    player.takeDamage(10)
    print("You feel yourself start to get woozy from breathing your own CO2... \nYou lose 10 health before you rip off the mask, gasping for air")
    print(f"Your health is now: {player.get_health()}")

### Katana:

def slice(player):
    print('SHIIIING! You slice the blade through the air')

def shoot(player):
    print("BANG! You fire recklessly down the corridor")