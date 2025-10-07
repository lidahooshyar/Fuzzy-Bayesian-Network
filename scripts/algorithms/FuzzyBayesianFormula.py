
import numpy as np

def mu_A(x):
   
    return np.exp(-((x - 5)**2) / 2.0)

def mu_B(y):
    
    return np.exp(-((y - 3)**2) / 2.0)

def P_A(x):
    return 1 / (np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2.0)

def P_B_given_A(y, x):
    return 1 / (np.sqrt(2 * np.pi)) * np.exp(-(y - x)**2 / 2.0)

def P_B():
    B_values = np.linspace(-10, 10, 100)
    A_values = np.linspace(-10, 10, 100)
    total_prob = 0.0
    
    for y in B_values:
        prob_sum = 0.0
        for x in A_values:
            prob_sum += mu_A(x) * P_A(x) * P_B_given_A(y, x)
        total_prob += mu_B(y) * prob_sum
    
    return total_prob

def P_fuzzy_A_given_B():
    B_values = np.linspace(-10, 10, 100)
    A_values = np.linspace(-10, 10, 100)
    total_prob = 0.0
    
    for y in B_values:
        prob_sum = 0.0
        for x in A_values:
            prob_sum += mu_A(x) * mu_B(y) * P_B_given_A(y, x) * P_A(x)
        total_prob += prob_sum
    
    return total_prob / P_B()
result = P_fuzzy_A_given_B()
print("P_fuzzy_A_given_B:", result)