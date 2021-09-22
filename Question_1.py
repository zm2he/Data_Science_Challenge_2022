# I named the data csv challenge_data.csv for simplicity

# a) We get such a high AOV because there are outlier transactions with unusually high values
# which will push the AOV to be higher than the values of most transactions. For instance, 
# shop 42 having a transaction woth 704000 on 2017-03-07 4:00:00. This makes the AOV unrepresentative
# of the value of the majority of transactions. To counteract this, we can calculate a trimmed
# mean where we reject all values 1 standard deviation away from the mean.

# b) I would calculate a trimmed mean by taking the original AOV and rejecting all values more than +/- one
# standard deviation around it. Because the outliers are so far removed from the values of the majority
# of transactions, they necessarily will be removed, since they must be beyond the standard deviation. We still
# have a representative result, since only 44 data points were removed.

# c) The value I calculated was 400.04. This is much more representative of what a normal transaction looks like.

import csv
from math import sqrt

sum_val = 0
count = 0
with open('challenge_data.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    sum_val += int(row['order_amount'])
    count += 1

mean = sum_val/count
print("AOV: %.2f" % mean)

stdev_sum = 0
with open('challenge_data.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    stdev_sum += (int(row['order_amount']) - mean)**2/count

std_dev = sqrt(stdev_sum)

trimmed_sum = 0
trimmed_count = 0
with open('challenge_data.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    val = int(row['order_amount'])
    if val <= mean + std_dev and val >= mean - std_dev:
      trimmed_count += 1
      trimmed_sum += val

trimmed_mean = trimmed_sum/trimmed_count
print("Trimmed Mean: %.2f" % trimmed_mean)
