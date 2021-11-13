import random
import os
class cell:
    """
    Base class for cells in the map.
    """
    def __init__(self, number, type, neighbors, item, effect):
        self.number = number
        self.neighbors = neighbors
        self.item = item
        self.type = type
        self.effect = effect
        self.passable = True
        self.visited = 0
    
    def set_item(self, item):
        self.item = item
    
    def get_item(self):
        return self.item

    def get_type(self):
        return self.type
    
    def get_effect(self):
        if self.effect:
            return self.effect
        else: 
            return None

    def set_passable(self, bool):
        self.passable = bool

    def get_passable(self):
        return self.passable

    def get_visited(self):
        return self.visited
    
    def set_visited(self, n):
        self.visited = n

    def about(self, world):
        print(f"You are in a {self.type}\n")

        for direction in self.neighbors:
            if self.neighbors[direction]:
                Direction = direction.capitalize()
                print(f"[{Direction}] there is a {world[self.neighbors[direction]].get_type()}\n")
        if self.item:
            print(f"There is a [{self.item.name}] in the corner.\n")
    def start(self, world):
        self.about(world)

##Effect callback functions for different cells:

#sword:
def showSword(player):
    with open('sword.txt') as file:
        for line in file.readlines():
            print(line, end="")  

#gun:
def showGun(player):
    with open('gun.txt') as file:
        for line in file.readlines():
            print(line, end="")  


def vaccination(player):   
    if player.get_location().get_visited() == 0:
         player.get_location().set_visited(player.get_location().get_visited()+1)
         player.get_location().set_passable(False)
    print()
    print('A Male nurse sees you walk in. He barks at his orderlies to grab you.\n')
    print('A Female doctor stands in the shadows. She asks for your papers.')
    if not player.get_location().get_passable():
        print('They have you right where they want you. What do you do?')
        action = input()
        action = player.parseCommand(action)
        if "vaxcard" in action and "vaxcard" in player.items.keys():

            print("You scream \"Here! Take my papers! Please don't give me the shot!\"\n They laugh as they take your vaccine card and kick you to the ground.\n")
            print('You fooled them. Get out of here before they realize it was a fake!')
            input()
            return
        elif "vaxcard" in action:
            print("If only you had a conterfeit vaccination record to show them!\n")
        elif "constitution" in action:
            print("You wave the constitution in their faces, screaming about your right to privacy.\n")
            print("The Dems just laugh...\n")
        elif set.intersection(set(action), set(player.goCommands)):
            print("You're stuck!")
        print("One of the surlier male nurses grabs a long, rusty syringe filled with a noxious green fluid...")
        input()
        print("You try to wriggle free, but they have you pinned tighter than a noose on hanging day\n")
        print("As the needle pierces your skin, you scream.\n")
        player.takeDamage(40)
            #player.getItem(vaxcard)
        print(f"You've been vaccinated. Your health is now {player.get_health()}")
        player.location.set_passable(True)
        input()
        
    else:
        print('\nQUENTIN: "I know my rights!"')
        print('\nThe gender fluid medical team eyes you hungrily from the shadows as you run past them.')
        input()
    player.location.set_passable(True)
 
 #hippies battle   
def hippies(player):
    def lose():
        player.takeDamage(10)
        print('The beggars surround you, and give you a vigorous thrashing\n')
        print('Luckily, their socialistic apathy and lack of work ethic saves you, and they walk away\n')
        print(f'Your health is now {player.get_health()}')
        
    def win():
        print('You gave them a solid thrashing. They\'ll think again before they try to get a handout from Quentin Thomas')

    if player.get_location().get_visited() == 0:
        player.get_location().set_visited(True)
            
        print('You smell an overpowering stench of patchouli oil... What could it be?')
        input()
            
        print('From out of nowhere, a roving band of burnout druggy beggars ambushes you!\n')
        print('They\'ve grown fat and week from a lifetime of Newsom\'s handouts. You can probably take them out. \n')
        print('What do you do?')
        action = input()
        action = player.parseCommand(action)

        if action[0] in player.goCommands or action[0] in player.directions:
            print("Whew! It looks like you left them in the dust.")
            input()
            
        elif action[0] in ["use", "u"]: 
            if len(action) > 1:

                item = action[1]
            else:
                print("What do you want to use?")
                print([key for key in player.items.keys()], sep = "  ")
                item = input()
            if item not in player.items.keys():
                player.use(item)
                lose()
            else:
                player.use(item)
                if not player.items[item].isWeapon():
                    lose()
                else:
                    win()
        else:
            print('You wasted too much time')
            lose()


#Newsom Battle                   
def newsom(player):
    newsomHealth = 50
    constitution = False
    def intro():
        print("\nYou enter the throne room. Across the cavernous space, a leather chair faces out\n away from you towards the massive windows\n")
        print("From up here you can see the whole state. Its a wasteland. Tent cities stretch out past the horizon.\nThe Montecito country club is a pile of rubble, now used only as housing for immigrants.")
        print("This is it. The most important moment of your life. A chance to kill Gavin Newsom.\n")
        input()
        print("From across the room comes a soft chuckle, slowly building to a crescendo of cruel laughter\nGavin Newsom slowly turns to face you.")
        print("The smoke from his Cuban cigar wafts past his slicked-back hair.")
        print("GAVIN: 'Did you really think you ever had a chance, Quentin?'")
        input()
        print("QUENTIN:'As long as I have my rights, there's always a chance!'")
        input()
        print("GAVIN: HA! Your rights? Your rights come by consent of the government, dear, sweet, STUPID Quentin.")
        input()
        print("GAVIN: And they've just been REVOKED!")
        
        
    def lose():
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('gameOver.txt') as file:
            for line in file.readlines():
                print(line, end="")  
        quit()

    def win():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Today, liberty defeated tyranny! God Bless America!')
        quit()

    def fightLoop(player, newsomHealth, constitution):
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------------------------------')
        print()
        
        
        #Take Damage:
        damage = random.randint(10, 30)
        
        print(f'Newsom deals a savage blow! you take {damage} damage!')
        player.takeDamage(damage)
        print(f'Your health is {player.get_health()}\n')
        print("There's no turning back now, what are you going to use?")
        item = input().lower()
        #check if item is in items:
        command = item.split(" ")
        if len(command) > 1:
            if item.split(" ")[0] == "use":
                item = command[1]
        elif command[0] in ["back", "b", "go", "g", "f", "forward", "left", "right"]:
                print("GAVIN: You're not going anywhere!\n")  
                fightLoop(player, newsomHealth, constitution)
        while item not in player.items.keys():
            print("No time for this! What item are you going to use?!")
            print([item for item in player.items.keys()])
            item = input().lower()

        #Parse action:
        if item == 'constitution':
            constitution = True
            print('Your berating has weakened his gun control laws!')
            
        elif item == 'gun':
            if constitution == False:
                print("It's no use, his tyrannical gun control laws are too strong!")
                
            else:
                print('Bullseye! Thank god for good guys with guns!')
                damage = random.randint(5, 40)
                newsomHealth -= damage
                print(f'Newsom takes {damage} damage. He has {newsomHealth} health.')
                input()
                
        elif item == 'katana':
            damage = 20
            newsomHealth -= damage
            print("SAAAAAAAAAAAIT!!!")
            print('Newsom takes 20 damage')  
            print(f'Newsom\'s health is how {newsomHealth}')  
            
        elif item == 'vitamind':
            player.takeDamage(-20)
            print(f"You feel rejuvenated by the Vitamin D. Your health is now {player.get_health()}.")
             
        else:
            print("The item has no effect! Newsom just keeps smirking.")   
        
        if newsomHealth <1:
            win()
        if player.get_health() < 1:
            lose()
        fightLoop(player, newsomHealth, constitution)
    
    
    intro()
    fightLoop(player, newsomHealth, constitution)

def showCastle(player):
    with open('castle.txt') as file:
        [print(line, end="") for line in file.readlines()]
    
    

