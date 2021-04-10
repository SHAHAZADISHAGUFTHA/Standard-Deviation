import csv
import statistics as st

with open("data.csv",newline="")as f:
    reader = csv.reader(f)
    file_data = list(reader)
 
Data = [60,61,65,63,98,99,90,95,91,96]
Standard_Deviation = st.stdev(Data)
print("Standard Deviation of 60,61,65,63,98,99,90,95,91,96 \n  ",Standard_Deviation)

