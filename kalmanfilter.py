import numpy as np
import matplotlib.pyplot as plt
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import rts_smoother


def add_noise(path, t_list):
    """Simulates noise for the rocket path readings for realism purposes."""
    noisy_path = path
    noisy_path[2][:] = path[2][:] + np.random.normal(0.2,0.2,len(t_list)) 
    return noisy_path

def filter_noise(noisy_path):
    """Filters noisy paths via a Kalman Filter, then smooths them out with a RTS smoother."""
    f = KalmanFilter (dim_x=2, dim_z=1)

    f.F = np.array([[1.,1.],
                    [0.,1.]])

    f.H = np.array([[1.,0.]])

    f.P = np.array([[1000.,    0.],
                    [   0., 1000.] ])

    f.R = np.array([[500.]])

    f.Q = Q_discrete_white_noise(dim=2, dt=0.1, var=0.13) # Extra noise for the path
    
    mu, cov, _, _ = f.batch_filter(noisy_path) # Filters all of the rocket's path in a batch rather than individually, which is more compact and faster.
    M,P,C, _ = f.rts_smoother(mu, cov) # Smooths out the path using a Rauch–Tung–Striebel smoother (RTS) with a backward pass.
    
    
    return np.array(M[:,0]).T[0] # Returns RTS smoothed and Kalman filtered path in the right dimension for the plotting functions to accept it.