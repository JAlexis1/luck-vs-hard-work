class Stats:
    def __init__(self, luck_candidates, no_luck_candidates):
        self.luck_candidates = luck_candidates
        self.no_luck_candidates = no_luck_candidates
        self.runs = len(luck_candidates)
        self.candidates = len(luck_candidates[0])

    def calculate_luck_average(self, top_n):
        sum_of_run_averages = 0
        for run in range(self.runs):
            total_luck = 0
            for candidate in range(top_n):
                total_luck += self.luck_candidates[run][candidate][1][1] # to get the luck score of the candidate
            sum_of_run_averages += total_luck/top_n
        luck_average = sum_of_run_averages/self.runs
        return luck_average
    
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