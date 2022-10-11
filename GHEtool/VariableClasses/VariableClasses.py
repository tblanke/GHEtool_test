
from typing import Optional
from abc import ABC

class GroundData:
    __slots__ = 'H', 'B', 'k_s', 'Tg', 'Rb', 'N_1', 'N_2', 'flux', 'volumetric_heat_capacity', 'alpha'

    def __init__(self, h: float, b: float, k_s: float, t_g: float, r_b: float, n_1: int, n_2: int,
                 volumetric_heat_capacity: float = 2.4 * 10**6, flux: float = 0.06) -> None:
        """
        Data for storage of ground data

        :param h: Depth of boreholes [m]
        :param b: Borehole spacing [m]
        :param k_s: Ground thermal conductivity [W/m.K]
        :param t_g: Surface ground temperature [deg C]
        (this is equal to the ground temperature at infinity when no heat flux is given (default))
        :param r_b: Equivalent borehole resistance [m K/W]
        :param n_1: Width of rectangular field [#]
        :param n_2: Length of rectangular field [#]
        :param volumetric_heat_capacity: The volumetric heat capacity of the ground (J/m3K)
        :param flux: the geothermal heat flux (W/m2)
        :return: None
        """
        self.H = h  # m
        self.B = b  # m
        self.k_s = k_s  # W/mK
        self.Tg = t_g  # °C
        self.Rb = r_b  # mK/W
        self.N_1 = n_1  # #
        self.N_2 = n_2  # #
        self.volumetric_heat_capacity = volumetric_heat_capacity  # J/m3K
        self.alpha = self.k_s / self.volumetric_heat_capacity  # m2/s
        self.flux = flux  # W/m2

    def __eq__(self, other):
        if not isinstance(other, GroundData):
            return False
        for i in self.__slots__:
            if getattr(self, i) != getattr(other, i):
                return False
        return True


class FluidData:

    __slots__ = 'k_f', 'rho', 'Cp', 'mu', 'mfr'

    def __init__(self, *, mass_flow_rate: float, conductivity_fluid: float, density: float, heat_capacity: float, viscosity: float) -> None:
        """
        Data for storage of ground data

        :param mass_flow_rate: Mass flow rate per borehole [kg/s]
        :param conductivity_fluid: Thermal Conductivity [W/mK]
        :param density: Density [kg/m3]
        :param heat_capacity: Thermal capacity [J/kgK]
        :param viscosity: EDynamic viscosity [Pa/s]
        :return: None
        """

        self.k_f = conductivity_fluid  # Thermal conductivity W/mK
        self.mfr = mass_flow_rate  # Mass flow rate per borehole kg/s
        self.rho = density  # Density kg/m3
        self.Cp = heat_capacity    # Thermal capacity J/kgK
        self.mu = viscosity    # Dynamic viscosity Pa/s

    def __eq__(self, other):
        if not isinstance(other, FluidData):
            return False
        for i in self.__slots__:
            if getattr(self, i) != getattr(other, i):
                return False
        return True


class PipeData(ABC):
    __slots__ = 'r_in', 'r_out', 'k_p', 'D_s', 'r_b', 'number_of_pipes', 'epsilon', 'k_g', 'D'

    def __init__(self, conductivity_grout: float, inner_radius: float, outer_radius: float, conductivity_pipe: float, pipe_distance: float,
                 borehole_radius: float, number_of_pipes, pipe_roughness: float = 1e-6, burial_depth: float = 4) -> None:
        """
        Data for storage of ground data

        :param conductivity_grout: Grout thermal conductivity [W/mK]
        :param inner_radius: Inner pipe radius [m]
        :param outer_radius: Outer pipe radius [m]
        :param conductivity_pipe: Pipe thermal conductivity [W/mK]
        :param pipe_distance: Distance of the pipe until center [m]
        :param borehole_radius: Borehole radius [m]
        :param number_of_pipes: Number of pipes [#] (single U-tube: 1, double U-tube:2)
        :param pipe_roughness: Pipe roughness [m]
        :param burial_depth: burial depth [m]
        :return: None
        """
        self.k_g: float = conductivity_grout  # grout thermal conductivity W/mK
        self.r_in: float = inner_radius  # inner pipe radius m
        self.r_out: float = outer_radius  # outer pipe radius m
        self.k_p: float = conductivity_pipe  # pipe thermal conductivity W/mK
        self.D_s: float = pipe_distance  # distance of pipe until center m
        self.r_b: float = borehole_radius  # borehole radius m
        self.number_of_pipes: int = number_of_pipes  # number of pipes #
        self.epsilon: float = pipe_roughness  # pipe roughness m
        self.D: float = burial_depth  # burial depth m

    def __eq__(self, other):
        if not isinstance(other, FluidData):
            return False
        for i in self.__slots__:
            if getattr(self, i) != getattr(other, i):
                return False
        return True


class MultipleUPPipeData(PipeData):
    """Pipe Data for multiple U pipes"""

    __slots__ = PipeData.__slots__


class CoaxialPipe(PipeData):

    __slots__ = PipeData.__slots__ + ('r_in_b', 'k_o')

    def __init__(self, conductivity_grout: float, inner_radius: float, outer_radius: float, conductivity_pipe: float, pipe_distance: float,
                 borehole_radius: float, borehole_pipe_inner_radius: float, conductivity_outer_pipe: float, pipe_roughness: float = 1e-6,
                 burial_depth: float = 4) -> None:
        """
        Data for storage of ground data

        :param conductivity_grout: Grout thermal conductivity [W/mK]
        :param inner_radius: Inner pipe radius [m]
        :param outer_radius: Outer pipe radius [m]
        :param conductivity_pipe: Pipe thermal conductivity [W/mK]
        :param pipe_distance: Distance of the pipe until center [m]
        :param borehole_radius: Borehole radius [m]
        :param pipe_roughness: Pipe roughness [m]
        :param burial_depth: burial depth [m]
        :return: None
        """
        # check if pipe data is valid
        super().__init__(conductivity_grout, inner_radius, outer_radius, conductivity_pipe, pipe_distance, borehole_radius, 0, pipe_roughness,
                         burial_depth)
        self.r_in_b: float = borehole_pipe_inner_radius
        self.k_o: float = conductivity_outer_pipe
