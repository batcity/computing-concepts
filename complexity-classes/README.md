# 🧠 Complexity Classes

## 📘 What Are Complexity Classes?
A **complexity class** is a group of computational problems that require **similar amounts of time or memory** for a computer to solve.  
They help computer scientists understand **how hard problems are** and **which algorithms are practical**.

---

## ⚙️ Resources We Measure
1. **Time complexity** → how long an algorithm takes as input size grows  
2. **Space complexity** → how much memory an algorithm uses  

We usually describe both using **Big-O notation** — e.g., `O(n)`, `O(n²)`, `O(2ⁿ)` — to show how the work grows with the input size `n`.

---

## ⏱ Polynomial vs Exponential Time

| Term | Example | Growth | Meaning |
|------|----------|---------|---------|
| **Polynomial time** | `O(n)`, `O(n²)`, `O(n³)` | Grows reasonably | Efficient — gets slower as inputs grow, but still practical |
| **Exponential time** | `O(2ⁿ)`, `O(3ⁿ)` | Grows extremely fast | Impractical — becomes huge even for small inputs |

➡️ **Polynomial = good (feasible)**  
➡️ **Exponential = bad (explodes quickly)**

---

## 🧩 Key Complexity Classes

| Class | Meaning | Example Problems |
|--------|----------|----------------|
| **P** | Problems that can be **solved quickly (in polynomial time)** | Sorting numbers, finding shortest paths (Dijkstra’s algorithm) |
| **NP** | Problems where a **solution can be checked quickly**, even if finding it might be hard | Sudoku, Traveling Salesman, Boolean Satisfiability (SAT) |
| **NP-complete** | The **hardest problems in NP** — if one of them can be solved quickly, *all* NP problems can | Traveling Salesman, Subset Sum |
| **PSPACE** | Problems that can be solved using a **reasonable (polynomial) amount of memory** | Certain game-solving problems (like chess endgames) |
| **EXPTIME** | Problems that need **exponential time** | Solving generalized chess |

---

## 🧮 The Big Question: *P vs NP*
- **P** = problems that can be solved quickly.  
- **NP** = problems whose solutions can be *verified* quickly.  
- The **open question**:  
  > “If a solution can be verified quickly, can it also be found quickly?”

This is the famous **P vs NP problem**, one of the biggest unsolved questions in computer science.  
No one knows yet if **P = NP** or **P ≠ NP**.

---

## 🧭 In Summary
- **Complexity classes** categorize problems by how much **time** or **memory** they need.  
- **P** problems are efficient.  
- **NP** problems might not be.  
- **Exponential-time** problems blow up fast as input grows.  
- Understanding these classes helps us know **which problems are realistically solvable** by computers.