"""
This document compares both the L2 sizing method of (Peere et al., 2021) with a more general L3 sizing.
The comparison is based on speed and relative accuracy in the result.
"""
if __name__ == "__main__":

    import time

    import numpy as np

    from GHEtool import Borefield, GroundData

    number_of_iterations = 100
    max_value_cooling = 700
    max_value_heating = 800

    # initiate the arrays
    results_L2 = np.empty(number_of_iterations)
    results_L3 = np.empty(number_of_iterations)
    difference_results = np.empty(number_of_iterations)

    monthly_load_cooling_array = np.empty((number_of_iterations, 12))
    monthly_load_heating_array = np.empty((number_of_iterations, 12))
    peak_load_cooling_array = np.empty((number_of_iterations, 12))
    peak_load_heating_array = np.empty((number_of_iterations, 12))

    # populate arrays with random values
    for i in range(number_of_iterations):
        for j in range(12):
            monthly_load_cooling_array[i, j] = np.random.randint(0, max_value_cooling)
            monthly_load_heating_array[i, j] = np.random.randint(0, max_value_heating)
            peak_load_cooling_array[i, j] = np.random.randint(monthly_load_cooling_array[i, j], max_value_cooling)
            peak_load_heating_array[i, j] = np.random.randint(monthly_load_heating_array[i, j], max_value_heating)

    # initiate borefield model
    data = GroundData(110, 6, 3, 10, 0.2, 10, 12, 2.4 * 10**6)

    # Monthly loading values
    peak_cooling = np.array([0.0, 0, 34.0, 69.0, 133.0, 187.0, 213.0, 240.0, 160.0, 37.0, 0.0, 0.0])  # Peak cooling in kW
    peak_heating = np.array([160.0, 142, 102.0, 55.0, 0.0, 0.0, 0.0, 0.0, 40.4, 85.0, 119.0, 136.0])  # Peak heating in kW

    # annual heating and cooling load
    annual_heating_load = 300 * 10**3  # kWh
    annual_cooling_load = 160 * 10**3  # kWh

    # percentage of annual load per month (15.5% for January ...)
    monthly_load_heating_percentage = np.array([0.155, 0.148, 0.125, 0.099, 0.064, 0.0, 0.0, 0.0, 0.061, 0.087, 0.117, 0.144])
    monthly_load_cooling_percentage = np.array([0.025, 0.05, 0.05, 0.05, 0.075, 0.1, 0.2, 0.2, 0.1, 0.075, 0.05, 0.025])

    # resulting load per month
    monthly_load_heating = annual_heating_load * monthly_load_heating_percentage  # kWh
    monthly_load_cooling = annual_cooling_load * monthly_load_cooling_percentage  # kWh

    # create the borefield object
    borefield = Borefield(
        simulation_period=20, peak_heating=peak_heating, peak_cooling=peak_cooling, baseload_heating=monthly_load_heating, baseload_cooling=monthly_load_cooling
    )

    borefield.set_ground_parameters(data)

    # set temperature boundaries
    borefield.set_max_ground_temperature(16)  # maximum temperature
    borefield.set_min_ground_temperature(0)  # minimum temperature

    # size according to L2 method
    start_L2 = time.time()
    for i in range(number_of_iterations):
        borefield.set_baseload_cooling(monthly_load_cooling_array[i])
        borefield.set_baseload_heating(monthly_load_heating_array[i])
        borefield.set_peak_cooling(peak_load_cooling_array[i])
        borefield.set_peak_heating(peak_load_heating_array[i])
        results_L2[i] = borefield.size(100, L2_sizing=True)
    end_L2 = time.time()

    # size according to L3 method
    start_L3 = time.time()
    for i in range(number_of_iterations):
        borefield.set_baseload_cooling(monthly_load_cooling_array[i])
        borefield.set_baseload_heating(monthly_load_heating_array[i])
        borefield.set_peak_cooling(peak_load_cooling_array[i])
        borefield.set_peak_heating(peak_load_heating_array[i])
        results_L3[i] = borefield.size(100, L3_sizing=True)
    end_L3 = time.time()

    print("Time for sizing according to L2:", end_L2 - start_L2, "s (or ", round((end_L2 - start_L2) / number_of_iterations * 1000, 3), "ms/sizing)")
    print("Time for sizing according to L3:", end_L3 - start_L3, "s (or ", round((end_L3 - start_L3) / number_of_iterations * 1000, 3), "ms/sizing)")

    # calculate differences
    for i in range(number_of_iterations):
        difference_results[i] = results_L3[i] - results_L2[i]

    print(
        "The maximal difference between the sizing of L2 and L3 was:",
        np.round(np.max(difference_results), 3),
        "m or",
        np.round(np.max(difference_results) / results_L2[np.argmax(difference_results)] * 100, 3),
        "% w.r.t. the L2 sizing.",
    )
    print(
        "The mean difference between the sizing of L2 and L3 was:",
        np.round(np.mean(difference_results), 3),
        "m or",
        np.round(np.mean(difference_results) / np.mean(results_L2) * 100, 3),
        "% w.r.t. the L2 sizing.",
    )
