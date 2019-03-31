import simpy
import simulation
from variables import SimulationVariables
import logging, coloredlogs
from datetime import datetime
import performance


def convert_data_to_lists(data):
    new_dict = {}
    for x in data:
        try:
            for y in data[x]:
                if y not in new_dict:
                    new_dict[y] = []
                new_dict[y].append(data[x][y])
        except TypeError:
            pass
    return new_dict


#   Checks if this is the main execution script in the program
if __name__ == '__main__':
    # Simulation variables
    REPLICATIONS = int(input("Enter Replications: "))
    REPLICATION_DURATION = int(input("Enter time (sec): "))
    REPLICATION_OUTPUTS = {}

    #   Logging Setup
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    logger = logging.getLogger()

    fileHandler = logging.FileHandler("logs/{1}.log".format("logs", datetime.now().strftime("%d-%m-%Y")))
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel("WARNING")
    logger.addHandler(fileHandler)
0
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    coloredlogs.install(level=logging.INFO)

    performance.logger = logger

    #   Start Program
    logger.info("Creating simulation environment")

    #   Execution loop
    for iteration in range(1, REPLICATIONS+1):

        #   Environment
        logger.info('Starting iteration ' + str(iteration))
        main_env = simpy.Environment()
        simulation_output = SimulationVariables(logger)

        # Class instantiations
        workstation_1 = simulation.Workstation1(main_env, logger, simulation_output)
        workstation_2 = simulation.Workstation2(main_env, logger, simulation_output)
        workstation_3 = simulation.Workstation3(main_env, logger, simulation_output)
        inspector_1 = simulation.Inspector1(main_env, logger, simulation_output,
                                            workstation_1, workstation_2, workstation_3, False)
        inspector_2 = simulation.Inspector2(main_env, logger, simulation_output, workstation_2, workstation_3)
        logger.debug("Simulation classes created")

        # Run simulation
        logger.debug("Running simulation...")
        main_env.run(until=REPLICATION_DURATION)  # 'until' is simulation duration

        #   Save iteration variables
        REPLICATION_OUTPUTS[iteration] = simulation_output.get_means()
        #   Simulation End

    #   Collect outputs
    logger.info('Simulation ended, collecting output')
    simulation_output_dict = convert_data_to_lists(REPLICATION_OUTPUTS)
    performance.calculate_statistics(simulation_output_dict)

    input("Press the Enter key to exit...")
