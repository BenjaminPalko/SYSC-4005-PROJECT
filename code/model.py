import numpy


def inspect1_comp1():
    datalist = open('servinsp1.dat').read().splitlines()
    return calc_rand_list(datalist)


def inspect2_comp2():
    datalist = open('servinsp22.dat').read().splitlines()
    return calc_rand_list(datalist)


def inspect2_comp3():
    datalist = open('servinsp23.dat').read().splitlines()
    return calc_rand_list(datalist)


def workstation1():
    datalist = open('ws1.dat').read().splitlines()
    return calc_rand_list(datalist)


def workstation2():
    datalist = open('ws2.dat').read().splitlines()
    return calc_rand_list(datalist)


def workstation3():
    datalist = open('ws3.dat').read().splitlines()
    return calc_rand_list(datalist)


def get_ordinary_mean(field):
    if field is "inspector_1_service_times":
        datalist = open('servinsp1.dat').read().splitlines()
    elif field is "inspector_22_service_times":
        datalist = open('servinsp22.dat').read().splitlines()
    elif field is "inspector_23_service_times":
        datalist = open('servinsp23.dat').read().splitlines()
    elif field is "workstation_1_service_times":
        datalist = open('ws1.dat').read().splitlines()
    elif field is "workstation_2_service_times":
        datalist = open('ws2.dat').read().splitlines()
    elif field is "workstation_3_service_times":
        datalist = open('ws3.dat').read().splitlines()
    else:
        datalist = []
    for n in range(len(datalist)):
        datalist[n] = float(datalist[n])
    return numpy.mean(datalist)


def calc_rand_list(datalist):
    datatotal = 0
    for x in range(0, 300):
        datatotal += float(datalist[x])
    mean = datatotal / 300
    return numpy.random.exponential(mean, 1)[0]



