import simpy
from simpy.resources import container
import random
import model


class Inspector1(object):

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 1 starting')
        while True:
            service_time = model.inspect1_comp1  # <--Generate duration here
            yield self.env.process(self.component_1(service_time))

    def component_1(self, duration):
        yield self.env.timeout(duration)
        wait = True
        while wait:
            wait = False
            if workstation_1.component_container.level < 2:
                workstation_1.component_container.put()
                print('Added component 1 to workstation 1')
            elif workstation_2.component_container_1.level < 2:
                workstation_2.component_container_1.put()
                print('Added component 1 to workstation 2')
            elif workstation_3.component_container_1.level < 2:
                workstation_3.component_container_1.put()
                print('Added component 1 to workstation 3')
            else:
                wait = True


class Inspector2(object):

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 2 starting')
        while True:
            if bool(random.getrandbits(1)):  # Randomly decides which component to make
                service_time = model.inspect2_comp2()  # <--Generate duration here
                yield self.env.process(self.component_2(service_time))
            else:
                service_time = model.inspect2_comp3()  # <--Generate duration here
                yield self.env.process(self.component_3(service_time))

    def component_2(self, duration):
        yield self.env.timeout(duration)
        while workstation_2.component_container_2.level >= 2:
            pass  # Blocks inspector while container is full
        workstation_2.component_container_2.put()
        print('Added component 2 to workstation 2')

    def component_3(self, duration):
        yield self.env.timeout(duration)
        while workstation_3.component_container_3.level >= 2:
            pass  # Blocks inspector while container is full
        workstation_3.component_container_3.put()
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
            if self.component_container.level > 0:
                self.component_container.get()
                duration = model.workstation1()  # <--Generate duration here
                self.assemble_1(duration)
            else:
                pass

    def assemble_1(self, duration):
        yield self.env.timeout(duration)
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
            if self.component_container_1.level > 0 and self.component_container_2.level > 0:
                self.component_container_1.get()
                self.component_container_2.get()
                service_time = model.workstation2()  # <--Generate duration here
                self.assemble_2(service_time)
            else:
                pass

    def assemble_2(self, duration):
        yield self.env.timeout(duration)
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
            if self.component_container_1.level > 0 and self.component_container_3.level > 0:
                self.component_container_1.get()
                self.component_container_3.get()
                service_time = model.workstation3()  # <--Generate duration here
                self.assemble_3(service_time)
            else:
                pass

    def assemble_3(self, duration):
        yield self.env.timeout(duration)
        print('Product 3 assembled')


#   Checks if this is the main execution script in the program
if __name__ == '__main__':

    print('Creating simulation environment')
    main_env = simpy.Environment()
    # Class instantiations
    inspector_1 = Inspector1(main_env)
    inspector_2 = Inspector2(main_env)
    workstation_1 = Workstation1(main_env)
    workstation_2 = Workstation2(main_env)
    workstation_3 = Workstation3(main_env)
    # Run simulation
    main_env.run(until=60)  # 'until' is simulation duration


