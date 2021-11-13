import string
from cell import cell
import os
class Player:
    
    items = {}
    
    commands = ["go",
                "g",
                "run",
                "walk",
                "w",
                "forward",
                "back",
                "left",
                "right",
                "f",
                "b",
                "look",
                "use",
                "u",
                "take",
                "t",
                "help",
                "quit",
                "health"
                ]
    
    goCommands = ["go",
                "g"
                "run",
                "walk",
                "w",
                "forward",
                "f"]
    
    directions = ["forward",
                "back",
                "left",
                "right",
                "f",
                "b",]
    
    location = None
    
    neighbors = { "left" : None,
                "right" : None,
                "forward" : None,
                "back" : None}




    def __init__(self, location, world, goCommands = goCommands, directions = directions, commands = commands) -> None:
        self.location = location
        self.neighborsDictionary = location.neighbors
        self.neighbors = {}
        for key in self.neighborsDictionary:
            if self.neighborsDictionary[key]:
                self.neighbors[key] = world[self.neighborsDictionary[key]]
            else: 
                self.neighbors[key] = None
        self.world = world
        self.goCommands = goCommands
        self.directions = directions
        self.commands = commands
        self.health = 100


    #Getters and Setters:
    def get_health(self) -> int:
        return self.health
    
    def set_health(self, number):
        self.health = number
    
    def get_location(self):
        return self.location

    #Methods:
    def parseCommand(self, command):
        """
        Takes in string command, strips punctution and makes lower case.
        Splits into list, and returns list.
        """
        command = command.lower().translate(str.maketrans('', '', string.punctuation)).split(" ")
        return command
    
    def go(self, command):
        """
        
        Updates self.location and self directions if direction is valid. Calls new cell's start function.

        If direction is not valid, returns false
        """
        #parse which direction:
        if command in self.goCommands:
            direction = "forward"
        elif command in ["back", "backwards", "b"]:
            direction = "back"
        elif command in ["left", "l"]:
            direction = "left"
        elif command in ["right", "r"]:
            direction = "right"
        else:
            print(f"You can't go {command}... is this a bug?")
            input()
            return    


        #go that way, update neighborhood
        if self.neighbors[direction]:
            self.location = self.neighbors[direction]
            self.neighborsDictionary = self.location.neighbors
            self.neighbors = {}
            for key in self.neighborsDictionary:
                if self.neighborsDictionary[key]:
                    self.neighbors[key] = self.world[self.neighborsDictionary[key]]
                else: 
                    self.neighbors[key] = None
            self.location.start(self.world)
        else:
            print("I can't go that way...")
            input()
        return
    
    def look(self):
        """
        TO DO: prints self.location.about() which tells about the environemnt, and if any items are near.
        """

        self.location.about(self.world)


    def take(self):
        if self.location.get_item():
            item = self.location.get_item()
            self.items[item.get_name()] = item
            self.location.set_item(None)
            print(f"You picked up {item.getInfo()}")
            input()
        else:
            print("You don't see anything to take...")
            input()
    
    def addItem(self, item):
        self.items[item.get_name()] = item
    
    def use(self, object):
        """
        TO DO: the response here will be complicated and depending on context. It really depends on
        how I implement the rest of the game. Should have some effect on enemies and no effect otherwise.
        Using the map should bring up a picture of the world
        """
        if object.lower() in self.items.keys():
            self.items[object].haveEffect(self)
            input()
        else:
            print(f"You don't have a {object}.")
            input()
    
    def showHealth(self):
        print('You\'re health is: ', self.health)
        input()



    def followCommand(self, command):
        """
        Interprets logic of command. takes command arg as list of strings. 
        Returns False if command is not understood.
        """
        
        if not command[0] in self.commands:
            print(f"Ooooo... Soods! I don't know what {command[0]} means")
            input()
            return False

        elif command[0] in self.goCommands:
            if len(command) > 1:
                self.go(command[1])
            else:
                self.go("forward")

        elif command[0] in self.directions:
            self.go(command[0])

        elif command[0] == "look":

            self.look()

        elif command[0] in ["use", "u"]: 
            if len(command) > 1:

                self.use(command[1])
            else:
                print("What do you want to use?")
                print([key for key in self.items.keys()], sep = "  ")
                item = input()
                self.use(item)
        elif command[0] in ["take", "t"]:

            self.take()

        elif command[0] == "help":
            print("you can use the following commands: ")
            print(self.commands)
            input()
        elif command[0] == "quit":

            self.gameOver()
        elif command[0] == "health":
            self.showHealth()

        return True
    
    def takeDamage(self, damage:int) -> None:
        """
        subtracts enemy hit from health
        """
        self.health -= damage
        if self.health < 1:
            self.gameOver()
    
    def gameOver(self):
        """
        Show game over screen
        """      
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('gameOver.txt') as file:
            for line in file.readlines():
                print(line, end="")  
        quit()
    


##Testing code:
"""
cell1 = cell(1, "Hallway", {"forward":None}, "Axe")
cell2 = cell(2,"Hallway", {"forward":cell1}, "Axe")
cell1.neighbors["forward"] = cell2
q = Player(location = cell1)
i = input()
command = q.parseCommand(i)
q.followCommand(command)
"""