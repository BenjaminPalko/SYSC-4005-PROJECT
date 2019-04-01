import model


def validate_inspect1_comp1(n):
    datalist = open('servinsp1.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.inspect1_comp1()
    random_mean = random_mean / n

    print('Inspector 1 Component 1')
    print_mean(actual_mean, random_mean)


def validate_inspect2_comp2(n):
    datalist = open('servinsp22.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.inspect2_comp2()
    random_mean = random_mean / n

    print('Inspector 2 Component 2')
    print_mean(actual_mean, random_mean)


def validate_inspect2_comp3(n):
    datalist = open('servinsp23.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.inspect2_comp3()
    random_mean = random_mean / n

    print('Inspector 2 Component 3')
    print_mean(actual_mean, random_mean)


def validate_workstation1(n):
    datalist = open('ws1.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.workstation1()
    random_mean = random_mean / n

    print('Workstation 1')
    print_mean(actual_mean, random_mean)


def validate_workstation2(n):
    datalist = open('ws2.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.workstation2()
    random_mean = random_mean / n

    print('Workstation 2')
    print_mean(actual_mean, random_mean)


def validate_workstation3(n):
    datalist = open('ws3.dat').read().splitlines()
    actual_mean = 0
    for x in range(0, 300):
        actual_mean += float(datalist[x])
    actual_mean = actual_mean / 300

    random_mean = 0
    for x in range(0, n):
        random_mean += model.workstation3()
    random_mean = random_mean / n

    print('Workstation 3')
    print_mean(actual_mean, random_mean)


def print_mean(actual_mean, random_mean):
    print('Actual Mean: ', actual_mean)
    print('Random Mean:', random_mean)
    print('Difference(%): ', (abs(actual_mean-random_mean)/actual_mean) * 100, '\n')


if __name__ == '__main__':
    validate_inspect1_comp1(30000)
    validate_inspect2_comp2(30000)
    validate_inspect2_comp3(30000)
    validate_workstation1(30000)
    validate_workstation2(30000)
    validate_workstation3(30000)
