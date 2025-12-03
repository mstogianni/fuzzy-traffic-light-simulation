import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time

# Fuzzy logic variables (antecedents and consequent)
queue1 = ctrl.Antecedent(np.arange(0, 101, 1), "queue1")
queue2 = ctrl.Antecedent(np.arange(0, 101, 1), "queue2")
queue3 = ctrl.Antecedent(np.arange(0, 101, 1), "queue3")
queue4 = ctrl.Antecedent(np.arange(0, 101, 1), "queue4")
green_time = ctrl.Consequent(np.arange(10, 91, 1), "green_time")

# Define fuzzy sets for queues (small, medium, large)
for queue in [queue1, queue2, queue3, queue4]:
    queue["small"] = fuzz.trimf(queue.universe, [0, 0, 30])
    queue["medium"] = fuzz.trimf(queue.universe, [20, 50, 80])
    queue["large"] = fuzz.trimf(queue.universe, [60, 100, 100])

# Define fuzzy sets for green light duration
green_time["short"] = fuzz.trimf(green_time.universe, [10, 10, 30])
green_time["medium"] = fuzz.trimf(green_time.universe, [20, 50, 70])
green_time["long"] = fuzz.trimf(green_time.universe, [60, 90, 90])

# Fuzzy rules
rules = []
for queue in [queue1, queue2, queue3, queue4]:
    rules.append(ctrl.Rule(queue["small"], green_time["short"]))
    rules.append(ctrl.Rule(queue["medium"], green_time["medium"]))
    rules.append(ctrl.Rule(queue["large"], green_time["long"]))

# Create control system
traffic_ctrl = ctrl.ControlSystem(rules)
traffic_sim = ctrl.ControlSystemSimulation(traffic_ctrl)

# Vehicle flow constants
MAX_PASSING = 15  # max number of vehicles that can pass per 10 seconds


def vehicles_passing(green_duration, queue_length):
    """
    Calculates how many vehicles pass during the green light.
    Base flow: 10 veh / 10 sec.
    Higher queue length increases flow up to MAX_PASSING.
    """
    base_flow = 10
    dynamic_flow = min(MAX_PASSING, base_flow + (queue_length // 20) * 5)
    return min(queue_length, int((green_duration / 10) * dynamic_flow))


def simulate_traffic_lights():
    queues = [0, 0, 0, 0]  # initial vehicle queues
    max_cycles = 10

    print("Enter the vehicle arrival rate for each traffic light:")

    arrival_rates = []
    for i in range(4):
        while True:
            try:
                rate = int(input(f" Arrival rate for light {i + 1}: "))
                if rate < 0:
                    print("Arrival rate cannot be negative. Try again.")
                else:
                    arrival_rates.append(rate)
                    break
            except ValueError:
                print("Please enter a valid integer.")

    for cycle in range(1, max_cycles + 1):
        print(f"\n--- Cycle {cycle} ---")

        # Random arrivals (Poisson distributed)
        for i in range(4):
            arrivals = np.random.poisson(arrival_rates[i])
            queues[i] += arrivals
            print(f" Light {i + 1}: Arrivals = {arrivals}, Total waiting = {queues[i]}")

        # Each light turns green once per cycle
        for i in range(4):

            for j in range(4):
                traffic_sim.input[f"queue{j + 1}"] = min(queues[j], 100)

            traffic_sim.compute()

            green_duration = traffic_sim.output["green_time"]
            passed = vehicles_passing(green_duration, queues[i])
            queues[i] = max(0, queues[i] - passed)

            print(f"\n Light {i + 1}: Green for {green_duration:.2f} seconds")
            print(f" Vehicles passed: {passed}")
            print(f" Vehicles remaining: {queues[i]}")

            time.sleep(1)

        print(f"\nEnd of cycle {cycle}.")

        if all(q == 0 for q in queues):
            print("No vehicles waiting. Ending simulation.")
            break


if __name__ == "__main__":
    simulate_traffic_lights()
