import rocket as rt
import helperfunctions as hf
import plotting as pt
import numpy as np
import kalmanfilter as kf

test_rocket = rt.Rocket("rocket", np.array([30,20,30,0,5,50]), 10, lambda t : 15 * ((t-20) ** 2 + 4 * t + 3), 80, 30, 10000, 0.1)
# lambda t : (t-20) ** 2 + 4 * t + 3
Bob_Sim = rt.Simulation(5.972e24, test_rocket, 6371000, 800, 0.1)
t_list, real_path, final_i = Bob_Sim.run_simulation()

noisy_path = real_path.copy()
kf.add_noise(noisy_path, t_list)

denoised_path = kf.filter_noise(noisy_path[2])
#print(denoised_path)
pt.plot_path(noisy_path, denoised_path, real_path, t_list, test_rocket, final_i)