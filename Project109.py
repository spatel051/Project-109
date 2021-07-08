import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_deviation = statistics.stdev(data)

first_std_deviation_start, first_std_deviation_end = mean - standard_deviation, mean + standard_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * standard_deviation), mean + (2 * standard_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * standard_deviation), mean + (3 * standard_deviation)

thin_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("Mean of this data is " + str(mean))
print("Median of this data is " + str(median))
print("Mode of this data is " + str(mode))
print("Standard deviation of this data is " + str(standard_deviation))
print("{}% of data lies between 1 standard deviation".format(len(thin_1_std_deviation) * 100.0 / len(data)))
print("{}% of data lies between 2 standard deviation".format(len(thin_2_std_deviation) * 100.0 / len(data)))
print("{}% of data lies between 3 standard deviation".format(len(thin_3_std_deviation) * 100.0 / len(data)))

fig = ff.create_distplot([data], ["Reading Scores"], show_hist = False)
fig.add_trace(go.Scatter(
    x = [mean, mean],
    y = [0, 0.17],
    mode = "lines",
    name = "MEAN"
))
fig.add_trace(go.Scatter(
    x = [first_std_deviation_start, first_std_deviation_start],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 1"
))
fig.add_trace(go.Scatter(
    x = [first_std_deviation_end, first_std_deviation_end],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 1"
))
fig.add_trace(go.Scatter(
    x = [second_std_deviation_start, second_std_deviation_start],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 2"
))
fig.add_trace(go.Scatter(
    x = [second_std_deviation_end, second_std_deviation_end],
    y = [0, 0.17],
    mode = "lines",
    name = "STANDARD DEVIATION 2"
))
fig.show()