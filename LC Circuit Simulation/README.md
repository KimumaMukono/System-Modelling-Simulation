
# LC Oscillator Simulation

## Overview

This repository simulates an LC oscillator using PyAMS. It models an inductor (L) and capacitor (C) circuit that oscillates by transferring energy between the capacitor's electric field and the inductor's magnetic field. The simulation assumes zero resistance, producing continuous sinusoidal oscillations.

The PyAMS script performs transient analysis over a time range of 0 to 6 seconds with a step size of 0.05 seconds and plots the output voltage at the "out" node. The script uses the `pyams.lib` module to create and simulate the LC circuit, visualizing the charge and current oscillations over time.

## Getting Started

Follow these steps to set up and run the simulation:

### 1. Clone the repository:

```bash
git clone https://github.com/KimumaMukono/Applied_Mathematics_Modelling
```

### 2. Install PyAMS and dependencies:

To install PyAMS and its dependencies, you can use `pip` or `conda` (depending on your environment):

```bash
pip install pyams
```

### 3. Run the simulation:

You can run the simulation using either a Jupyter Notebook or a Python script. The output will be a plot of the voltage across the capacitor over time.

To run the Python script:

```bash
python lc_oscillator_simulation.py
```

### 4. View the Results:

The simulation will generate a plot showing the voltage oscillations of the LC circuit over the specified time range.

## License

This project is licensed under the [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).
