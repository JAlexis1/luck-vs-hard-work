from simulation import Simulation
from stats import Stats

if __name__ == "__main__":
    candidates = 100
    runs = 1000
    top_n = 1

    simulation = Simulation(candidates, runs)
    simulation_with_luck, simulation_without_luck = simulation.run()

    stats_calculator = Stats(simulation_with_luck, simulation_without_luck)

    luck_average = stats_calculator.calculate_luck_average(top_n)
    selection_overlap = stats_calculator.selection_overlap(top_n)
    porcentage_overlap = selection_overlap/top_n*100

    print("-"*90)
    print(f"The average luck score of the top candidates was: {luck_average:.2f}")
    print("-"*90)
    print(f"The average overlap between the top candidates with and without luck was: {selection_overlap:.2f}")
    print("-"*90)
    print(f"This means that on average, the top candidate with luck was also in the top candidate without luck in {porcentage_overlap:.2f}% of the runs.")