import numpy as np
import helperfunctions as hf

g = -9.81
n_max = 5
grav_const = 6.67e-11
earth_mass = 5.972e24


class Rocket():
    def __init__(self, name, y, mass, thrust_function, start_thrust, rough_burn_time, max_steps, dt):
        self.name = name
        self.y = y
        self.mass = mass
        self.thrust_func = thrust_function
        self.start_thrust = start_thrust
        self.rough_burn_time = rough_burn_time
        self.max_steps = max_steps
        self.step_thrust_distribution = np.zeros(self.max_steps * 2)
        self.dt = dt
        self.calculate_impulse()

    def calculate_impulse(self):
        step_thrust_chunks = int(self.rough_burn_time // self.dt)
        thrust_beginning = int(self.start_thrust // self.dt)
        for i in range(0,step_thrust_chunks):
            impulse_dt = hf.trap_integrator(i * self.dt, self.dt, 50, self.thrust_func)
            self.step_thrust_distribution[thrust_beginning + i] = impulse_dt
            
class Simulation(Rocket):
    def __init__(self, body_mass, rocket, planet_radius, max_steps, dt, thrust_graph=[]):
        self.body_mass = body_mass
        self.rocket = rocket
        self.planet_radius = planet_radius
        self.max_steps = max_steps
        self.dt = dt
        self.thrust_graph = []
        
    def run_simulation(self):
        t_list, y, i_final = hf.RK4(self, self.rocket.y, hf.ff.force_function, self.max_steps, self.dt)
        return t_list, y, i_final