import numpy as np
import time
traffic_streets = np.array([50, 10, 80, 20])

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

while True:
    
    busy_street_indices = np.where(traffic_streets > 100)[0] + 1
    status = GREEN + "Normal" + RESET
    
    if len(busy_street_indices) > 0:
        status = RED + "CRITICAL - ACTION REQUIRED" + RESET 

    print(f"Traffic state now is: {traffic_streets} | Status: {status}")
    print(f"Decision: Grant Greeb Light to Streets: {busy_street_indices}")

    change = np.random.randint(-10, 15, size=4)

    traffic_streets = np.maximum(traffic_streets + change, 0)

    time.sleep(1)
    print("-" * 30)