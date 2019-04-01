from scipy import stats
import numpy

logger = None


def calc_ci(data, confidence=0.95):
    if not isinstance(data, list):
        return data, 0
    n = len(data)
    if n is 0:
        return 0, 0
    mean, std_dev = numpy.mean(data), stats.sem(data)

    logger.debug("Numpy mean " + str(mean))
    logger.debug("Scipy standard deviation " + str(std_dev))

    h = std_dev * stats.t.ppf((1 + confidence) / 2., n - 1)
    return mean, h


def calculate_statistics(data):
    block_times_1 = []
    block_times_2 = []
    block_times_3 = []
    idle_times_1 = []
    idle_times_2 = []
    idle_times_3 = []
    products_produced_1 = []
    products_produced_2 = []
    products_produced_3 = []

    for variable in data:
        block_times_1.extend(variable.block_times[1])
        block_times_2.extend(variable.block_times[2])
        block_times_3.extend(variable.block_times[3])
        idle_times_1.extend(variable.idle_times[1])
        idle_times_2.extend(variable.idle_times[2])
        idle_times_3.extend(variable.idle_times[3])
        products_produced_1.append(variable.products[1])
        products_produced_2.append(variable.products[2])
        products_produced_3.append(variable.products[3])

    m, h = calc_ci(block_times_1)
    logger.info("Confidence interval for inspector 1 block times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(block_times_2)
    logger.info("Confidence interval for inspector 2 block times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(block_times_3)
    logger.info("Confidence interval for inspector 3 block times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(idle_times_1)
    logger.info("Confidence interval for workstation 1 idle times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(idle_times_2)
    logger.info("Confidence interval for workstation 2 idle times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(idle_times_3)
    logger.info("Confidence interval for workstation 3 idle times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(products_produced_1)
    logger.info("Confidence interval for product 1 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(products_produced_2)
    logger.info("Confidence interval for product 2 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")
    m, h = calc_ci(products_produced_3)
    logger.info("Confidence interval for product 3 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")
