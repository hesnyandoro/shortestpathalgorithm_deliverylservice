import numpy as np
def inventory_optimization(h, s, o, demand, I_max, T):
    # Initialize the cost table and decision table
    costs = np.full((T + 1, I_max + 1), float('inf'))  # Costs for each state
    decisions = np.zeros((T, I_max + 1), dtype=int)   # Optimal reorder decisions

    # Base case: No cost in the final period
    costs[T, :] = 0

    # Backward iteration over time periods
    for t in range(T - 1, -1, -1):
        for I in range(I_max + 1):  # Iterate over all possible inventory levels
            for Q in range(I_max + 1):  # Iterate over all possible order quantities
                I_next = I + Q - demand[t]
                if 0 <= I_next <= I_max:  # Ensure the inventory remains within bounds
                    holding_cost = h * max(I_next, 0)
                    shortage_cost = s * max(-I_next, 0)
                    order_cost = o if Q > 0 else 0
                    total_cost = holding_cost + shortage_cost + order_cost + costs[t + 1, I_next]
                    
                    # Update the cost and decision if this is the best option
                    if total_cost < costs[t, I]:
                        costs[t, I] = total_cost
                        decisions[t, I] = Q

    return costs, decisions

# Example Parameters
h = 1  # Holding cost per unit
s = 5  # Shortage cost per unit
o = 10  # Fixed order cost
demand = [4, 6, 3, 7]  # Demand for 4 periods
I_max = 10  # Maximum inventory capacity
T = len(demand)  # Number of periods

# Compute optimal reorder points
costs, decisions = inventory_optimization(h, s, o, demand, I_max, T)

# Output results
print("Optimal Decisions:")
for t in range(T):
    print(f"Period {t + 1}: {decisions[t]}")

print("\nMinimum Cost Table:")
print(costs)
