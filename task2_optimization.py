import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Hill Climbing (Підйом на гору / Спуск у долину)
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    step_size = 0.1
    
    for _ in range(iterations):
        # Генеруємо сусіда з невеликим відхиленням
        next_solution = [
            max(min(current_solution[i] + random.uniform(-step_size, step_size), bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]
        next_value = func(next_solution)
        
        if abs(current_value - next_value) < epsilon:
            break
            
        if next_value < current_value:
            current_solution, current_value = next_solution, next_value
            
    return current_solution, current_value

# Random Local Search (Випадковий локальний пошук)
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    for _ in range(iterations):
        # Випадково генеруємо абсолютно нову точку в межах
        candidate_solution = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate_solution)
        
        if abs(current_value - candidate_value) < epsilon:
            # Хоча для випадкового пошуку epsilon менш показовий, слідуємо ТЗ
            if candidate_value < current_value:
                current_solution, current_value = candidate_solution, candidate_value
            continue

        if candidate_value < current_value:
            current_solution, current_value = candidate_solution, candidate_value
            
    return current_solution, current_value

# Simulated Annealing (Імітація відпалу)
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)
    
    current_temp = temp
    
    for _ in range(iterations):
        if current_temp < epsilon:
            break
            
        # Генеруємо сусіда
        next_solution = [
            max(min(current_solution[i] + random.uniform(-0.5, 0.5), bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]
        next_value = func(next_solution)
        
        # Обчислюємо різницю
        delta = next_value - current_value
        
        # Якщо краще — приймаємо. Якщо гірше — приймаємо з ймовірністю P
        if delta < 0 or random.random() < math.exp(-delta / current_temp):
            current_solution, current_value = next_solution, next_value
            
        current_temp *= cooling_rate
        
    return current_solution, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print(f"Розв'язок: {hc_solution} Значення: {hc_value}")

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print(f"Розв'язок: {rls_solution} Значення: {rls_value}")

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print(f"Розв'язок: {sa_solution} Значення: {sa_value}")