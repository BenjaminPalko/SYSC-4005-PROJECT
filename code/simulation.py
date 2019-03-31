from simpy.resources import container
import random
import model


class Inspector1(object):

    def __init__(self, env, logger, simulation_output, workstation_1, workstation_2, workstation_3, alternate_design):
        self.env = env
        self.logger = logger
        self.simulation_output = simulation_output
        self.action = env.process(self.run())
        self.workstation_1 = workstation_1
        self.workstation_2 = workstation_2
        self.workstation_3 = workstation_3
        self.alternate = alternate_design

    def run(self):
        self.logger.debug('Inspector 1 starting')
        while True:
            service_time = model.inspect1_comp1()  # <--Generate duration here
            self.simulation_output.service_times["inspector_1_service_times"].append(service_time)
            # Finds the container with the least number of type 1 components
            yield self.env.timeout(service_time)
            if not self.alternate:
                #   Normal design
                if self.workstation_1.component_container.level <= self.workstation_2.component_container_1.level or \
                        self.workstation_1.component_container.level <= self.workstation_3.component_container_1.level:
                    yield self.workstation_1.component_container.put(1)
                    self.logger.debug('Added component 1 to workstation 1')
                elif self.workstation_2.component_container_1.level <= self.workstation_3.component_container_1.level:
                    yield self.workstation_2.component_container_1.put(1)
                    self.logger.debug('Added component 1 to workstation 2')
                else:
                    yield self.workstation_3.component_container_1.put(1)
                    self.logger.debug('Added component 1 to workstation 3')
            else:
                #   Alternative design
                if self.workstation_3.component_container_1.level <= self.workstation_2.component_container_1.level or \
                        self.workstation_3.component_container_1.level <= self.workstation_1.component_container.level:
                    yield self.workstation_3.component_container_1.put(1)
                    self.logger.spam('Added component 1 to workstation 3')
                elif self.workstation_2.component_container_1.level <= self.workstation_1.component_container.level:
                    yield self.workstation_2.component_container_1.put(1)
                    self.logger.debug('Added component 1 to workstation 2')
                else:
                    yield self.workstation_1.component_container.put(1)
                    self.logger.debug('Added component 1 to workstation 1')


class Inspector2(object):

    def __init__(self, env, logger, simulation_output, workstation_2, workstation_3):
        self.env = env
        self.logger = logger
        self.simulation_output = simulation_output
        self.action = env.process(self.run())
        self.workstation_2 = workstation_2
        self.workstation_3 = workstation_3

    def run(self):
        self.logger.debug('Inspector 2 starting')
        while True:
            if bool(random.getrandbits(1)):  # Randomly decides which component to make
                service_time = model.inspect2_comp2()  # <--Generate duration here
                self.simulation_output.service_times["inspector_22_service_times"].append(service_time)
                yield self.env.timeout(service_time)
                yield self.workstation_2.component_container_2.put(1)
                self.logger.debug('Added component 2 to workstation 2')
            else:
                service_time = model.inspect2_comp3()  # <--Generate duration here
                self.simulation_output.service_times["inspector_23_service_times"].append(service_time)
                yield self.env.timeout(service_time)
                yield self.workstation_3.component_container_3.put(1)
                self.logger.debug('Added component 3 to workstation 3')


class Workstation1(object):

    def __init__(self, env, logger, simulation_output):
        self.env = env
        self.logger = logger
        self.simulation_output = simulation_output
        self.component_container = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        self.logger.debug('Workstation 1 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container.get(1)
            service_time = model.workstation1()  # <--Generate duration here
            self.simulation_output.service_times["workstation_1_service_times"].append(service_time)
            yield self.env.timeout(service_time)
            self.simulation_output.products["product_1"] += 1
            self.logger.debug('Product 1 assembled')


class Workstation2(object):

    def __init__(self, env, logger, simulation_output):
        self.env = env
        self.logger = logger
        self.simulation_output = simulation_output
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_2 = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        self.logger.debug('Workstation 2 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container_1.get(1) & self.component_container_2.get(1)
            service_time = model.workstation2()  # <--Generate duration here
            self.simulation_output.service_times["workstation_2_service_times"].append(service_time)
            yield self.env.timeout(service_time)
            self.simulation_output.products["product_2"] += 1
            self.logger.debug('Product 2 assembled')


class Workstation3(object):

    def __init__(self, env, logger, simulation_output):
        self.env = env
        self.logger = logger
        self.simulation_output = simulation_output
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_3 = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        self.logger.debug('Workstation 3 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container_1.get(1) & self.component_container_3.get(1)
            service_time = model.workstation3()  # <--Generate duration here
            self.simulation_output.service_times["workstation_3_service_times"].append(service_time)
            yield self.env.timeout(service_time)
            self.simulation_output.products["product_3"] += 1
            self.logger.debug('Product 3 assembled')
