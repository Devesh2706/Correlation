import csv
import numpy as np

def getDataSource (data_path):
    Size_of_TV = []
    Average_time_spent_watching_TV_in_a_week = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row["Size of TV"]))
            Average_time_spent_watching_TV_in_a_week.append(float(row["	Average time spent"]))

        return {"x" : Size_of_TV,"y" : Average_time_spent_watching_TV_in_a_week}

def FindCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Size Of TV and Average time spent watching TV in a week (hours) are:- \n--->",correlation[0,1])

def setup():
    data_source = getDataSource("Size of TV,_Average time spent watching TV in a week (hours).csv")
    FindCorrelation(data_source)

setup()            
