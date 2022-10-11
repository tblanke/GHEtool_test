import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from GHEtool import Borefield
from GHEtool.VariableClasses import FluidData, GroundData, PipeData

# initiate parameters
ground_data = GroundData(100, 6, 3, 10, 0.12, 10, 12, 2.4 * 10 ** 6)  # ground data with an inaccurate guess of 100m for the depth of the borefield
pipe_data = PipeData(1, 0.015, 0.02, 0.4, 0.05, 0.075, 2, pipe_roughness=1e-6)

# initiate borefield model
borefield = Borefield()
borefield.set_ground_parameters(ground_data)
borefield.set_pipe_parameters(pipe_data)

# initialise variables
R_fp = []
R_p = []
Rb = []

# load data EED
data_EED = pd.read_csv("resistances_EED.csv", sep=";")

mfr_range = np.arange(0.05, 0.55, 0.05)

# calculate effective borehole thermal resistance (Rb*)
for mfr in mfr_range:
    fluid_data = FluidData(mfr, 0.568, 998, 4180, 1e-3)
    borefield.set_fluid_parameters(fluid_data)
    Rb.append(borefield.calculate_Rb())
    R_p.append(borefield.R_p)
    R_fp.append(borefield.R_f)

# make figure
plt.figure()
plt.plot(R_fp, 'r+', label="GHEtool")
plt.plot(data_EED["R_fp"], 'bo', label="EED")
plt.xlabel("Mass flow rate per borehole l/s")
plt.ylabel("Fluid-pipe resistance resistance mK/W")
plt.title("Comparison R_fp from GHEtool with EED")
plt.legend()

plt.figure()
plt.plot(mfr_range, (R_fp - data_EED["R_fp"])/data_EED["R_fp"]*100, 'bo')
plt.xlabel("Mass flow rate per borehole l/s")
plt.ylabel("Difference in fluid-pipe resistance %")
plt.title("Comparison R_fp from GHEtool with EED (relative)")

plt.figure()
plt.plot(Rb, 'r+', label="GHEtool")
plt.plot(data_EED["Rb*"], 'bo', label="EED")
plt.xlabel("Mass flow rate per borehole l/s")
plt.ylabel("Effective borehole thermal resistance mK/W")
plt.title("Comparison Rb* from GHEtool with EED")
plt.legend()

plt.figure()
plt.plot(mfr_range, (Rb - data_EED["Rb*"])/data_EED["Rb*"]*100, 'bo')
plt.xlabel("Mass flow rate per borehole l/s")
plt.ylabel("Difference in effective borehole thermal resistance %")
plt.title("Comparison Rb* from GHEtool with EED (relative)")

plt.show()
