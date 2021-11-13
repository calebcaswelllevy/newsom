from cell import *
from item import *


#Construct items:
constitution = item("constitution", showConstitution, "a copy of the US Constitution, the greatest achievement of Mankind.")
vaxCard = item("vaxcard", showVaxCard, "a counterfeit vaccination record.")
vitaminD = item("vitamind", takeVitamins, "a bottle of vitamin D")
mask = item("mask", maskUp, "a mask. Better be careful with this.")
gun = item("gun", shoot, "a gun! Badass.")
katana = item("katana", slice, "the final sword forged by Shakku Arai. \nThe inscription says it was made to protect innocent lives from tyranny.")


#ITEM ARGS = "number", "type", "neighbors", "item", "effect"
mapFramework = [#1-20 are main path
    ["0", "room in the Vaccine Concentration Camp", {"forward": "1", "back" : None, "left": None, "right": None}, mask, None], 
    ["1", "hallway leading towards the Imperial Palace", {"forward": "2", "back" : "0", "left": None, "right": None},None, None], 
    ["2", "hallway", {"forward": "3", "back" : "1", "left": None, "right": None},None, None],
    ["3", "hallway", {"forward": "4", "back" : "2", "left": "Left1", "right": None},None, None],
    ["4", "hallway", {"forward": "5", "back" : "3", "left": None, "right": None},None, None],
    ["5", "hallway", {"forward": "6", "back" : "4", "left": None, "right": None},None, None],
    ["6", "Health Clinic", {"forward": "7", "back" : "5", "left": None, "right": "Right1"},None, None],
    ["7", "Health Clinic", {"forward": "8", "back" : "6", "left": None, "right": None},None, None],
    ["8", "Mandatory Vaccination Checkpoint", {"forward": "9", "back" : "7", "left": None, "right": None},None, vaccination],
    ["9", "Health Clinic", {"forward": "10", "back" : "8", "left": None, "right": "Right9"},None, None],
    ["10", "pathway", {"forward": "11", "back" : "9", "left": None, "right": None},None, None],
    ["11", "pathway", {"forward": "12", "back" : "10", "left": None, "right": None},None, None],
    ["12", "pathway", {"forward": "13", "back" : "11", "left": None, "right": None},None, hippies],
    ["13", "pathway", {"forward": "14", "back" : "12", "left": None, "right": None},None, None],
    ["14", "pathway", {"forward": "15", "back" : "13", "left": "Left2.1", "right": None},None, None],
    ["15", "pathway. A sign reads 'You are approaching the glorious palace of Emperor Gavinius'", {"forward": "16", "back" : "14", "left": None, "right": None},None, None],
    ["16", "pathway", {"forward": "17", "back" : "15", "left": None, "right": None},None, None],
    ["17", "pathway", {"forward": "18", "back" : "16", "left": None, "right": None},None, None],
    ["18", "pathway", {"forward": "19", "back" : "17", "left": None, "right": None},None, None],
    ["19", "pathway", {"forward": "20", "back" : "18", "left": None, "right": "Right2.1"},None, showCastle],
    ["20", "threshold to the palace", {"forward": None, "back" : "19", "left": None, "right": None},None, newsom],  
    #first left passage. branches at 3
    ["Left1", "small side passage marked 'Danger! Do Not Enter!'", {"forward": "Left2", "back" : "3", "left": None, "right": None},None, None],
    ["Left2", "small side passage", {"forward": "Left3", "back" : "Left1", "left": None, "right": None},None, None],
    ["Left3", "small side passage", {"forward": "Left4", "back" : "Left2", "left": None, "right": None},None, None],
    ["Left4", "a musty library", {"forward": None, "back" : "Left3", "left": None, "right": None}, constitution, None],
    #Right loop passage in health clinic:
   
    ["Right1", "small side passage marked 'Employees, LGBTQIA+, and BIPOC Only!'", {"forward": "Right2", "back" : "6", "left": None, "right": None},None, None],
    ["Right2", "small side passage. No one appears to be working. They must all be collecting welfare.", {"forward": "Right3", "back" : "Right1", "left": None, "right": None},None, None],
    ["Right3", "small side passage", {"forward": "Right4", "back" : "Right2", "left": None, "right": None},None, None],
    ["Right4", "a vaccine storage facility", {"forward": "Right5", "back" : "Right3", "left": None, "right": None}, vaxCard, None],
    ["Right5", "small side passage", {"forward": "Right6", "back" : "Right4", "left": None, "right": None}, None, None],
    ["Right6", "small side passage", {"forward": "Right7", "back" : "Right5", "left": None, "right": None}, None, None],
    ["Right7", "small side passage", {"forward": "Right8", "back" : "Right6", "left": None, "right": None}, None, None],
    ["Right8", "Pharmacy store room", {"forward": "Right9", "back" : "Right7", "left": None, "right": None}, vitaminD, None],
    ["Right9", "Pharmacy entrance", {"forward": "9", "back" : "Right8", "left": None, "right": None}, None, None],
    #TO DO: make side passages with gun and katana

    #Left branch with gun at 14:
    ["Left2.1", "small side passage marked 'Danger! Firearms may be present!'", {"forward": "Left2.2", "back" : "14", "left": None, "right": None},None, None],
    ["Left2.2", "small side passage", {"forward": "Left2.3", "back" : "Left2.1", "left": None, "right": None},None, None],
    ["Left2.3", "armory", {"forward": None, "back" : "Left2.2", "left": None, "right": None}, gun, showGun],

    #Right branch with katana: branches at 19
    ["Right2.1", "pathway to the Shrine of Shakku Arai'", {"forward": "Right2.2", "back" : "19", "left": None, "right": None},None, None],
    ["Right2.2", "a peaceful wooded path", {"forward": "Right2.3", "back" : "Right2.1", "left": None, "right": None},None, None],
    ["Right2.3", "armory", {"forward": None, "back" : "Right2.2", "left": None, "right": None},katana, showSword]

]
        
def makeWorld():
    world = {}
    for list in mapFramework:
        world[list[0]] = cell(*list)
    return world



