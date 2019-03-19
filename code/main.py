import simpy
from simpy.resources import container
import random
import model
from operator import attrgetter


class Inspector1(object):

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 1 starting')
        while True:
            service_time = model.inspect1_comp1()  # <--Generate duration here
            inspector_1_service_times.append(service_time)
            li = [workstation_1.component_container, workstation_2.component_container_1,
                  workstation_3.component_container_1]
            # Finds the container with the least number of type 1 components
            yield self.env.timeout(service_time)
            if workstation_1.component_container.level <= workstation_2.component_container_1.level or workstation_1.\
                    component_container.level <= workstation_3.component_container_1.level:
                yield workstation_1.component_container.put(1)
                print('Added component 1 to workstation 1')
            elif workstation_2.component_container_1.level <= workstation_3.component_container_1.level:
                yield workstation_2.component_container_1.put(1)
                print('Added component 1 to workstation 2')
            else:
                yield workstation_3.component_container_1.put(1)
                print('Added component 1 to workstation 3')


class Inspector2(object):

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 2 starting')
        while True:
            if bool(random.getrandbits(1)):  # Randomly decides which component to make
                service_time = model.inspect2_comp2()  # <--Generate duration here
                inspector_22_service_times.append(service_time)
                yield self.env.timeout(service_time)
                yield workstation_2.component_container_2.put(1)
                print('Added component 2 to workstation 2')
            else:
                service_time = model.inspect2_comp3()  # <--Generate duration here
                inspector_23_service_times.append(service_time)
                yield self.env.timeout(service_time)
                yield workstation_3.component_container_3.put(1)
                print('Added component 3 to workstation 3')


class Workstation1(object):

    def __init__(self, env):
        self.env = env
        self.component_container = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        print('Workstation 1 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container.get(1)
            service_time = model.workstation1()  # <--Generate duration here
            workstation_1_service_times.append(service_time)
            yield self.env.timeout(service_time)
            global product_1
            product_1 += 1
            print('Product 1 assembled')


class Workstation2(object):

    def __init__(self, env):
        self.env = env
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_2 = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        print('Workstation 2 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container_1.get(1) & self.component_container_2.get(1)
            service_time = model.workstation2()  # <--Generate duration here
            workstation_2_service_times.append(service_time)
            yield self.env.timeout(service_time)
            global product_2
            product_2 += 1
            print('Product 2 assembled')


class Workstation3(object):

    def __init__(self, env):
        self.env = env
        self.component_container_1 = container.Container(self.env, 2)
        self.component_container_3 = container.Container(self.env, 2)
        self.action = env.process(self.run())

    def run(self):
        print('Workstation 3 starting')
        while True:
            # Waits until there are components available to use
            yield self.component_container_1.get(1) & self.component_container_3.get(1)
            service_time = model.workstation3()  # <--Generate duration here
            workstation_3_service_times.append(service_time)
            yield self.env.timeout(service_time)
            global product_3
            product_3 += 1
            print('Product 3 assembled')


def list_avg(lst):
    try:
        return sum(lst)/len(lst)
    except ZeroDivisionError:
        return 0


#   Checks if this is the main execution script in the program
if __name__ == '__main__':
    # Simulation variables
    SIMULATION_TIME = 1200
    inspector_1_service_times = []
    inspector_22_service_times = []
    inspector_23_service_times = []
    workstation_1_service_times = []
    workstation_2_service_times = []
    workstation_3_service_times = []
    product_1 = 0
    product_2 = 0
    product_3 = 0

    print('Creating simulation environment')
    main_env = simpy.Environment()
    # Class instantiations
    inspector_1 = Inspector1(main_env)
    inspector_2 = Inspector2(main_env)
    workstation_1 = Workstation1(main_env)
    workstation_2 = Workstation2(main_env)
    workstation_3 = Workstation3(main_env)
    # Run simulation
    main_env.run(until=SIMULATION_TIME)  # 'until' is simulation duration
    print('\n====================\n' +
          ' Simulation results' +
          '\n====================\n')
    print('Execution times\n'
          'Inspector 1 {} \nInspector 22 {} \nInspector 23 {} \nWorkstation 1 {} \nWorkstation 2 {} \nWorkstation 3 {}'
          .format(inspector_1_service_times, inspector_22_service_times, inspector_23_service_times,
                  workstation_1_service_times, workstation_2_service_times, workstation_3_service_times))
    print('\nAverage service times:\n' +
          'Inspector 1 - {}, Inspector 2 - {}, \nWorkstation 1 - {}, Workstation 2 - {}, Workstation 3 - {}\n'.format(
              list_avg(inspector_1_service_times), list_avg(inspector_22_service_times),
              list_avg(inspector_23_service_times), list_avg(workstation_1_service_times),
              list_avg(workstation_2_service_times), list_avg(workstation_3_service_times)) +
          'Total execution time: {}\n'.format(SIMULATION_TIME) +
          '\nProducts produced:\n'
          '{} of product 1, {} of product 2, {} of product 3\n'.format(product_1, product_2, product_3))
