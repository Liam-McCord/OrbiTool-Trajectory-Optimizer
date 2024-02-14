





thrust_graph = plt.axes()
thrust_graph.plot(np.arange(0,len(plotted_path[5]),1), plotted_path[5])
thrust_graph.set_box_aspect(1)

thrust_graph.plot(np.arange(0,len(test_rocket.step_thrust_distribution),1), test_rocket.step_thrust_distribution)
thrust_graph.set_box_aspect(1)
plt.show()