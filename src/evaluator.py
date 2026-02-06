class Evaluator:
    EFFORT_WEIGHT = 0.95
    LUCK_WEIGHT = 0.05

    @staticmethod
    def evaluate_with_luck(candidate):
        effort = (
            candidate.skill + 
            candidate.experience + candidate.hard_work
            )/ 3
        
        return (
            effort * Evaluator.EFFORT_WEIGHT + 
            candidate.luck * Evaluator.LUCK_WEIGHT, candidate.luck # to know the luck of the candidate 
            )
    
    @staticmethod
    def evaluate_without_luck(candidate):
        effort = (
            candidate.skill + 
            candidate.experience + candidate.hard_work
            )/ 3
        
        return effort