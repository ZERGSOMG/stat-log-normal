import numpy
import sys
import math
import matplotlib.pyplot as plot

def getNormalValue():
    x = numpy.random.normal(3,1)
    y = math.exp(x)
    return y

def getLognormalSample():
    sample = []
    for x in range(3):
        sample.append(get_normal_value())
    return sample

numberOfTimes = int(input())

finalDest = []
sampDist = []
normalList = []

for x in range(numberOfTimes):
    sampDist.append(get_lognormal_sample())

for sample in sampDist:
    finalDest.append(numpy.mean(sample, axis=0, dtype=numpy.float64))

sampleMean = numpy.mean(finalDest, dtype=numpy.float64)
sampleStd = numpy.std(finalDest)

for normal in range(numberOfTimes):
    normalList.append(numpy.random.normal(sampleMean,sampleStd))
    
normalPercentile = numpy.percentile(normalList, 90)
print(normalPercentile)
plot.hist(finalDest, bins=5000)
plot.title("Sample Distribution of Log-normal")
plot.suptitle("90th Percentile is " + str(numpy.percentile(finalDest, 90)))
plot.show()