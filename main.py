import json
import matplotlib.pyplot as plt
import data_request as pull
import plotter

def main():
   data = pull.populate()
   print(len(data))
   plotter.plot(data,"States/Territories", "Positive Cases")

main()