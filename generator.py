import matplotlib.pyplot as plt
import cv2
import statistics as stats
import csv


def generate():
    """
    to be done by - Srirangan
    generates a pdf report card based on the given data, images and table.
    """
    
def calculate(data,name):
    """
    to be done by - Krishna Shivram
    calculates statistics based on the given data.
    statistics - mea and median.
    assume that `data` includes all details regarding student in the format:
    {exam_name(str):[eng,phy,chem,cs,math],exam_name_2:[eng,phy,chem,cs,math]}
    name will be the name of the student .
    append mean,median to the data and return the data
    """
    "D=given dictionary"
    
    for i in data:
        if i==name:
         su=0
         for j in d[i]:
             su+=j
           


         mean=su/5
         median=(len(j)+1)/2
         data[i].append(mean)
         data[i].append(median)
         return(data)
         print("the mean mark of ",i,"is ",mean)
         print("the median of the marks is",median)

def table(data,rows,columns):
    """
    to be done by - Srirangan
    creates a table that plots the data against the given rows and columns
    """
    
def plot(data):
    """
    to be done by - Krishna Shivram
    plots the data obtained from `calculate` function and plots it in a graph.
    store the graph as an image with the file name as: `{student_name}.jpeg`
    """
    

def main():
    

if __name__ == "__main__":
    main()
