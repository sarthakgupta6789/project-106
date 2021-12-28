import plotly.express as px
import csv
import numpy as np
def PlotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Coffee in ml", y = "sleep in hours")
        fig.show()
def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x":  Coffee_in_ml,"y": sleep_in_hours}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Coffee in ml and sleep in hours",correlation[0,1])
def setUp():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    PlotFigure(data_path)
setUp()
    
