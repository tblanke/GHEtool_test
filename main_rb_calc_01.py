import pygfunction as gt
import numpy as np
from math import pi
import pandas as pd


def main():
    results = np.zeros((200, 3))
    for d in range(200):
        borehole = gt.boreholes.Borehole(d + 5, 6, 0.075, 0, 0)
        mfr = 0.5
        r_in = 0.019
        r_out = 0.022
        D_s = .042
        R_p: float = gt.pipes.conduction_thermal_resistance_circular_pipe(r_in, r_out, 0.42)
        h_f: float = gt.pipes.convective_heat_transfer_coefficient_circular_pipe(mfr / 2, r_in,
                                                                                 0.001,
                                                                                 1000, 0.5, 4182, 0.000_000_1)
        R_f: float = 1. / (h_f * 2 * pi * r_in)
        resistances = [R_f + R_p]
        dt: float = pi / float(2)
        pos: list = [(0., 0.)] * 2 * 2
        for i in range(2):
            pos[i] = (D_s * np.cos(2.0 * i * dt + pi), D_s * np.sin(2.0 * i * dt + pi))
            pos[i + 2] = (D_s * np.cos(2.0 * i * dt + pi + dt), D_s * np.sin(2.0 * i * dt + pi + dt))

        pipe = gt.pipes.MultipleUTube(pos, r_in, r_out, borehole, 1.5, 1.5,
                                      resistances[0], 2, J=2)

        results[d, 0] = d + 5
        results[d, 1] = pipe.effective_borehole_thermal_resistance(mfr, 4182)
        results[d, 2] = 0
    pd.DataFrame(results).to_csv('Rb_2U.csv')
    """
    if self.pipe_data.__class__ == PipeData or isinstance(self.pipe_data, MultipleUPPipeData):
        pipe = gt.pipes.MultipleUTube(self.pos, self.pipe_data.r_in, self.pipe_data.r_out, borehole, self.k_s, self.pipe_data.k_g,
                                      self.resistances[0], 2, J=2)
    elif isinstance(self.pipe_data, CoaxialPipe):
    

    if self.pipe_data.__class__ == PipeData or isinstance(self.pipe_data, MultipleUPPipeData):
        # initiate pipe
        R_p: float = gt.pipes.conduction_thermal_resistance_circular_pipe(self.pipe_data.r_in, self.pipe_data.r_out, 0.42)
        h_f: float = gt.pipes.convective_heat_transfer_coefficient_circular_pipe(self.fluid_data.mfr / 2, self.pipe_data.r_in,
                                                                                 0.001,
                                                                                 1000, 0.5, 4182,
                                                                                 self.pipe_data.epsilon)
        R_f: float = 1. / (h_f * 2 * pi * self.pipe_data.r_in)
        self.resistances = [R_f + R_p]
    if isinstance(self.pipe_data, CoaxialPipe):
    """
    results = np.zeros((200, 3))
    for d in range(200):
        borehole = gt.boreholes.Borehole(d + 5, 6, 0.075, 0, 0)
        mfr = 2
        r_in = 0.035
        r_in_out = 0.065
        r_out = 0.039
        r_out_out = 0.07
        h_f_inner = gt.pipes.convective_heat_transfer_coefficient_circular_pipe(mfr, r_in, 0.001, 1000, 0.5, 4182, 0.000_000_1)
        h_f_outer = gt.pipes.convective_heat_transfer_coefficient_concentric_annulus(mfr, r_out, r_in_out, 0.001, 1000, 0.5, 4182, 0.000_000_1)
        R_inner_pipe = gt.pipes.conduction_thermal_resistance_circular_pipe(r_in, r_out, 0.42)
        R_f_inner = 1. / (h_f_inner * 2 * pi * r_in)
        R_f_outer_in = 1. / (h_f_outer[0] * 2 * pi * (r_in_out - r_out))
        R_f_outer_out = 1. / (h_f_outer[1] * 2 * pi * (r_in_out - r_out))
        R_outer_pipe = gt.pipes.conduction_thermal_resistance_circular_pipe(r_in_out, r_out_out, 40)
        resistances = [R_f_inner + R_f_outer_in + R_inner_pipe, R_outer_pipe + R_f_outer_out]
        pipe = gt.pipes.Coaxial(pos=[(0, 0)],
                                r_in=np.array([r_in, r_in_out]),
                                r_out=np.array([r_out, r_out_out]),
                                borehole=borehole, k_s=1.5, k_g=1.5, R_ff=resistances[0], R_fp=resistances[1], J=2)

        results[d, 0] = d + 5
        results[d, 1] = pipe.effective_borehole_thermal_resistance(mfr, 4182)
        results[d, 2] = R_outer_pipe + R_f_outer_out
    pd.DataFrame(results).to_csv('Rb.csv')


if __name__ == "__main__":
    main()
