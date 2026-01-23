class candidate:
    def __init__(self, skill, experience, hard_work, luck):
        self._skill = skill
        self._experience = experience
        self._hard_work = hard_work
        self._luck = luck
    
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