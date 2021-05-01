import csv
import math
import pandas as pd
import plotly_express as px
import numpy as np

File_Object = open(
    'Co-relation\Correlation-data-files-main\Student Marks vs Days Present.csv', newline='')
reader = csv.reader(File_Object)

List_1 = list(reader)
List_1.pop(0)

Height_List = []

for i in range(len(List_1)):
    Numbers = List_1[i][1]
    Height_List.append(float(Numbers))


l = len(Height_List)
Total = 0

for x in Height_List:
    Total = Total + float(x)

mean = Total/l


path = "Co-relation\Correlation-data-files-main\Student Marks vs Days Present.csv"
CSV_File_Object = open(path)

Csv_File = csv.reader(CSV_File_Object)
All_Data = list(Csv_File)
All_Data.pop(0)

AverageTvSize = []
AverageTimeSpent = []

for i in All_Data:
    AverageTvSize.append(float(i[2]))
    AverageTimeSpent.append(float(i[1]))

DataSource = {'x': AverageTvSize, 'y': AverageTimeSpent}

Corelation = np.corrcoef(
    DataSource['x'], DataSource['y']
)

print(Corelation[0, 1])

Csv_File_Path = 'Co-relation\Correlation-data-files-main\Student Marks vs Days Present.csv'
Graph_Csv_File = pd.read_csv(Csv_File_Path)

Graph = px.scatter(Graph_Csv_File, x='Days Present',
                   y='Marks In Percentage')

Graph.update_layout(shapes=[

    dict(

        type='line',
        x0=0,
        x1=l,
        y1=mean,
        y0=mean

    )
])

Graph.show()
