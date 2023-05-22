import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define parameters
M = 75  # Grid dimensions (rows)
N = 75  # Grid dimensions (columns)
T = 26  # Number of time steps (days)

# Initialize the grid
B = np.zeros((M, N, T+1))  # 3D matrix representing the tissue culture well

# Define the neighborhood
neighborhood_size = 7  # Seven by seven grid surrounding each cell

# Set initial conditions
mean = 10  # Mean value for the number of initial clusters (you can adjust this value)
std = 1  # Standard deviation for the number of initial clusters (you can adjust this value)

i = np.random.normal(mean, std)  # Number of initial clusters
initial_sites = np.random.choice(M*N, int(i), replace=False)  # Randomly select initial sites
B_flat = B.reshape(-1, T+1)  # Flatten the matrix B for easier indexing
B_flat[initial_sites, 0] = np.random.uniform(0, 1, size=int(i))  # Set initial values for selected sites

# Update mechanism
for t in range(T):
    for row in range(M):
        for col in range(N):
            current_value = B[row, col, t]
            neighbor_values = B[max(row-neighborhood_size//2, 0):min(row+neighborhood_size//2+1, M),
                                max(col-neighborhood_size//2, 0):min(col+neighborhood_size//2+1, N),
                                t]
            average_neighbor_value = np.mean(neighbor_values)
            
            if average_neighbor_value > current_value:
                B[row, col, t+1] = current_value + np.random.uniform(0, 1)  # Increase bone formation

# Validate the model against experimental data
# Perform the permutation test or other validation methods

# Visualize the simulation results (optional)
# Create initial plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

simulation_plot = ax.imshow(B[:, :, 0], cmap='hot', interpolation='nearest')
plt.colorbar(simulation_plot)

# Create slider
ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Time Step (T)', 0, T, valinit=0, valstep=1)

# Slider update function
def update_slider(val):
    t = int(slider.val)
    simulation_plot.set_data(B[:, :, t])
    plt.title(f"Bone Formation Simulation (T = {t})")
    fig.canvas.draw_idle()

# Connect slider to update function
slider.on_changed(update_slider)

# Set initial title
plt.title("Bone Formation Simulation (T = 0)")

# Show the plot
plt.show()