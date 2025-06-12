"""
Class: Pet Info Base
Author: Crimson_Lycan
Date: 6-12-2025
"""
class petInfoBase:
    def __init__(self, name, idNum):
        # Basic Stats used in almost every pet sim.
        self.name = name
        self.age = 0
        self.mood = 0
        self.belly = 0
        self.secretIQ = 0
        self.secretLuck = 0
        self.affinity = 0
        self.idNum = idNum
        self.mainTimekeep = 0
        self.moodTimekeep = 0
        self.bellyTimekeep = 0