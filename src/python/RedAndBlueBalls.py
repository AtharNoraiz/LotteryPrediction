import pandas
import time
import matplotlib.pyplot as plt
import random

#See http://www.red-dove.com/python_logging.html
import logging
logging.basicConfig()
log = logging.getLogger(None)
log.setLevel(logging.DEBUG) #set verbosity to show all messages of severity >= DEBUG
log.info("Starting PandasCSV!")
class UTCFormatter(logging.Formatter):
    converter = time.gmtime # not documented, had to read the module's source code ;-)
#read CSV
#balls = pd.read_csv('../../lottery-data/red_bule_balls_2003.csv')
balls = pandas.read_csv('../../lottery-data/red_bule_balls_2003.csv',sep=';',header=None)
print(balls)
#Dot plot,a very simple way to gain an initial sense of the data set is to create a dot plot.
##Dot plot display
###Blue balls statistics
blue_balls = balls['X7']
print("blue_balls.describe:")
print(blue_balls.describe())
series_blue_balls = pandas.Series(blue_balls)
print("series_blue_balls.value_counts():")
series_blue_balls_value_counts = series_blue_balls.value_counts()
##sort_index
series_blue_balls_value_counts = series_blue_balls_value_counts.sort_index(ascending=True)
print(series_blue_balls_value_counts)
##Dot plot display
dfs_blue_balls_count_values = series_blue_balls_value_counts.values
print("Dot,dfs_blue_balls_count_values:")
print(dfs_blue_balls_count_values)
plt.plot(dfs_blue_balls_count_values,'x',label='Dot plot')
plt.legend()
plt.ylabel('Dot,number of blue balls')
plt.xlabel('Dot,number of duplication')
plt.show()
#Jitter plot
idx_min = min(dfs_blue_balls_count_values)
idx_max = max(dfs_blue_balls_count_values)
idx_len = idx_max-idx_min
print("min:",idx_min,"max:",idx_max)
num_jitter = 0
samplers = random.sample(range(idx_min,idx_max),idx_len)
while num_jitter < 5:
    samplers += random.sample(range(idx_min,idx_max),idx_len)
    num_jitter += 1
##lots of jitter effect
print("samplers:",samplers)
plt.plot(samplers,'ro',label='Jitter plot')
plt.ylabel('Jitter,number of blue balls')
plt.xlabel('Jitter,number of duplication')
plt.legend()
plt.show()
#Histograms and Kernel Density Estimates:
#Scott rule,
#This rule assumes that the data follows a Gaussian distribution;

#Plotting the VIP appear frequency histograms(x-axis:frequency,y-axis:VIPs)
##@see http://pandas.pydata.org/pandas-docs/dev/basics.html#value-counts-histogramming