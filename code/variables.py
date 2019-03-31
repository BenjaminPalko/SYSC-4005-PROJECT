

class SimulationVariables(object):

    def __init__(self, logger):
        self.logger = logger
        self.service_times = {
            "inspector_1_service_times": [],
            "inspector_22_service_times": [],
            "inspector_23_service_times": [],
            "workstation_1_service_times": [],
            "workstation_2_service_times": [],
            "workstation_3_service_times": [],
        }
        self.products = {
            "product_1": 0,
            "product_2": 0,
            "product_3": 0,
        }

    def get_means(self):
        means = {}
        for variable in self.service_times:
            try:
                means[variable] = sum(self.service_times[variable]) / len(self.service_times[variable])
                self.logger.debug("New mean calculated " + str(means[variable]))
            except ZeroDivisionError:
                self.logger.warning(str(variable) + " ZeroDivisionError")
                means[variable] = 0
        return means
