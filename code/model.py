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


def calc_rand_list(datalist):
    datatotal = 0
    for x in range(0, 300):
        datatotal += float(datalist[x])
    mean = datatotal / 300
    return numpy.random.exponential(mean)


