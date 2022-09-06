"""
This document compares the speed of the L2 sizing method of (Peere et al., 2021) with and without the precalculated gfunction data.
This is done for two fields with different sizes. It shows that, specifically for the larger fields, the precalculated data is way faster.
"""

import time

from GHEtool import Borefield, GroundData


def test_64_boreholes():
    data = GroundData(110, 6, 3, 10, 0.2, 8, 8, 2.4 * 10**6)

    # monthly loading values
    peak_cooling = [
        0.0,
        0,
        34.0,
        69.0,
        133.0,
        187.0,
        213.0,
        240.0,
        160.0,
        37.0,
        0.0,
        0.0,
    ]  # Peak cooling in kW
    peak_heating = [
        160.0,
        142,
        102.0,
        55.0,
        0.0,
        0.0,
        0.0,
        0.0,
        40.4,
        85.0,
        119.0,
        136.0,
    ]  # Peak heating in kW

    # annual heating and cooling load
    annual_heating_load = 300 * 10**3  # kWh
    annual_cooling_load = 160 * 10**3  # kWh

    # percentage of annual load per month (15.5% for January ...)
    monthly_load_heating_percentage = [
        0.155,
        0.148,
        0.125,
        0.099,
        0.064,
        0.0,
        0.0,
        0.0,
        0.061,
        0.087,
        0.117,
        0.144,
    ]
    monthly_load_cooling_percentage = [
        0.025,
        0.05,
        0.05,
        0.05,
        0.075,
        0.1,
        0.2,
        0.2,
        0.1,
        0.075,
        0.05,
        0.025,
    ]

    # resulting load per month
    monthly_load_heating = list(map(lambda x: x * annual_heating_load, monthly_load_heating_percentage))  # kWh
    monthly_load_cooling = list(map(lambda x: x * annual_cooling_load, monthly_load_cooling_percentage))  # kWh

    # create the borefield object
    borefield = Borefield(
        simulation_period=20,
        peak_heating=peak_heating,
        peak_cooling=peak_cooling,
        baseload_heating=monthly_load_heating,
        baseload_cooling=monthly_load_cooling,
    )

    borefield.set_ground_parameters(data)

    # set temperature boundaries
    borefield.set_max_ground_temperature(16)  # maximum temperature
    borefield.set_min_ground_temperature(0)  # minimum temperature

    # size borefield
    t1 = time.time()
    depth_precalculated = borefield.size(100)
    t1_end = time.time()

    ### size without the precalculation

    borefield.use_precalculated_data = False
    # size borefield
    t2 = time.time()
    depth_calculated = borefield.size(100)
    t2_end = time.time()

    print(
        "With precalculated data, the sizing took",
        round(t1_end - t1, 3),
        "s for 64 boreholes.",
    )
    print(
        "Without the precalculated data, the sizing took",
        round(t2_end - t2, 3),
        "s for 64 boreholes.",
    )
    print(
        "The difference in accuracy between the two results is",
        round((depth_calculated - depth_precalculated) / depth_calculated * 100, 3),
        "%.",
    )


def test_10_boreholes():
    data = GroundData(110, 6, 3, 10, 0.2, 2, 5)

    # monthly loading values
    peak_cooling = [
        0.0,
        0,
        3.0,
        9.0,
        13.0,
        20.0,
        43.0,
        30.0,
        16.0,
        7.0,
        0.0,
        0.0,
    ]  # Peak cooling in kW
    peak_heating = [
        16.0,
        14,
        10.0,
        5.0,
        0.0,
        0.0,
        0.0,
        0.0,
        4,
        8.0,
        19.0,
        13.0,
    ]  # Peak heating in kW

    # annual heating and cooling load
    annual_heating_load = 16 * 10**3  # kWh
    annual_cooling_load = 24 * 10**3  # kWh

    # percentage of annual load per month (15.5% for January ...)
    monthly_heating_load_percentage = [
        0.155,
        0.148,
        0.125,
        0.099,
        0.064,
        0.0,
        0.0,
        0.0,
        0.061,
        0.087,
        0.117,
        0.144,
    ]
    monthly_load_cooling_percentage = [
        0.025,
        0.05,
        0.05,
        0.05,
        0.075,
        0.1,
        0.2,
        0.2,
        0.1,
        0.075,
        0.05,
        0.025,
    ]

    # resulting load per month
    monthly_load_heating = list(map(lambda x: x * annual_heating_load, monthly_heating_load_percentage))  # kWh
    monthly_load_cooling = list(map(lambda x: x * annual_cooling_load, monthly_load_cooling_percentage))  # kWh

    # create the borefield object
    borefield = Borefield(
        simulation_period=20,
        peak_heating=peak_heating,
        peak_cooling=peak_cooling,
        baseload_heating=monthly_load_heating,
        baseload_cooling=monthly_load_cooling,
    )

    borefield.set_ground_parameters(data)

    # set temperature boundaries
    borefield.set_max_ground_temperature(16)  # maximum temperature
    borefield.set_min_ground_temperature(0)  # minimum temperature

    # size borefield
    t1 = time.time()
    depth_precalculated = borefield.size(100)
    t1_end = time.time()

    ### size without the precalculation

    borefield.use_precalculated_data = False
    # size borefield
    t2 = time.time()
    depth_calculated = borefield.size(100)
    t2_end = time.time()

    print(
        "With precalculated data, the sizing took",
        round(t1_end - t1, 3),
        "s for 10 boreholes.",
    )
    print(
        "Without the precalculated data, the sizing took",
        round(t2_end - t2, 3),
        "s for 10 boreholes.",
    )
    print(
        "The difference in accuracy between the two results is",
        round((depth_calculated - depth_precalculated) / depth_calculated * 100, 3),
        "%.\n",
    )


if __name__ == "__main__":

    test_10_boreholes()
    test_64_boreholes()
