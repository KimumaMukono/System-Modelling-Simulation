from pyams.lib import circuit
from pyams.models import Inductor, CapacitorIc
from math import pi

# Define components
L1 = Inductor("out","0")
C1 = CapacitorIc("out","0")

# Set component values
L1.L += 1/pi
C1.C += 1/pi
C1.Ic += 5  # Initial capacitor charge

# Create circuit and add elements
circuit = circuit()
circuit.addElements({'L1': L1, 'C1': C1})

# Set output for plotting
circuit.setOutPuts("out")

# Perform transient analysis
circuit.analysis(mode="tran", start=0, stop=6, step=0.05)
circuit.run()
circuit.plot()