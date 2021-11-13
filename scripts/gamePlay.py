import os
import cell
import player
import gameMap
from directoryHandler import switchToThisDirectory

def main():
    def startGame():
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('titlePage.txt') as file:
            for line in file.readlines():
                print(line, end="")
        input('\n\nPress Enter to enter Hell on earth...')

    def playIntro():
        """
        Show intro screens
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('intro_1.txt') as file:
            for line in file.readlines():
                print(line, end = "")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')   
        with open('intro_2.txt') as file:
            for line in file.readlines():
                print(line, end = "")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')

        with open('intro_3.txt') as file:
            for line in file.readlines():
                print(line, end = "")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('intro_4.txt') as file:
            for line in file.readlines():
                print(line, end="")
        input()


    def playGame():
        """
        To DO: Implement Main game loop
        """
        over = False
        
        world = gameMap.makeWorld()
        
        quentin = player.Player(world["0"], world)

        while quentin.get_health() > 0 and not over:
            takeTurn(quentin)
        if quentin.get_health() <= 0:
            gameOver()
        else:
            win()

    def takeTurn(quentin):
        """
        TO DO: show cell, have effect of cell (i.e. if enemy present), take input
        """
        #Show Cell:
        os.system('cls' if os.name == 'nt' else 'clear')
        quentin.look()

        #Have effect:
        if quentin.get_location().get_effect():
            
            effect = quentin.get_location().get_effect()
            effect(quentin)
        
        #take input:
        print()
        print("What would you like to do? Type 'help' for commands")
        command = input()
        command = quentin.parseCommand(command)
        quentin.followCommand(command)

    def gameOver():
        """
        Show game over screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('gameOver.txt') as file:
            for line in file.readlines():
                print(line, end="")  
    def win():
        """
        Show winning screen
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You Win!")

    #If this script was called from another, directory, moves us here for access ot other files.
    switchToThisDirectory()
    #gets us going.
    startGame()
    playIntro()
    playGame()
    gameOver()

if __name__ == "__main__":
    main()
