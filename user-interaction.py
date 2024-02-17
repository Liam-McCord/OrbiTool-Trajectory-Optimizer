import rocket as rt
import helperfunctions as hf
import plotting as pt
import numpy as np
import kalmanfilter as kf

test_rocket = rt.Rocket("rocket", np.array([30,20,30,0,5,50]), 10, lambda t : 15 * ((t-20) ** 2 + 4 * t + 3), 80, 30, 10000, 0.1)
# lambda t : (t-20) ** 2 + 4 * t + 3
Bob_Sim = rt.Simulation(5.972e24, test_rocket, 6371000, 800, 0.1)
t_list, plotted_path, final_i = Bob_Sim.run_simulation()
plotted_path = kf.add_noise(plotted_path, t_list)
denoised_path = kf.filter_noise(plotted_path[2])
#print(denoised_path)
pt.plot_path(plotted_path, denoised_path, t_list, test_rocket, final_i)