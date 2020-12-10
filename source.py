import pandas as pd 
import numpy as np
import math
import matplotlib.pyplot as plt
import statistics
import scipy.stats
from statistics import mean
csvname=input("Enter the name of the csv file, Example: filename.csv:")
build_space_est=input("Enter the building space in (sq. ft.) to estimate vehicle-trips for that office building (DON'T ADD COMMAS):")
build_space_est=float(build_space_est)
df=pd.read_csv(csvname)
print(df)


def num_vehicletrip_office_build(df, build_space_est):
    
    """ Returns the average of office the office building space:
    """
    avg_office_building_space = df['Building Number'].mean()

    """ Returns number of employees per building:  
    """
    num_employees_per_building = df['Office Space (Sq.Ft.)']*df['Number of Employees per 1,000 Sq.Ft.']/1000
    

    """ Returns the Average number of employees per building:
    """
    a = num_employees_per_building.mean()
    avg_num_employees_per_building = math.ceil(a)
    
    """ Returns the Number of person-trips which use auto mode: 
    """
    b = num_employees_per_building*0.2
    num_persontrip_automode = round(b)


    """ Returns the Total number of person-trips that use auto mode: 
    """
    tot_num_persontrip_automode = num_persontrip_automode.sum()
    
    """ Returns the Number of person-trips bus mode: 
    """
    c = num_employees_per_building*0.3
    num_persontrip_busmode = round(c)

    """ Returns the Total number of person-trips bus mode:   
    """
    tot_num_persontrip_busmode = num_persontrip_busmode.sum()
    
    """ Returns the Number of person-trips subway mode: 
    """
    d = num_employees_per_building*1.3
    num_persontrip_subwaymode = round(d)
    
    """ Returns the Total number of person-trips subway mode:   
    """
    tot_num_persontrip_subwaymode = num_persontrip_subwaymode.sum()
    
    """ Returns the Number of person-trips railmode: 
    """
    e = num_employees_per_building*0.2
    num_persontrip_railmode = round(e)
    
    """ Returns the Total number of person-trips rail mode:  
    """
    tot_num_persontrip_railmode = num_persontrip_railmode.sum()
    
    """ Returns the Number vehicle-trips per building (auto + bus):
    """
    f = num_persontrip_automode / 1.48
    g = num_persontrip_busmode / 48
    num_vehicletrip_per_building_autobus_mode = round(f + g)
    
    """ Returns the Vehicle-trips per building (auto + bus):
    """
    h = tot_num_persontrip_automode / 1.48
    i = tot_num_persontrip_busmode / 48
    vehicletrip_per_building_autobus_mode = round(h+i)
    
    """ X and Y coordinates for the graph:
    """
    x = df['Office Space (Sq.Ft.)']
    y = num_vehicletrip_per_building_autobus_mode
    

    """ Calculates the slope (m) and y intercept (b):
    """
    m = (((mean(x) * mean(y)) - mean(x * y)) /
         ((mean(x)*mean(x)) - mean(x*x)))
    b = mean(y) - m * mean(x)
    
    """ Plot:
    """
    ax=plt.axes()
    ax.set_xlabel('Office Space (Sq.Ft.)', fontweight='semibold')
    ax.set_ylabel('Number vehicle-trips per building (auto + bus)', fontweight='semibold')
    plt.plot(x,y,'o')
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
    plt.show()

    return (m * build_space_est) + b
