# Programming Assignment 1: Matching and Verifying

## Authors
* **Name 1:** Vinay Reddy Ratnam (UFID: 20765170)
* **Name 2:** Isaac Philipose (UFID: 86084445)

---

## Instructions to Compile/Build
Since this project is implemented in **Python 3**, there is no explicit compilation step (like `make` or `javac`). However, the environment must be set up correctly to run the scripts.

* **Prerequisites:** Python 3.6 or higher.
* **Dependencies:**
    * The core algorithms (`matcher.py`, `verifier.py`) use only standard libraries (`sys`).

---

## Instructions to Run
The programs are designed to communicate via **Standard Input/Output (stdin/stdout)**. This allows for flexible testing and piping between the matcher and the verifier.

### 1. Run the Matcher (Task A)
The matcher reads preference input from **stdin** and prints the resulting matched pairs to **stdout**.

* **Basic Run (Output to Terminal):**
  ```bash
  python3 src/gale_shapley.py < [Location of Input File]
  ```

* **Save Output to File:**
  ```bash
  python3 src/gale_shapley.py < [Location of Input File] > [Name of Output File]
  ```

* **Example:**
  ```bash
  python3 src/gale_shapley.py < data/input/given_example.in > data/output/given_example.out
  ```

### Run the Verifier (Task B)
The verifier requires 2 inputs, both passed in through stdin.

* **Basic Run:**
  ```bash
  (cat [Location of Preference Lists File]; echo ""; cat [Location of Matchings File]) | python3 src/verifier.py
  ```

* **Example:**
  ```bash
  (cat data/input/given_example.in; echo ""; cat data/output/given_example.out) | python3 src/verifier.py
  ```

## Assumptions


### Input Handling

* **Strict Formatting:** The input parser is strict. It expects exactly $2n + 1$ non-empty lines. Blank lines in the middle of preference lists will cause an error (to prevent parsing malformed data). However, you can include a variable number of spaces between each number on a line.
* **Whitespace: DO NOT INCLUDE NEWLINES AT THE END OF INPUT FILES**
* **Permutations:** It is assumed (and checked) that every preference list is a valid permutation of numbers $1 \dots n$.

### Indexing

* **Internal:** The code converts these to **0-based indexing** for processing and converts them back to 1-based for output.

### Execution Environment

* It is assumed the user runs commands from the root of the repository (e.g., `python3 src/matcher.py` rather than `cd src; python3 matcher.py`).

---

![Alt text](graphs/scalability_graph_avg.png)