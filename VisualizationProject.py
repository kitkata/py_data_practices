from csv import reader
import os
#import plotly
#import plotly.graph_objs as go

#import pandas as pd

opened_file = open(os.path.realpath("Files\AB_Listings.csv"), encoding="utf8")
read_file = reader(opened_file)
listings_data = list(read_file)

print(listings_data[:5])