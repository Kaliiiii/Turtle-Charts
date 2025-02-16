from constants_globals import *
import random

#Data for line graph and bar graph
def sales_per_month_data(): #How many sales of a product per month
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    data = []
    max_value = 0
    for i in range(X_LEN):
        value = random.randint(0, Y_MAX)
        data.append(value)
        if value > max_value:
            max_value = value
    return data, labels

#TO DO : Implement decimal values for hours
#Data for scatter graph
def quiz_data(): # Quiz score vs hours studied
    data = []
    score_max = 100
    score_min = 15 #Showed up to quiz and turned it in
    hours_max = 10
    for i in range(DATA_POINTS):
        hours = random.randint(0, hours_max)
        if i % 3 == 0: # 1/3 of the data is skewed
            if hours <= (hours_max/5): # If studied 0 hours likely lower score
                score = random.randint(score_min, int(score_max/2))
            elif hours >= hours_max - (hours_max/5): # If studied 8 hours likely higher score
                score = random.randint(int(score_max/2), score_max)
            else:
                score = random.randint(int(score_max/4), score_max - int(score_max/4))
        else:
            score = random.randint(score_min, score_max)
        data.append((hours, score))
    return data

#Data for whisker graph
def test_scores_data():
    pass