# 🎯 Monty Hall Problem Simulation

This project is a Python implementation of the **Monty Hall Problem**, a famous probability puzzle based on a TV game show scenario.  
The simulation allows you to test both strategies:
- **Changing** your choice after the host reveals a goat door.
- **Keeping** your original choice.

---

## 📜 About the Monty Hall Problem
In the game:
1. There are three doors: behind one is a **car** (prize), behind the other two are **goats**.
2. You choose one door.
3. The host (Monty Hall) opens another door, always revealing a goat.
4. You are given the option to **switch** to the other unopened door or **stay**.

**Mathematically**:
- If you **stay**, your chance of winning is about **33.3%**.
- If you **switch**, your chance of winning is about **66.6%**.

---

## 🚀 How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Amin-Abdolahi/App-Monty-Hall-Problem.git
cd App-Monty-Hall-Problem
````

### 2️⃣ Run the script

```bash
python monty_hall.py
```

### 3️⃣ Follow the prompts

* Enter the number of simulation rounds.
* Choose whether you want to play **with the change option** (`y`) or without (`n`).

---

## 📊 Example Output

```text
Press Enter to start the simulation...
Enter the number of times to play: 10000
Play with change option? (y/n): y
Win rate: 66.77%
Loss rate: 33.23%
```

---

## 🧠 Why this matters

The Monty Hall Problem is a great example of how **human intuition** can often fail in probability scenarios.
This simulation lets you **see the results for yourself** by running thousands of trials.

---

## 📂 Project Structure

```
App-Monty-Hall-Problem/
│── monty_hall.py     # Main simulation code
│── README.md         # Project documentation
```

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it.
