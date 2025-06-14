"""
Class: Food
Author: Crimson_Lycan
Date: 6-14-2025
Purpose: To implement various types of food. Also, a mushroom is not a fruit.
"""
class Food:
    def __init__(self, foodName, foodDescription, foodPrice, foodServingsMax):
        self.foodName = foodName
        self.foodDescription = foodDescription
        self.foodPrice = foodPrice
        self.foodServingsMax = foodServingsMax # 4 for Chao Garden fruit
        self.foodServingsCurrent = 0
        self.affinityPerServing = 0
        self.airPerServing = 0
        self.armorPerServing = 0
        self.landPerServing = 0
        self.powerPerServing = 0
        self.waterPerServing = 0
        self.staminaPerServing = 1
        self.iqPerServing = 0

    def setStatBoostsPerServing(self, affinity, air, armor, land, power, water, stamina, iq):
        self.affinityPerServing = affinity
        self.airPerServing = air
        self.armorPerServing = armor
        self.landPerServing = land
        self.powerPerServing = power
        self.waterPerServing = water
        self.staminaPerServing = stamina
        self.iqPerServing = iq