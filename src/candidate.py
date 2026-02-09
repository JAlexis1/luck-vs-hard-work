from random import randint

class Candidate:
    def __init__(self):
        self._skill = self._assign_score()
        self._experience = self._assign_score()
        self._hard_work = self._assign_score()
        self._luck = self._assign_score()
    
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
    
    def _assign_score(self):
        MAX_SCORE = 100
        MIN_SCORE = 1
        return randint(MIN_SCORE, MAX_SCORE)