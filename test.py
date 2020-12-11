from source import num_vehicletrip_office_build
import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt
import statistics
import scipy.stats
from statistics import mean

csvname = input("Enter the name of the csv file, Example: filename.csv:")
build_space_est = input("Enter the building space in (sq. ft.) to estimate vehicle-trips for that office building (DON'T ADD COMMAS):")
build_space_est = float(build_space_est)
df = pd.read_csv(csvname)
print(df)


a=num_vehicletrip_office_build()
print("The Number of vehicle-trips for a planned office building of " + str(build_space_est) + " square feet is " + str(a) )

