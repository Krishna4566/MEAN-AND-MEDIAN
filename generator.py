import matplotlib.pyplot as plt
import cv2
import statistics as stats
import csv
import fpdf


def generate():
    """
    to be done by - Srirangan
    generates a pdf report card based on the given data, images and table.
    """
    raise NotImplementedError

   
def calculate(data):
    for i in data:
        for j in i:
            value = data[j]
            value.append(stats.mean(data[j]))
            value.append(stats.median(data[j]))
            data[j] = value
    return data

    
def plot(data):
    """
    to be done by - Krishna Shivram
    plots the data obtained from `calculate` function and plots it in a graph.
    store the graph as an image with the file name as: `{student_name}.jpeg`
    complete both plot and table with matplotlib.
    """
    # plot the mean in a graph and also generate a table that contains the marks of the student.
    # ref link for table :  https://www.scaler.com/topics/matplotlib/matplotlib-table/
    # ref link for data-plotting :  https://matplotlib.org/
    # ref link for tutorial:  https://www.w3schools.com/python/matplotlib_intro.asp
    raise NotImplementedError
def create_data(exam):
    file = open(f"{exam}.csv",'w')
    writer = csv.DictWriter(file,fieldnames=["USN","name","eng","phy","chem","cs","math"])
    # write data
    # writeheader() -> writes headers
    # writerow(dict) -> writes rows
    file.close()
    raise NotImplementedError

def read_data():
    # read data from the file.
    raise NotImplementedError

def main():
    # everything in between.
    raise NotImplementedError
    

if __name__ == "__main__":
    main()
