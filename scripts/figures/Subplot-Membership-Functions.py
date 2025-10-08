import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 18,
    'axes.labelsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 18,
    'lines.linewidth': 4
})

def triangular(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)

def trapezoidal(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)

def gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma)**2)

def sigmoid(x, a, c):
    return 1 / (1 + np.exp(-a * (x - c)))

# Adjusted figsize
fig, axs = plt.subplots(2, 2, figsize=(24, 40))
plt.subplots_adjust(plt.subplots_adjust(left=0.08, right=0.98, top=0.99, bottom=0.1, hspace=0.25, wspace=0.2)
 )  # manually increase left margin

# Thicker spines
for ax in axs.flat:
    for spine in ax.spines.values():
        spine.set_linewidth(3)

# Panel (a): Basic shapes
x = np.linspace(-10, 10, 400)
axs[0, 0].plot(x, triangular(x, -5, 0, 5), label='Triangular')
axs[0, 0].plot(x, trapezoidal(x, -7, -3, 3, 7), label='Trapezoidal')
axs[0, 0].plot(x, gaussian(x, 0, 2), label='Gaussian')
axs[0, 0].plot(x, sigmoid(x, 1, 0), label='Sigmoid', color='red')
#axs[0, 0].set_title('(a)')
axs[0, 0].set_xlabel('(a) Variable range')
axs[0, 0].set_ylabel('Membership degree')
axs[0, 0].legend(loc='upper left')
axs[0, 0].grid(True)

# Panel (b): Age
x_age = np.linspace(0, 100, 1000)
alpha_age = 0.2
sigma_age = 10
mu_young = 1 - sigmoid(x_age, alpha_age, 25)
mu_middle = gaussian(x_age, 50, sigma_age)
mu_old = sigmoid(x_age, alpha_age, 75)

axs[0, 1].plot(x_age, mu_young, label='Young', color='blue')
axs[0, 1].plot(x_age, mu_middle, label='Middle-aged', color='green')
axs[0, 1].plot(x_age, mu_old, label='Old', color='red')
#axs[0, 1].set_title('(b)')
axs[0, 1].set_xlabel('(b) Age (Years)')
axs[0, 1].set_ylabel('Membership degree')
axs[0, 1].legend(loc='upper left')
axs[0, 1].grid(True)

# Panel (c): Physical Activity
x_activity = np.linspace(0, 20, 1000)
alpha_activity = 0.6
sigma_activity = 2
mu_low = (1 - sigmoid(x_activity, alpha_activity, 5)) / (1 - sigmoid(0, alpha_activity, 5))
mu_moderate = gaussian(x_activity, 10, sigma_activity)
mu_high = sigmoid(x_activity, alpha_activity, 15) / sigmoid(20, alpha_activity, 15)

axs[1, 0].plot(x_activity, mu_low, label='Low', color='blue')
axs[1, 0].plot(x_activity, mu_moderate, label='Moderate', color='green')
axs[1, 0].plot(x_activity, mu_high, label='High', color='red')
#axs[1, 0].set_title('(c)')
axs[1, 0].set_xlabel('(c) Physical activity (Hours per week)')
axs[1, 0].set_ylabel('Membership degree')
axs[1, 0].legend(loc='upper left')
axs[1, 0].grid(True)

# Panel (d): Smoking Status
x_smoking = np.linspace(0, 120, 1000)
alpha_smoking = 0.4
sigma_smoking = 20
mu_nonsmoker = (1 - sigmoid(x_smoking, alpha_smoking, 20)) / (1 - sigmoid(0, alpha_smoking, 20))
mu_medium = gaussian(x_smoking, 60, sigma_smoking)
mu_heavy = sigmoid(x_smoking, alpha_smoking, 100) / sigmoid(120, alpha_smoking, 100)

axs[1, 1].plot(x_smoking, mu_nonsmoker, label='Nonsmoker', color='blue')
axs[1, 1].plot(x_smoking, mu_medium, label='Medium smoker', color='green')
axs[1, 1].plot(x_smoking, mu_heavy, label='Heavy smoker', color='red')
#axs[1, 1].set_title('(d)')
axs[1, 1].set_xlabel('(d) Smoking status (Pack years)')
axs[1, 1].set_ylabel('Membership degree')
axs[1, 1].legend(loc='upper left')
axs[1, 1].grid(True)
axs[1, 1].set_xlim(0, 120)

# Save with padding
plt.savefig('membership_functions_fixed.png', dpi=400, bbox_inches='tight', pad_inches=0.5)
plt.show()
