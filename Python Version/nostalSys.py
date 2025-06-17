"""
Class: NostalSys
Author: Crimson_Lycan
Date: 6-12-2025
"""
import json, random
from petInfoBase import PetInfoBase
from playerInfoBase import PlayerInfoBase

class NostalSys:
    playerFileName = "player.json"
    petFileName = "pet_base.json"

    def __init__(self):
        # ID Number Generation 
        stringID1 = random.randint(10, 99)
        stringID2 = random.randint(100, 999)
        stringID3 = random.randint(1000, 9999)
        idString = f"{stringID1}-{stringID2}-{stringID3}"

        self.petBase = PetInfoBase("", idString)
        self.playerBase = PlayerInfoBase("", idString)
        self.playerBase.money = 100

    #Load player data, needs work...
    def loadGamePlayer(self):
        with open(self.playerFileName) as json_file:
            self.playerBase = json.load(json_file)
        return self.playerBase
    
    #Save player data.
    def saveGamePlayer(self):
        with open(self.playerFileName, 'w') as outfile:
            json.dump(self.playerBase, outfile)
    
    # Load basic pet data.
    # A game using NostalSys needs to load expansion data in their own program for other key data.
    def loadPetData(self):
        with open(self.petFileName) as json_file:
            self.petBase = json.load(json_file)
        return self.petBase

    def petCommand(self):
        if (self.petBase.mood < 10):
            self.petBase.mood += 1
            self.petBase.moodTimekeep = 0