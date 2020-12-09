# CE-UY 3013 Project Template

*This file presents a description of the final project. For your submission,*
*this file must serve as the documentation of your project, how your program*
*should be used along with examples.*

This program estimates future planned developments. To explain it further this program estimates the number of vehicle-trips for a planned office building of a input sq. ft. desired by the user by using the info of the list with the office spaces around that development. Its basically like a trip assessment for a development. 

Assumptions:
* The auto mode is 0.1, bus mode is 0.15, subway mode is 0.65, rail mode is 0.1
* Make sure that there is NO commas in the numbers in the csv file. The commas can interfere with data types. 






Inputs:
* A csv file with the office space of buildings in the studied area in sq. ft. and the Number of Employees per 1,000 Sq. Ft. 
* The building space (sq. ft.) to estimate how many vehicle-trips can exist in office building.

Outputs:
* Average office building space
* Number of employees per building
* Total number of person-trips which use automobiles
* Total number of person-trips which use subway
* Total number of person-trips which use rails like the (LIRR)
* Vehicle trips per building
* A plot of with regression line office building space vs the total number of vehicle trips
* The number of vehicle-trips for the input building space (sq. ft.)

## Setup
In order to use the program, you have clone/download this repository,
navigate to the local directory and create a virtual environment with:

```
$ python -m venv venv
```
Then, activate the virtual environment:

'''
For Linux/Mac OS:
$ source venv/bin/activate

For Windows:
> venv\Scripts\activate
'''

Finally, install the required libraries for this program with:

'''
$ pip install -r requirements.txt
'''

## How to use the program
First, as stated above make sure you have a csv file with a column, Office Space in (sq. ft.) and Number of Employees per 1,000 Sq. Ft..
Make sure none of these numbers have commas in it because it can interrupt with the datatypes. 


Now, you have to make sure you download the packages needed. For this program you will need: pandas, numpy, math, and matplotlib. 
So make sure you have these downloaded before starting. 

When you run the code it will ask you for 2 inputs: 1. Enter the name of the csv file, Example: filename.csv:
2. Enter the building space in (sq. ft.) to estimate vehicle-trips for that office building (DON'T ADD COMMAS): 
Again don't add commas here either.
When you enter for the first input make sure you input EXACT name of the csv you are using and make sure you can access it.

For the next calcualtions you will need to do 1 by 1 to get information about your data
Below you will find the functions already made to help with calculations MAKE SURE you follow these step by step

* 1- Average office building space
avg_office_building_space()

* 2- Number of employees per building
num_employees_per_building()

* 3- Average number of employees per building.
avg_num_employees_per_building()

* Number of person-trips which use auto mode 
num_persontrip_automode()

* Total number of person-trips use auto mode 
tot_num_persontrip_automode()

* Number of person-trips bus mode 
num_persontrip_busmode()

* Total number of person-trips bus mode 
tot_num_persontrip_busmode()

* Number of person-trips subway mode 
num_persontrip_subwaymode()

* Total number of person-trips subway mode 
tot_num_persontrip_subwaymode()

* Number of person-trips rail mode 
num_persontrip_railmode()

* Total number of person-trips rail mode 
tot_num_persontrip_railmode()

* Number vehicle-trips per building (auto + bus)
num_vehicletrip_per_building_autobus_mode()

* Vehicle-trips per building (auto + bus)
vehicletrip_per_building_autobus_mode()

After all of these calculations were made, now time to plot: 
If you are using Jupyter Notebook use:
%matplotlib inline













