from constants_globals import *
import csv

SALES_DATA_FILENAME = 'Sample_data/sales_data.csv'
QUIZ_SCORE_DATA_FILENAME = 'Sample_data/quiz_score_data.csv'
WEIGHT_DATA_FILENAME = 'Sample_data/weight_data.csv'

##------Reading CSV files------##
def read_csv(filename) -> list:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


#Data for line graph and bar graph
def sales_per_month_data(): #How many sales of a product per month
    data = read_csv(SALES_DATA_FILENAME)
    data = data[1:]
    labels = []
    values = []
    for item in data:
        labels.append(item[0])
        values.append(int(item[1]))
    return labels, values

#TO DO : Implement decimal values for hours
#Data for scatter graph
def quiz_data(): # Quiz score vs hours studied
    pass

#Data for whisker graph
def test_scores_data():
    pass