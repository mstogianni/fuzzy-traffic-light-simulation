# Fuzzy Traffic Light Simulation

This project implements a **fuzzy logic–based traffic light controller** in Python.

It simulates multiple traffic lights and uses **fuzzy rules** to adjust the green-light duration dynamically based on:

- current queue length  
- vehicle arrival rate  
- traffic intensity per direction  

The goal is to demonstrate how fuzzy logic can be used to improve traffic flow compared to fixed-timing traffic lights.

---

## 🧠 Core Idea

Instead of using fixed green times, the controller:

- measures the **number of cars** in each lane/queue  
- estimates the **traffic load**  
- uses fuzzy membership functions and rules to decide:
  - whether the light should stay green longer  
  - or switch sooner to another direction  

This creates a more adaptive and realistic traffic behavior.

---

## 🔧 Technologies Used

- **Python**
- **NumPy**
- **scikit-fuzzy**
- (optionally) `matplotlib` for plotting or debugging

---

## 🔍 Main Components

### 🧮 Fuzzy Logic System

The project defines:

- **Input variables** (e.g. queue length, arrival rate)  
- **Output variable** (e.g. green time or extension)  
- Membership functions for low / medium / high values  
- Fuzzy rules (IF–THEN) such as:

> IF queue is **high** AND arrival rate is **high** → THEN green time is **long**

These are built using `scikit-fuzzy`’s control system API.

---

### 🚦 Traffic Light Simulation

The simulation loop typically:

1. Initializes several traffic lights (e.g. 4 directions)
2. For each time step:
   - updates the **number of cars** in queues  
   - simulates **arrivals** (often with randomness / Poisson-like behavior)  
   - calls the fuzzy controller to compute a **green duration** or extension  
   - updates the state of each traffic light accordingly  
3. Tracks:
   - how many cars passed  
   - how long queues become  
   - overall throughput

This makes it useful as a **small traffic engineering experiment.**

---

## 📁 File Included

- `fuzzy_traffic_simulation.py` — main simulation and fuzzy logic controller

---

## ▶️ How to Run

1. Install the dependencies:

```bash
pip install numpy scikit-fuzzy
```
Run the script:

```bash
python fuzzy_traffic_simulation.py
```
Watch the console output (and any optional plots) showing how:

queues evolve

green times change

traffic is served per cycle

🎓 What This Project Demonstrates
Practical use of fuzzy logic in a control problem

Modeling a traffic light controller using fuzzy rules

Simulation of queues and flow in a traffic network

Integration of Python, NumPy, and scikit-fuzzy

Structuring a small simulation project

This project is a good example of combining AI-style reasoning (fuzzy logic) with a real-world inspired system like traffic lights.
