# Antenna Radiation Pattern Simulation

This repository contains a Python script to simulate and visualize the radiation pattern of a half-wave dipole antenna. The simulation includes a 3D surface plot and a 2D polar plot, with an animation of the 3D view to enhance visualization.

## Features
- Models the radiation pattern of a half-wave dipole antenna at 1 GHz.
- Generates a 3D surface plot of the radiation pattern.
- Creates a 2D polar plot for the E-plane.
- Animates the 3D plot by rotating the view angle.
- Uses NumPy for calculations and Matplotlib for visualization.

## Prerequisites
- Python 3.6 or higher
- Required Python packages:
  - `numpy`
  - `matplotlib`
- Optional (for saving animation):
  - `ffmpeg-python` (for saving the animation as a video)
  - FFmpeg installed on your system

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/KimumaMukono/Applied_Mathematics_Modelling/antenna-radiation-pattern.git
   cd antenna-radiation-pattern
   ```
2. Install the required Python packages:
   ```bash
   pip install numpy matplotlib
   ```
3. (Optional) For saving animations, install FFmpeg and the Python package:
   ```bash
   pip install ffmpeg-python
   ```
   Ensure FFmpeg is installed on your system. On Windows, you may need to download it from [FFmpeg's website](https://ffmpeg.org/download.html). On macOS/Linux, use:
   ```bash
   # macOS (using Homebrew)
   brew install ffmpeg
   # Ubuntu
   sudo apt-get install ffmpeg
   ```

## Usage
1. Run the Python script to generate the visualization:
   ```bash
   python antenna_radiation.py
   ```
2. The script will display two plots:
   - A 3D surface plot of the radiation pattern, animated to rotate around the z-axis.
   - A 2D polar plot showing the radiation pattern in the E-plane.
3. (Optional) To save the animation as a video, uncomment the following line in `antenna_radiation.py`:
   ```python
   # ani.save('radiation_pattern.mp4', writer='ffmpeg')
   ```
   Ensure FFmpeg is installed, then run the script again.

## Mathematical Basis
The simulation is based on the following key equations:
- Wavelength: \(\lambda = \frac{c}{f}\), where \(c = 3 \times 10^8 \, \text{m/s}\), \(f = 1 \, \text{GHz}\).
- Wave number: \(k = \frac{2\pi}{\lambda}\).
- Dipole length: \(L = \frac{\lambda}{2}\).
- Normalized power pattern: \(P(\theta) = \left( \frac{\cos\left(\frac{\pi}{2} \cos\theta\right)}{\sin\theta} \right)^2\).

See the [equations documentation](equations.md) for detailed explanations.

## File Structure
- `antenna_radiation.py`: Main Python script for simulation and visualization.
- `README.md`: This file, providing project overview and instructions.
- `equations.md` (optional): Documentation of the mathematical equations used.

## Customization
- Modify the `frequency` variable in `antenna_radiation.py` to simulate different frequencies.
- Adjust the `interval` parameter in `animation.FuncAnimation` to change the rotation speed of the 3D plot.
- Update the grid resolution (`theta` and `phi` linspace) for higher or lower detail in the plots.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for bug fixes, improvements, or new features.

## Contact
For questions or feedback, please open an issue on this repository or contact [your-email@example.com](mailto:your-email@example.com).