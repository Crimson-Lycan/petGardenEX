"""
Class: Player Info Base
Author: Crimson_Lycan
Date: 6-12-2025
"""
class PlayerInfoBase:
    def __init__(self, name, idNum):
        self.name = name
        self.password = ""
        self.money = 0
        self.idNum = idNum
        self.moneyTimekeep = 0
        self.affinity = 0
        self.level = 0
        self.experience = 0
