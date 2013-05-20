from csv_helper import *
import matplotlib.pyplot as plt
import numpy as np


ICECREAM_CSV_DIR = "../../icecream_csv/csv/"


# dtest
fig1 = plt.figure()
ax1 = fig1.add_subplot(2,2,1)
ax1.set_title("N = 100")
ax2 = fig1.add_subplot(2,2,2)
ax2.set_title("N = 1000")
ax3 = fig1.add_subplot(2,2,3)
ax3.set_title("N = 10000")
ax4 = fig1.add_subplot(2,2,4)
ax4.set_title("N = 100000")

N100_file = "dtest_N100d20interval2.csv"
N1000_file = "dtest_N1000d40interval4.csv"
N10000_file = "dtest_N10000d44interval4.csv"
N50000_file = "dtest_N50000d19interval2.csv"

x,y = avg_plot_data(ICECREAM_CSV_DIR + N100_file, 1, 0)
ax1.plot(x,y,label="Average")
ax1.legend()

x,y = avg_plot_data(ICECREAM_CSV_DIR + N1000_file, 1, 0)
ax2.plot(x,y,label="Average")
ax2.legend()

x,y = avg_plot_data(ICECREAM_CSV_DIR + N10000_file, 1, 0)
ax3.plot(x,y,label="Average")
ax3.legend()

x,y = avg_plot_data(ICECREAM_CSV_DIR + N50000_file, 1, 0)
ax4.plot(x,y,label="Average")
ax4.legend()




fig1 = plt.figure()
ax1 = fig1.add_subplot(2,2,1)
ax1.set_title("N = 100")
ax2 = fig1.add_subplot(2,2,2)
ax2.set_title("N = 1000")
ax3 = fig1.add_subplot(2,2,3)
ax3.set_title("N = 10000")
ax4 = fig1.add_subplot(2,2,4)
ax4.set_title("N = 100000")

N100_file = "dtest_N100d20interval2.csv"
N1000_file = "dtest_N1000d40interval4.csv"
N10000_file = "dtest_N10000d44interval4.csv"
N50000_file = "dtest_N50000d19interval2.csv"

x,y = max_plot_data(ICECREAM_CSV_DIR + N100_file, 1, 0)
ax1.plot(x,y,label="Maximum")
ax1.legend()

x,y = max_plot_data(ICECREAM_CSV_DIR + N1000_file, 1, 0)
ax2.plot(x,y,label="Maximum")
ax2.legend()

x,y = max_plot_data(ICECREAM_CSV_DIR + N10000_file, 1, 0)
ax3.plot(x,y,label="Maximum")
ax3.legend()

x,y = max_plot_data(ICECREAM_CSV_DIR + N50000_file, 1, 0)
ax4.plot(x,y,label="Maximum")
ax4.legend()



# ntest
d3_file = "ntest_d3N25to51200interval2.csv"

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title("d = 3")

x,y = avg_plot_data(ICECREAM_CSV_DIR + d3_file, 2, 0)
ax1.plot(x,y,label="Average")
ax1.legend()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title("d = 3")

x,y = max_plot_data(ICECREAM_CSV_DIR + d3_file, 2, 0)
ax1.plot(x,y,label="Maximum")
ax1.legend()



#alttest
fig = plt.figure()



plt.show()


