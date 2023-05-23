# Bone Formation Using Cellular Automata
This is a Python script that simulates bone formation in a tissue culture well. The simulation is based on a cellular automaton model, where each cell represents a site in the tissue culture well. The model takes into account the mechanical tension in the tissue culture well, as well as the influence of neighboring cells on each other.

## Getting Started
To run the simulation, you will need to have Python 3 installed on your computer. You will also need to install the following Python packages:

- numpy
- matplotlib

You can install these packages using pip:

    pip install numpy matplotlib

Once you have installed the required packages, you can run the simulation by running the ```main.py``` script:
    
    python main.py


## Usage
When you run the main.py script, a plot will be displayed showing the tissue culture well at time step 0. You can use the slider at the bottom of the plot to change the time step and see how the tissue culture well changes over time.

## Customization
You can customize the simulation by changing the parameters at the beginning of the main.py script. Here are some of the parameters you can change:

- ```M``` and ```N```: The dimensions of the tissue culture well (in cells).
- ```T```: The number of time steps to simulate.
neighborhood_size: The size of the neighborhood around each cell that influences its behavior.
- ```mean``` and ```std```: The mean and standard deviation of the number of initial clusters in the tissue culture well.
- ```mechanical_tension```: The mechanical tension in the tissue culture well.

You can also customize the behavior of the cells by modifying the update mechanism in the main.py script.