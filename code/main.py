import simpy
import simulation
from variables import ReplicationVariables
import logging, coloredlogs
from datetime import datetime
import performance
import numpy


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
    #   Logging Setup
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    logger = logging.getLogger()

    fileHandler = logging.FileHandler("logs/{1}.log".format("logs", datetime.now().strftime("%d-%m-%Y")))
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel("WARNING")
    logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    coloredlogs.install(level=logging.INFO)

    performance.logger = logger

    # Simulation variables
    print("Enter nothing for default simulation values (1000, 28'000)")
    REPLICATIONS = int(input("Enter Replications: ") or "1000")
    REPLICATION_DURATION = int(input("Enter time (sec): ") or "28000")
    REPLICATION_OUTPUTS = {}

    SIMULATION_VARIABLES = []

    #   Start Program
    logger.info("Creating simulation environment")

    #   Execution loop
    for iteration in range(1, REPLICATIONS+1):

        #   Environment
        logger.info('Starting iteration ' + str(iteration))
        main_env = simpy.Environment()
        REPLICATION_VARIABLES = ReplicationVariables(logger)

        # Class instantiations
        workstation_1 = simulation.Workstation1(main_env, logger, REPLICATION_VARIABLES)
        workstation_2 = simulation.Workstation2(main_env, logger, REPLICATION_VARIABLES)
        workstation_3 = simulation.Workstation3(main_env, logger, REPLICATION_VARIABLES)
        inspector_1 = simulation.Inspector1(main_env, logger, REPLICATION_VARIABLES,
                                            workstation_1, workstation_2, workstation_3, True)
        inspector_2 = simulation.Inspector2(main_env, logger, REPLICATION_VARIABLES, workstation_2, workstation_3)
        logger.debug("Simulation classes created")

        # Run simulation
        logger.debug("Running simulation...")
        main_env.run(until=REPLICATION_DURATION)  # 'until' is simulation duration

        #   Save iteration variables
        # REPLICATION_OUTPUTS[iteration] = simulation_output.get_means()
        SIMULATION_VARIABLES.append(REPLICATION_VARIABLES)
        #   Simulation End

    #   Collect outputs
    logger.info('Simulation ended, collecting output\n')
    performance.calculate_statistics(SIMULATION_VARIABLES)
    service_time_means = {
        "inspector_1": [],
        "inspector_22": [],
        "inspector_23": [],
        "workstation_1": [],
        "workstation_2": [],
        "workstation_3": [],

    }
    for x in SIMULATION_VARIABLES:
        for key, value in x.service_times.items():
            service_time_means[key].extend(value)
    for key, value in service_time_means.items():
        logger.info("Average service time for " + key + ": " + str(numpy.mean(value)))
