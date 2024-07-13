# import numpy
# town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
# town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]
# town1_mean = numpy.mean(town1_heights)
# town2_mean = numpy.mean(town2_heights)
# effectsize=town1_mean-town2_mean
# print ("Town 1 avg. height", town1_mean)
# print ("Town 2 avg. height", town2_mean)
# print ("Effect size: ", abs(effectsize))

import matplotlib.pyplot as plt
from collections import Counter
town1_heights = [5, 6, 7, 6, 7.1, 6, 4]
town2_heights = [5.5, 6.5, 7, 6, 7.1, 6]
increment = 1

width= .25
town1_bucketted = map(lambda ammt: ammt - ammt % increment, town1_heights)
town2_bucketted = map(lambda ammt: ammt - ammt % increment + width, town2_heights)
town1_hist = Counter(town1_bucketted)
town2_hist = Counter(town2_bucketted)

minamount = min(min(town1_heights), min(town2_heights))
maxamount = max(max(town1_heights), max(town2_heights))

buckets = range(int(minamount), int(maxamount)+1, increment)
fig = plt.figure()
sub = fig.add_subplot(111)
sub.bar(town1_hist.keys(), town1_hist.values(), color='b', width=width, label="town 1")
sub.bar(town2_hist.keys(), town2_hist.values(), color='r', width=width, label="town 2")
sub.legend()



fig = plt.figure()
sub = fig.add_subplot(111)
sub.boxplot([town1_heights, town2_heights], whis=1)
sub.set_xticklabels(("Town 1", "Town 2"))
sub.set_title("Town 1 vs. Town 2 Heights")
plt.show()
 
 