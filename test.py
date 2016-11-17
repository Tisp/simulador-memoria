from simulator import tracefile, simulation

trace = tracefile.Tracefile('tracefile')

simulation.Simulation(trace, 1, 1, 1).run()