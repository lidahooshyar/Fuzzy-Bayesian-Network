import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 18,
    'axes.labelsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16,
    'lines.linewidth': 4
})

def gaussian(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma)**2)

def sigmoid(x, a, c):
    return 1 / (1 + np.exp(-a * (x - c)))

# Normal square-ish figure with balanced spacing
fig, axs = plt.subplots(3, 1, figsize=(11, 14))
plt.subplots_adjust(left=0.10, right=0.95, top=0.97, bottom=0.15, hspace=0.35)

for ax in axs.flat:
    for spine in ax.spines.values():
        spine.set_linewidth(2.5)

# (a) Age
x_age = np.linspace(0, 100, 1000)
mu_young = 1 - sigmoid(x_age, 0.2, 25)
mu_middle = gaussian(x_age, 50, 10)
mu_old = sigmoid(x_age, 0.2, 75)

axs[0].plot(x_age, mu_young, label='Young', color='blue')
axs[0].plot(x_age, mu_middle, label='Middle-aged', color='green')
axs[0].plot(x_age, mu_old, label='Old', color='red')
axs[0].set_xlabel('(a) Age (Years)')
axs[0].legend(loc='upper left')
axs[0].grid(True)



# (b) Physical Activity
x_activity = np.linspace(0, 20, 1000)
mu_low = (1 - sigmoid(x_activity, 0.6, 5)) / (1 - sigmoid(0, 0.6, 5))
mu_moderate = gaussian(x_activity, 10, 2)
mu_high = sigmoid(x_activity, 0.6, 15) / sigmoid(20, 0.6, 15)

axs[1].plot(x_activity, mu_low, label='Low', color='blue')
axs[1].plot(x_activity, mu_moderate, label='Moderate', color='green')
axs[1].plot(x_activity, mu_high, label='High', color='red')
axs[1].set_xlabel('(b) Physical activity (Hours per week)')
axs[1].set_ylabel('Membership Degree ($\mu(x)$)')
axs[1].legend(loc='upper left')
axs[1].grid(True)

# (c) Smoking Status
x_smoking = np.linspace(0, 120, 1000)
mu_nonsmoker = (1 - sigmoid(x_smoking, 0.4, 20)) / (1 - sigmoid(0, 0.4, 20))
mu_medium = gaussian(x_smoking, 60, 20)
mu_heavy = sigmoid(x_smoking, 0.4, 100) / sigmoid(120, 0.4, 100)

axs[2].plot(x_smoking, mu_nonsmoker, label='Nonsmoker', color='blue')
axs[2].plot(x_smoking, mu_medium, label='Medium smoker', color='green')
axs[2].plot(x_smoking, mu_heavy, label='Heavy smoker', color='red')
axs[2].set_xlabel('(c) Smoking status (Pack years)')
axs[2].legend(loc='upper left')
axs[2].grid(True)
axs[2].set_xlim(-5, 125)

# Save and show
plt.savefig('membership_functions_centered.png', dpi=400, bbox_inches='tight', pad_inches=0.4)
plt.show()
