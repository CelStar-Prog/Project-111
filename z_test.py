import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
fig.show()
print(statistics.mean(data))
def randomSetOfMean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def showFigure(mean_list):
    df = mean_list
    fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = randomSetOfMean(10)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    showFigure(mean_list)
    print(statistics.mean(mean_list))

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
setup()