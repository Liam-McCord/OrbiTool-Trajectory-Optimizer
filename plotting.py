import matplotlib.pyplot as plt
import numpy as np

def plot_path(plotted_path, denoised_path, t_list, rocket, final_i):
    thrust_graph = plt.axes()
    thrust_graph.plot(np.arange(0,len(plotted_path[5]),1), plotted_path[5])
    
    thrust_graph.set_box_aspect(1)

    thrust_graph.plot(np.arange(0,len(rocket.step_thrust_distribution),1), rocket.step_thrust_distribution)
    thrust_graph.set_box_aspect(1)
    plt.show()

    print(f"Rocket hit the ground at t = {t_list[final_i]} s at a final velocity of {np.linalg.norm(plotted_path[3:][-1])} m/s")

    # Graphing section
    fig = plt.figure(figsize = (9,9))

    ax2 = fig.add_subplot(111, projection='3d')
    ax2.set_box_aspect([1,1,1])

    graphcounter = 0
    velocity_map = np.array(((plotted_path[0][:] ** 2) + (plotted_path[1][:] ** 2) + (plotted_path[2][:] ** 2)) ** 0.5) 
    velocity_map = velocity_map / max(velocity_map)

    print(velocity_map)
    
    ax2.plot3D(plotted_path[0][:final_i], plotted_path[1][:final_i], plotted_path[2][:final_i], label = "NOISY")
    

    leg = plt.legend(loc='upper left')

    ax2.set_xlabel('X')

    ax2.set_ylabel('Y')

    ax2.set_zlabel('Z')

    ax2.scatter3D(plotted_path[0][0], plotted_path[1][0], plotted_path[2][0], marker="o", alpha=0.6, color="b", label = "Starting Point")

    ax2.scatter3D(plotted_path[0][final_i], plotted_path[1][final_i], plotted_path[2][final_i], marker="X", alpha=0.6, color="r", label = "Rocket Impact")


    thrust_start_i = int(rocket.start_thrust // rocket.dt)
    thrust_end_i = int(rocket.start_thrust // rocket.dt + rocket.rough_burn_time // rocket.dt)

    ax2.scatter3D(plotted_path[0][thrust_start_i], plotted_path[1][thrust_start_i], plotted_path[2][thrust_start_i], marker="o", alpha=0.6, color="orange", label = "Thrust Start")

    ax2.scatter3D(plotted_path[0][thrust_end_i], plotted_path[1][thrust_end_i], plotted_path[2][thrust_end_i], marker="X", alpha=0.6, color="orange", label = "Thrust End")

    ax2.plot3D(plotted_path[0][:final_i], plotted_path[1][:final_i], denoised_path[:final_i], label = "DENOISED")

    #path_chopped = plotted_path[:final_i]
    #print(path_chopped)
    #path_spacing = path_chopped[:,0::100]
    #print(path_spacing)
    #ax2.scatter(path_spacing[0][:], path_spacing[1][:], path_spacing[2][:], marker="x", alpha=0.6)

    # The area that the graph will show upon start
    GraphAreaStart = 100
    plt.legend()
    ax2.set_xlim3d(-1 * GraphAreaStart, GraphAreaStart)
    ax2.set_ylim3d(-1 * GraphAreaStart, GraphAreaStart)
    ax2.set_zlim3d(-1 * GraphAreaStart, GraphAreaStart)
    plt.show()