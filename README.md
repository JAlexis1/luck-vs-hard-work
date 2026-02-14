# Luck vs hard work

This project aims to simulate the influence of luck in competitive selection systems such as hiring, academic admissions, promotions, entrepreneurship, or elite competitions.
The project explores whether this selection can be explained only by hard work and merit, or whether luck also plays an important role.

This project is inspired by the Veritasium video **“Is Success Luck or Hard Work?”**  
https://www.youtube.com/watch?v=3LopI4YeC4I

In the video (minute 3:40), success is modeled as being influenced mostly by skill, experience, and hard work (95%), with a small contribution from luck (5%). Even with such a small percentage, luck can significantly affect final outcomes.

To explore this idea, this project simulates candidates, evaluates them both with and without luck, and compares the results to analyze the impact that luck has on selection outcomes.

## How it works

Each candidate is randomly assigned scores from 1 to 100 for skill, experience, hard work, and luck. These attributes are combined using a weighted evaluation. The simulation runs multiple times to compare selection results when luck is included (95% merit, 5% luck) versus when it is ignored. We measure the average luck score of selected candidates and the overlap between top candidates selected with and without luck.

## Experimental setup

For this experiment we run the simulation 1000 times varying the number of candidates (100, 500, 1000) and the number of selected candidates (10, 5, 1)

## Results

### 100 Candidates

| Top N | Avg Luck | Overlap % |
|-------|----------|-----------|
| 10    | 55.53    | 92.03%    |
| 5     | 57.08    | 89.58%    |
| 1     | 59.06    | 84.30%    |

### 500 candidates

| Top N | Avg Luck | Overlap % |
|------:|---------:|----------:|
| 10    | 58.02    | 87.08%    |
| 5     | 60.71    | 82.78%    |
| 1     | 65.36    | 72.80%    |

### 1000 candidates

| Top N | Avg Luck | Overlap % |
|------:|---------:|----------:|
| 10    | 60.15    | 84.25%    |
| 5     | 62.85    | 80.16%    |
| 1     | 68.02    | 66.00%    |

## Key findings

At the end we find 3 main ideas:

1: Larger competitive systems amplify the effect of luck

As the number of candidates increases, the overlap between merit-only and merit+luck selections decreases.
**In large populations, small randomness significantly alters who is selected.**

2: Highly selective systems are more unstable

When only one candidate is selected (Top 1), overlap drops dramatically.
The more selective the system, the more luck influences the winner.
**Extreme competitiveness increases sensitivity to luck.**

3: Winners in larger systems tend to be luckier

The average luck score of selected candidates increases as the candidate pool grows.
**In larger competitions, being slightly lucky becomes increasingly important.**

## Conclusion

Even when luck influences just in a 5% it can change selection outcomes, especially in large candidate pools and highly selective systems.

This suggests that while hard work and merit are crucial, luck also plays a significant role in determining success, especially in highly competitive environments.