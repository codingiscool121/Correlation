import plotly.express as px
import csv
import numpy as np


def getData(path, column1, column2):
    col1=[]
    col2=[]
    with open(path) as f:
      data=csv.DictReader(f)
      for row in data:
          col1.append(float(row[column1]))
          col2.append(float(row[column2]))
    return{"x": col1, "y": col2}


def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print(correlation[0,1])

def main():
    path = input("Hey! Enter the path of the file.")
    column1 = input("Enter the column name for x.")
    column2 = input("Enter the column name for y.")
    data= getData(path, column1, column2)
    findCorrelation(data)

main()
 