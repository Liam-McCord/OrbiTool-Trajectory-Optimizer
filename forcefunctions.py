import numpy as np  

def thrust_function(sim,i):
    y_new = np.zeros(6)
    impulse = 0
    impulse += sim.rocket.step_thrust_distribution[i]
    acceleration = impulse / sim.rocket.mass
    y_new[5] += acceleration * sim.dt
    return y_new

def grav_function(sim, y, grav_const):
    y_new = np.zeros(6)
    r_h = y[2] + sim.planet_radius
    accel = ((grav_const * sim.body_mass) / (r_h ** 2))
    y_new[5] += -1 * accel * sim.dt
    return y_new

def drag_function(sim, y, p, drag_coeff, ref_area):
    # A very simple drag function for the rocket, UNFINISHED
    # Assuming p is constant for the first test
    # F = MA therefrore A = F / M
    y_new = np.zeros(6)
    #print(y)
    accel = (-0.5 * p * (np.linalg.norm(y[3:]) ** 2) * drag_coeff * ref_area) / sim.rocket.mass
    #print(accel)
    accel_unit_vector = y[3:] / np.linalg.norm(y[3:])
    #print(accel_unit_vector)
    #print(accel_unit_vector)
    y_new[3:] += accel * accel_unit_vector * sim.dt
    #print(y_new)
    return y_new
    # Need  
    
    
    
    



    