import numpy as np
import matplotlib.pyplot as plt

#functions for sigmoid, Gaussian, triangular, and trapezoidal
def sigmoid(x, alpha, c):
    return 1 / (1 + np.exp(-alpha * (x - c)))

def gaussian(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))

def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

def trapezoidal(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)

plt.rcParams.update({'font.size': 14, 'lines.linewidth': 3})

fig, axs = plt.subplots(3, 2, figsize=(12, 20))

x = np.linspace(-10, 10, 400)
a_tri, b_tri, c_tri = -5, 0, 5
a_trap, b_trap, c_trap, d_trap = -7, -3, 3, 7
mu_gauss, sigma_gauss = 0, 2
a_sigmoid, c_sigmoid = 1, 0

tri_values = triangular(x, a_tri, b_tri, c_tri)
trap_values = trapezoidal(x, a_trap, b_trap, c_trap, d_trap)
gauss_values = gaussian(x, mu_gauss, sigma_gauss)
sigmoid_values = sigmoid(x, a_sigmoid, c_sigmoid)

axs[0, 0].plot(x, tri_values, label='Triangular')
axs[0, 0].plot(x, trap_values, label='Trapezoidal')
axs[0, 0].plot(x, gauss_values, label='Gaussian')
axs[0, 0].plot(x, sigmoid_values, label='Sigmoid', color='red')

axs[0, 0].set_xlabel('Domain of variables')
axs[0, 0].set_ylabel('Membership degree')
axs[0, 0].set_title('(a)', loc='left')
axs[0, 0].legend()
axs[0, 0].grid(True)

x_age = np.linspace(0, 100, 1000)
alpha_age = 0.2
sigma_age = 10
mu_young = 1 - sigmoid(x_age, alpha_age, 25)
mu_middle = gaussian(x_age, 50, sigma_age)
mu_old = sigmoid(x_age, alpha_age, 75)

axs[0, 1].plot(x_age, mu_young, label='Young', color='blue')
axs[0, 1].plot(x_age, mu_middle, label='Middle-aged', color='green')
axs[0, 1].plot(x_age, mu_old, label='Old', color='red')
axs[0, 1].set_xlabel('Age')
axs[0, 1].set_ylabel('Membership degree')
axs[0, 1].set_title('(b)', loc='left')
axs[0, 1].legend()
axs[0, 1].grid(True)

x_race = np.linspace(0, 4, 1000)
sigma_race = 0.5
mu_type1 = gaussian(x_race, 1, sigma_race)
mu_type2 = gaussian(x_race, 2, sigma_race)
mu_type3 = gaussian(x_race, 3, sigma_race)

axs[1, 0].plot(x_race, mu_type1, label='Type 1', color='blue')
axs[1, 0].plot(x_race, mu_type2, label='Type 2', color='green')
axs[1, 0].plot(x_race, mu_type3, label='Type 3', color='red')
axs[1, 0].set_xlabel('Numerical representation of race')
axs[1, 0].set_ylabel('Membership degree')
axs[1, 0].set_title('(c)', loc='left')
axs[1, 0].set_xticks([1, 2, 3])
axs[1, 0].legend()
axs[1, 0].grid(True)

x_activity = np.linspace(0, 20, 1000)
alpha_activity = 0.6
sigma_activity = 2
mu_low = (1 - sigmoid(x_activity, alpha_activity, 5)) / (1 - sigmoid(0, alpha_activity, 5)) 
mu_moderate = gaussian(x_activity, 10, sigma_activity)
mu_high = sigmoid(x_activity, alpha_activity, 15) / sigmoid(20, alpha_activity, 15)

axs[1, 1].plot(x_activity, mu_low, label='Low', color='blue')
axs[1, 1].plot(x_activity, mu_moderate, label='Medium', color='green')
axs[1, 1].plot(x_activity, mu_high, label='High', color='red')
axs[1, 1].set_xlabel('Hours per week')
axs[1, 1].set_ylabel('Membership degree')
axs[1, 1].set_title('(d)', loc='left')
axs[1, 1].legend()
axs[1, 1].grid(True)

x_smoking = np.linspace(0, 60, 1000)
alpha_smoking = 0.2
sigma_smoking = 10
mu_nonsmoker = (1 - sigmoid(x_smoking, alpha_smoking, 10)) / (1 - sigmoid(0, alpha_smoking, 10))
mu_medium_smoker = gaussian(x_smoking, 30, sigma_smoking)
mu_heavy_smoker = sigmoid(x_smoking, alpha_smoking, 50) / sigmoid(60, alpha_smoking, 50)

axs[2, 0].plot(x_smoking, mu_nonsmoker, label='Low smoker', color='blue')
axs[2, 0].plot(x_smoking, mu_medium_smoker, label='Medium smoker', color='green')
axs[2, 0].plot(x_smoking, mu_heavy_smoker, label='Heavy smoker', color='red')
axs[2, 0].set_xlabel('Pack years')
axs[2, 0].set_ylabel('Membership degree')
axs[2, 0].set_title('(e)', loc='left')
axs[2, 0].legend()
axs[2, 0].grid(True)

x_risk = np.linspace(0, 1, 1000)
alpha_risk = 10
sigma_risk = 0.1
mu_low_risk = (1 - sigmoid(x_risk, alpha_risk, 0.2)) / (1 - sigmoid(0, alpha_risk, 0.2))
mu_medium_risk = gaussian(x_risk, 0.5, sigma_risk)
mu_high_risk = sigmoid(x_risk, alpha_risk, 0.8) / sigmoid(1, alpha_risk, 0.8)

axs[2, 1].plot(x_risk, mu_low_risk, label='Low risk', color='blue')
axs[2, 1].plot(x_risk, mu_medium_risk, label='Medium risk', color='green')
axs[2, 1].plot(x_risk, mu_high_risk, label='High risk', color='red')
axs[2, 1].set_xlabel('Probability')
axs[2, 1].set_ylabel('Membership degree')
axs[2, 1].set_title('(f)', loc='left')
axs[2, 1].legend()
axs[2, 1].grid(True)

for ax in axs.flat:
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
plt.tight_layout()
plt.subplots_adjust(hspace=0.84, wspace=0.3, top=0.95, bottom=0.05)
plt.show()
