
import numpy as np

# ---------------------------
# Fuzzy membership functions
# ---------------------------
def age_membership(x):
    young = 1 - 1/(1 + np.exp(-0.2*(x-25)))
    middle = np.exp(-((x-50)**2)/(2*10**2))
    old = 1/(1 + np.exp(-0.2*(x-75)))
    return np.array([young, middle, old])

def physical_membership(x):
    low = 1 - 1/(1 + np.exp(-0.2*(x-5)))
    medium = np.exp(-((x-10)**2)/(2*5**2))
    high = 1/(1 + np.exp(-0.2*(x-15)))
    return np.array([low, medium, high])

def smoking_membership(x):
    low = 1 - 1/(1 + np.exp(-0.4*(x-20)))
    medium = np.exp(-((x-60)**2)/(2*20**2))
    high = 1/(1 + np.exp(-0.4*(x-100)))
    return np.array([low, medium, high])

# ---------------------------
# CPT tables
# ---------------------------

# Age -> Physical activity
CPT_age_physical = np.array([
    [0.2, 0.2, 0.6],   # Young
    [0.2, 0.6, 0.2],   # Middle-aged
    [0.7, 0.2, 0.1]    # Old
])

# Age -> Smoking
CPT_age_smoking = np.array([
    [0.1, 0.3, 0.7],   # Young
    [0.1, 0.5, 0.4],   # Middle-aged
    [0.6, 0.2, 0.2]    # Old
])

# Physical activity + Smoking -> Cancer
CPT_lifestyle_cancer = np.array([
    [[0.2,0.4,0.4],[0.2,0.3,0.5],[0.2,0.2,0.6]],  # Low-active
    [[0.4,0.3,0.3],[0.3,0.2,0.5],[0.1,0.4,0.5]],  # Medium-active
    [[0.3,0.4,0.3],[0.1,0.3,0.6],[0.2,0.3,0.5]]   # High-active
])

# Oncogenes CPT (clusters x risk)
CPT_oncogenes = np.array([
    [0.2,0.5,0.3],
    [0.1,0.2,0.7],
    [0.7,0.2,0.1],
    [0.2,0.3,0.5]
])

# Tumor suppressors CPT (clusters x risk)
CPT_suppressors = np.array([
    [0.3,0.5,0.2],
    [0.7,0.2,0.1],
    [0.1,0.2,0.7],
    [0.2,0.3,0.5]
])

# ---------------------------
# Risk computation function
# ---------------------------
def compute_fuzzy_risk(age, physical, smoking, oncogene_clusters, suppressor_clusters):
    
    # Membership degrees
    mu_age = age_membership(age)
    mu_physical = physical_membership(physical)
    mu_smoke = smoking_membership(smoking)
    
    # CPT for lifestyle -> cancer
    # Compute weighted P(Ph|Age) and P(S|Age)
    P_ph = mu_age @ CPT_age_physical
    P_smoke = mu_age @ CPT_age_smoking
    
    # Combine lifestyle memberships
    lifestyle_prob = np.zeros(3)
    for i, ph in enumerate(P_ph):
        for j, s in enumerate(P_smoke):
            weight = mu_physical[i]*mu_smoke[j]
            lifestyle_prob += weight * CPT_lifestyle_cancer[i,j,:]
    lifestyle_prob /= np.sum(lifestyle_prob)  # normalize
    
    # CPT for genes
    oncogene_prob = np.sum(np.array(oncogene_clusters)[:,None] * CPT_oncogenes, axis=0)
    suppressor_prob = np.sum(np.array(suppressor_clusters)[:,None] * CPT_suppressors, axis=0)
    
    gene_prob = 0.5*oncogene_prob + 0.5*suppressor_prob
    
    # Combine lifestyle + gene
    final_prob = 0.5*lifestyle_prob + 0.5*gene_prob
    
    # Normalize
    final_prob /= np.sum(final_prob)
    
    return final_prob

# ---------------------------
# Example usage
# ---------------------------
age = 74
physical = 0
smoking = 2

oncogene_clusters = [0.2164, 0.0467, 0.6672, 0.0697]
suppressor_clusters = [0.9889, 0.0017, 0.0053, 0.0041]

risk = compute_fuzzy_risk(age, physical, smoking, oncogene_clusters, suppressor_clusters)
print("Fuzzy lung cancer risk (Low, Medium, High):", risk)
