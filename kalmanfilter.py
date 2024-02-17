import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import rts_smoother
def add_noise(path, t_list):
    noisy_path = path
    noisy_path[2][:] = path[2][:] + np.random.normal(0.2,0.2,len(t_list)) 
    return noisy_path

def filter_noise(noisy_path):
    f = KalmanFilter (dim_x=2, dim_z=1)

    f.F = np.array([[1.,1.],
                    [0.,1.]])

    f.H = np.array([[1.,0.]])

    f.P = np.array([[1000.,    0.],
                    [   0., 1000.] ])

    f.R = np.array([[500.]])

    f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13) # Extra noise for the path
    
    denoised_path = []    

    for z in noisy_path:
        f.predict()
        f.update(z)
        denoised_path.append(f.x[0,0])

    return denoised_path    
