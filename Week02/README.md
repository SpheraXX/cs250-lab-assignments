# CS250 - Computational Thinking: Lab 02 Submission

**Class Section:** 25A01  
**Practical Assignment:** Week 02 (Lab 02 - Basic Python)  
**Student Name:** Nguyen Duc Huy  
**Student ID:** 25125014  
**GitHub Profile:** [SpheraXX](https://github.com/SpheraXX)  
**Submission Archive:** `25125014_W02_11.zip`  

---

## 1. Submission Folder Structure

```text
25125014_W02/
├── README.md
├── Git Commit Log.md
├── Exercise01/ ... Exercise10/   # main.py + screenshot of the Accepted verdict on Codeforces
└── Exercise11/                   # group project contribution + git commit log (.txt)
```

Environment: Python 3, no external libraries. Run any exercise with `python main.py` and type the input.

---

## 2. Exercises

| Exercise | Problem | Idea |
| :--- | :--- | :--- |
| 01 | [1A - Theatre Square](https://codeforces.com/problemset/problem/1/A) | `ceil(n/a) * ceil(m/a)` |
| 02 | [2A - Winner](https://codeforces.com/problemset/problem/2/A) | First pass: final scores and max `m`. Second pass: replay rounds, first player with final score `m` to reach `>= m` wins |
| 03 | [3A - Shortest path of the king](https://codeforces.com/problemset/problem/3/A) | Each step fixes the horizontal axis (L/R) and the vertical axis (U/D) at the same time; stop when both are equal |
| 04 | [4A - Watermelon](https://codeforces.com/problemset/problem/4/A) | Even and greater than 2 |
| 05 | [5A - Chat Server's Outgoing Traffic](https://codeforces.com/problemset/problem/5/A) | Count people online, add `len(message) * people` for each message |
| 06 | [6B - President's Office](https://codeforces.com/problemset/problem/6/B) | Flood fill (DFS) from the president's desk, mark neighbouring desk colours in a map, then count the marked ones |
| 07 | [7B - Memory Manager](https://codeforces.com/problemset/problem/7/B) | Simulate the memory as an array of size `m` (brute force, `m, t <= 100`) |
| 08 | [8B - Obsession with Robots](https://codeforces.com/problemset/problem/8/B) | BUG if a cell is visited twice, or two cells at Manhattan distance 1 are not consecutive in the path |
| 09 | [9B - Running Student](https://codeforces.com/problemset/problem/9/B) | Try every stop (except the first), take minimum time; on a tie take the stop closest to the university |
| 10 | [10B - Cinema Cashier](https://codeforces.com/problemset/problem/10/B) | For each row keep a running count of free seats; segment cost from prefix sums of `|y - c|`. Rows are checked from the middle outwards and stop early once they cannot beat the best cost; each row caches its best segment per size until a seat in it is taken |
| 11 | Group project | See `Exercise11/` |

---

## 3. AI Usage Declaration

All ideas and code in this lab are my own work. AI was used only as a tool for debugging:

| Tool | Model | What I used it for |
| :--- | :--- | :--- |
| Claude Code | Claude Opus 5.5 (Anthropic) | Pointing out the tie-break edge case in Ex09, explaining why Ex10 got Time Limit Exceeded and hinting at pruning / caching, and reorganizing the repo folder |

I submitted all solutions to Codeforces myself and can explain each one.
