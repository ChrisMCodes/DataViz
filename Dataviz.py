# Trying to get a grip on different data visualization schemas
import matplotlib.pyplot as plt
import numpy as np

# Creating random data sets with approximately normal distribution
# This will be messy for a line graph
x = np.random.randn(100)
y = np.random.randn(100)
a = np.random.randn(100)
b = np.random.randn(100)

# First, line plots. Uncomment these to see them. They're messy as predicted.
# plt.plot(x, y, 'b', a, b, 'r')
# plt.title("Coordinate plane with two lines")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# Now we'll use the same data to make a histogram.
# This will make a lot, lot more sense than the madness above
# plt.hist(x, 10)
# plt.show()

# Two subplots (scatter)
plt.subplot(1, 2, 1)
plt.plot(x, y, 'go')
plt.title("First data set")

plt.subplot(1, 2, 2)
plt.plot(x ** 2, b, 'r^')
plt.title("Second data set")

plt.suptitle("First and second data sets")
plt.show()




