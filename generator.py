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
    pdf = 

   
def calculate(data):
    for i in data:
        value = data[i]
        value.append(stats.mean(data[i]))
        value.append(stats.median(data[i]))
        data[i] = value
    return data

    
def plot(data):
    """
    to be done by - Krishna Shivram
    plots the data obtained from `calculate` function and plots it in a graph.
    store the graph as an image with the file name as: `{student_name}.jpeg`
    complete both plot and table with matplotlib.
    """
    ...
    
def create_data(exam):
    file = open(f"{exam}.csv",'w')
    writer = csv.DictWriter(file,fieldnames=["USN","name","eng","phy","chem","cs","math"])
    # write data
    # writeheader() -> writes headers
    # writerow(dict) -> writes rows
    file.close()

def read_data():
    ...

def main():
    # everything in between.
    

if __name__ == "__main__":
    main()
