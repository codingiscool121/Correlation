import plotly.express as px
import csv
import numpy as np

with open('data.csv') as f:
    data=csv.DictReader(f)
    graph = px.scatter(data,x="Temperature", y="Ice-cream Sales")
    graph.show()

with open('tv.csv') as d:
    newdata= csv.DictReader(d)
    graph2 = px.scatter(newdata, x="Size of TV", y="Average time spent watching TV in a week (hours)")
    graph2.show()

