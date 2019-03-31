import model
from math import sqrt, fsum, fabs
from scipy import stats
import numpy

logger = None


def check_bias(variable, data):

    logger.info("Calculating bias for data")

    #   Round to 3 decimal places or else PE will never be unbiased
    point_estimator = round(fsum(data) / len(data), 3)
    logger.debug("Point estimator " + str(point_estimator))

    ordinary_mean = round(model.get_ordinary_mean(variable), 3)
    logger.debug("Ordinary mean " + str(ordinary_mean))

    return point_estimator, ordinary_mean


def calculate_confidence_interval(variable, replications, data):

    logger.debug("Calculating CI for data")

    def function(x):
        average = sum(x) / len(x)
        logger.debug("Average for " + variable + " is " + str(average))
        running_sum = 0
        for i in range(len(x)):
            running_sum += pow((x[i] - average), 2)
        logger.debug("Internal confidence interval function returning sum " + str(running_sum))
        return running_sum

    logger.debug("Calculation confidence interval for " + variable)

    sample_variance = sqrt((1/(replications-1)) * function(data))

    return sample_variance


def calculate_confidence_interval_half_width(variable, data, replications, confidence=0.95):

    variance = calculate_confidence_interval(variable, replications, data)
    logger.debug("Sample variance for " + variable + " is " + str(variance))

    n = len(data)
    mean, std_deviation = numpy.mean(data), stats.sem(data)
    logger.debug("Numpy mean " + str(mean))
    logger.debug("Scipy standard deviation " + str(std_deviation))

    h = std_deviation * stats.t.ppf((1+confidence)/2., n-1)

    return mean, h


def calculate_statistics(data):
    for variable in data:
        pe, ordinary = check_bias(variable, data[variable])

        if pe == ordinary:
            logger.info("PE is unbiased for " + variable)

        else:
            logger.info("PE is biased for " + variable +
                        " with a difference of  " +
                        str(fabs(pe - ordinary)))
        m, h = calculate_confidence_interval_half_width(variable, data[variable], len(data))
        logger.info("Confidence interval for " + variable + " is " + str(m) + " ±" + str(h))
