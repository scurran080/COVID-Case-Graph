import json
import matplotlib.pyplot as plt
import data_request as pull
import plotter
import json
import data_management

def main():
   data = pull.request_data(pull.STATES_DATA)
  # data = pull.request_data(pull.DAILY_DATA)
   positives = data_management.get_values(data,"state","positive")
   #icu = data_management.get_values(data, "date", "inIcuCurrently")
   #trimmed = data_management.date_range(icu, 20201118, 20210119)
   plotter.bar_graph(positives,"States", "Positives (million)","Total Positives Per State")
   #plotter.line_graph(trimmed, "Date", "# in ICU","Number of Patients In the ICU")



main()