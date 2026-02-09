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