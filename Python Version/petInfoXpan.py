"""
Class: Pet Info Expansion (Chao-Derivative Type)
Author: Crimson_Lycan
Date: 6-14-2025
"""

class PetInfoXpan:
    def __init__(self, idNum):
        # Use main program to fetch the ID number from the pet's base data to "link" with the expansion data.
        self.idNum = idNum

        # Expansion Data
        self.lifeStage = "Egg"
        self.airStat = 0            # Fly (Stealth)
        self.airLevel = 0
        self.airProgress = 0
        self.armorStat = 0          # Armor (This is new!)
        self.armorLevel = 0         # To convert to traditional chao type: (swim = water + armor / 2), maybe...
        self.armorProgress = 0
        self.landStat = 0           # Run (Speed)
        self.landLevel = 0
        self.landProgress = 0
        self.powerStat = 0          # Power ()
        self.powerLevel = 0
        self.powerProgress = 0
        self.staminaStat = 0        # Stamina (Health)
        self.staminaLevel = 0
        self.staminaProgress = 0
        self.waterStat = 0          # Swim (Defense)
        self.waterLevel = 0         # The conversion didn't make sense...
        self.waterProgress = 0
        self.antiCheatSave = hash((str(self.combineStats()) + self.idNum))

    def combineStats(self):
        combinedStats = (((self.airStat + self.landStat + self.waterStat) / 3) +
            ((self.armorStat + self.powerStat + self.staminaStat) / 3) / 2)
        return combinedStats
    
    #A simple piece of code, but it'll help keep the inexperienced from cheating...
    def antiCheat(self):
        return hash((str(self.combineStats()) + self.idNum))