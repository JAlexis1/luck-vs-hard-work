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
    
    def get_top_n_candidates(self, sorted_candidates, top_n):
        if top_n > len(sorted_candidates[0]):
            raise ValueError("top_n must be less than or equal to the number of candidates")
        top_candidates = []
        for i in range(len(sorted_candidates)):
            selected_candidates = [] # auxiliar list to store the top n candidates for each run
            for j in range(top_n):
                selected_candidates.append(sorted_candidates[i][j][0])
            top_candidates.append(selected_candidates)
        return top_candidates