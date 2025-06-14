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

    def petCommand(self):
        if (self.petBase.mood < 10):
            self.petBase.mood += 1
            self.petBase.moodTimekeep = 0