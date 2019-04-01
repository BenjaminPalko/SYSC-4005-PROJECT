import model


def validate_inspect1_comp1():
    datalist = open('servinsp1.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0,300):
        random_mean += model.inspect1_comp1()
    random_mean = random_mean / 300

    print('Inspector 1 Component 1')
    print_mean(actual_mean, random_mean)


def validate_inspect2_comp2():
    datalist = open('servinsp22.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, 300):
        random_mean += model.inspect2_comp2()
    random_mean = random_mean / 300

    print('Inspector 2 Component 2')
    print_mean(actual_mean, random_mean)


def validate_inspect2_comp3():
    datalist = open('servinsp23.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, 300):
        random_mean += model.inspect2_comp3()
    random_mean = random_mean / 300

    print('Inspector 2 Component 3')
    print_mean(actual_mean, random_mean)


def validate_workstation1():
    datalist = open('ws1.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, 300):
        random_mean += model.workstation1()
    random_mean = random_mean / 300

    print('Workstation 1')
    print_mean(actual_mean, random_mean)


def validate_workstation2():
    datalist = open('ws2.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, 300):
        random_mean += model.workstation2()
    random_mean = random_mean / 300

    print('Workstation 2')
    print_mean(actual_mean, random_mean)


def validate_workstation3():
    datalist = open('ws3.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, 300):
        random_mean += model.workstation3()
    random_mean = random_mean / 300

    print('Workstation 3')
    print_mean(actual_mean, random_mean)


def print_mean(actual_mean, random_mean):
    print('Actual Mean: ', actual_mean)
    print('Random Mean:', random_mean)
    print('Difference(%): ', (abs(actual_mean-random_mean)/actual_mean) * 100, '\n')


if __name__ == '__main__':
    validate_inspect1_comp1()
    validate_inspect2_comp2()
    validate_inspect2_comp3()
    validate_workstation1()
    validate_workstation2()
    validate_workstation3()
