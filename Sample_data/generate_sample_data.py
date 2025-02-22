import random
import csv


X_LEN = 6
Y_MAX = 300

SCORE_DATA_POINTS = 25
WEIGHT_DATA_POINTS = 100

MAX_WEIGHT = 400
MIN_WEIGHT = 90

SALES_DATA_FILENAME = 'sales_data.csv'
QUIZ_SCORE_DATA_FILENAME = 'quiz_score_data.csv'
WEIGHT_DATA_FILENAME = 'weight_data.csv'

def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        file.truncate(0)
        writer = csv.writer(file)
        writer.writerow(data[0])
        writer.writerows(data[1:])

##------Generating Sales Data------##
def sales_per_month_data(): #How many sales of a product per month
    data = [["Month", "Sales"]]
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for i in range(X_LEN):
        value = random.randint(1, Y_MAX)
        data.append([labels[i], value])

    write_to_csv(data, SALES_DATA_FILENAME) 

##------Generating Quiz Score Data------##
def quiz_data(): # Quiz score vs hours studied
    data = [['Hours', 'Score']]
    score_max = 100
    score_min = 15 #Showed up to quiz and turned it in
    hours_max = 10
    for i in range(SCORE_DATA_POINTS):
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
        data.append([hours, score])
    write_to_csv(data, QUIZ_SCORE_DATA_FILENAME) 

##------Generating Weight Data------##
def weight_data():
    data = [['weight']]
    for i in range(WEIGHT_DATA_POINTS):
        weight = random.randint(MIN_WEIGHT, MAX_WEIGHT)
        data.append([weight])
    # Open the CSV file in write mode ('w')
    write_to_csv(data, WEIGHT_DATA_FILENAME)

def main():
    sales_per_month_data()
    quiz_data()
    weight_data()

if __name__ == "__main__":
    main()
