import simpy
import random


class Inspector1(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 2 starting')
        while True:
            service_time = 5  # Generate random value here
            yield self.env.process(self.component_1(service_time))

    def component_1(self, duration):
        yield self.env.timeout(duration)


class Inspector2(object):
    def __init__(self, env):
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Inspector 2 starting')
        while True:
            if bool(random.getrandbits(1)):
                service_time = 5  # Generate random value here
                yield self.env.process(self.component_2(service_time))
            else:
                service_time = 5  # Generate random value here
                yield self.env.process(self.component_3(service_time))

    def component_2(self, duration):
        yield self.env.timeout(duration)

    def component_3(self, duration):
        yield self.env.timeout(duration)


class Workstation1(object):

    def __init__(self, env):
        self.buffer_1 = False
        self.buffer_2 = False
        self.env = env
        self.action = env.process(self.run())

    def run(self):
        print('Workstation 1 starting')
        while True:
            # Handles starting when there are buffered components
            if self.buffer_1:
                if self.buffer_2:  # If there is a second component buffered, clear it
                    self.buffer_2 = False
                else:  # If only 1 component buffered, clear it
                    self.buffer_1 = False
            else:
                pass


class Workstation2(object):
    buffer_1 = None
    buffer_2 = None


class Workstation3(object):
    buffer_1 = None
    buffer_2 = None


def main():
    pass


#   Checks if this is the main execution script in the program
if __name__ == "__main__":
    main_env = simpy.Environment()
    main()
