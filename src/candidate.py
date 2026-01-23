from random import randint

class Candidate:
    def __init__(self):
        self._skill = self.assign_score()
        self._experience = self.assign_score()
        self._hard_work = self.assign_score()
        self._luck = self.assign_score()
    
    @property
    def skill(self):
        return self._skill
    
    @property
    def experience(self):
        return self._experience
    
    @property
    def hard_work(self):
        return self._hard_work
    
    @property
    def luck(self): 
        return self._luck
    
    def assign_score(self):
        MAX_SCORE = 100
        MIN_SCORE = 1
        return randint(MIN_SCORE, MAX_SCORE)