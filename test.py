import numpy as np

# 2.1. In vitro characterization
# Preosteoblasts seeding and culture conditions
initial_density = 2.5 * 10**3  # cells/cm^2
well_area = 1.5 * 1.5  # cm^2
initial_cell_count = initial_density * well_area

medium_supplement = {
    'alpha_medium': 'minimum essential alpha medium',
    'fetal_bovine_serum': 0.1,  # 10%
    'penicillin_streptomycin': 0.01  # 1%
}

culture_conditions = {
    'CO2': 0.05,  # 5%
    'temperature': 37  # 37°C
}

differentiation_inducers = {
    'ascorbic_acid': 50,  # μg/mL
    'beta_glycerophosphate': 10  # mM
}

feeding_interval = 3  # days

# Bone formation quantification
time_points = [1, 2, 4, 8, 16, 26]  # days

# 2.2. CA model
M = 75
N = 75
cell_size = {
    'osteocyte': (5, 20),  # μm
    'osteoblast': (20, 30)  # μm
}

T = 26  # days

# CA model initialization
matrix_dim = (M, N, T + 1)
matrix_B = np.zeros(matrix_dim)

# Random number selection
random_mean = 5 
random_std = 2

# Simulation
for t in range(T + 1):
    # Randomly select i number of sites for mineralization
    i = int(np.random.normal(random_mean, random_std))
    selected_sites = np.random.choice(range(M * N), size=i, replace=False)
    
    # Deposit matrix material at selected sites
    matrix_B[selected_sites] = np.random.uniform(0, 1, size=i)
    
    # Check for bone formation at each site
    for site in selected_sites:
        x, y = site // N, site % N
        neighbors = matrix_B[max(0, x-3):min(M, x+4), max(0, y-3):min(N, y+4), t]
        
        if matrix_B[x, y, t] < np.mean(neighbors):
            matrix_B[x, y, t+1] += 1

# plot the matrix_B matrix
plt.imshow(matrix_B[:, :, 26])
plt.show()