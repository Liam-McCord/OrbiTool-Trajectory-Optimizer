import numpy as np
import forcefunctions as ff


def RK4(sim, y_initial, f, t, dt):
    """Implementation of a 4th-order Runge Kutta method."""  
    m = y_initial.shape[0]
    max_steps = int(t/dt)
    tlist = np.linspace(0, t, max_steps)
    y = np.zeros((m, max_steps), float)
    y[:, 0] = y_initial
    for i in range(0,max_steps-1):
        k1 = f(sim, y[:, i], t + i*dt,i)
        k2 = f(sim, y[:, i] + (0.5 * dt * k1),i*dt,i)
        k3 = f(sim, y[:, i] + 0.5 * dt * k2,i*dt,i)
        k4 = f(sim, y[:, i] + dt * k3,i*dt,i)
        y[:, i + 1] = y[:, i] + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        if y[2, i] < 0:
            break
    return(tlist, y, i)

def trap_integrator(t, dt, num_traps, thrust_func):
    """Gives impulse from a thrust equation."""
    
    dx = dt / num_traps
    impulse = 0
    x = t
    for trap in range(num_traps):
        left = thrust_func(x)
        right = thrust_func(x + dx)
        impulse += ((left + right) / 2) * dx
    return(impulse)

def force_function(sim,y,t,i):
    # combines the individual force functions into a total acceleration.
    y_new = np.zeros(6)
    y_new += ff.grav_function(sim, y)
    y_new += ff.thrust_function(sim, i)
    sim.thrust_graph.append(y_new[5])
    y_new[:3] += (y[3:] + y_new[3:]) * sim.dt
    return y_new