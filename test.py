import plotly.express as px
import csv
import numpy as np

def getData(path):
    col1=[]
    col2=[]
    with open(path) as f:
        data = csv.reader(f)
        for row in data:
            column1 = row[0]
            column2 = row[1]
            print(column2)
            break
        data2=  csv.DictReader(f)
        for row in data2:
          print(row)
          col1.append(float(row[column1]))
          col2.append(float(row[column2]))
    return{"x": col1, "y": col2}


def findCorrelation(data):
    correlation = np.corrcoef(data["x"], data["y"])
    print(correlation[0,1])

def main():
    path = input("Hey! Enter the path of the file.")
    data= getData(path)
    findCorrelation(data)

main()
getData()