from candidate import Candidate
from evaluator import Evaluator

class Simulation:
    def __init__(self, candidates, runs):
        self.candidates = candidates
        self.runs = runs
    
    def run(self):
        sorted_with_luck = []
        sorted_without_luck = []
        for _ in range(self.runs):
            score_with_luck = {}
            score_without_luck = {}
            for i in range(self.candidates):
                candidate = Candidate()
                score_with_luck[i] = Evaluator.evaluate_with_luck(candidate)
                score_without_luck[i] = Evaluator.evaluate_without_luck(candidate)
            sorted_with_luck.append(sorted(score_with_luck.items(), key=lambda x: x[1][0], reverse=True))
            sorted_without_luck.append(sorted(score_without_luck.items(), key=lambda x: x[1], reverse=True))
        return sorted_with_luck, sorted_without_luck