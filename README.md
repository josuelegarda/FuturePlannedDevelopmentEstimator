# FuturePlannedDevelopmentEstimator


This program estimates future planned developments. To explain it further this program estimates the number of vehicle-trips for a planned office building of a input sq. ft. desired by the user by using the info of the list with the office spaces around that development. Its basically like a trip assessment for a development. 

Assumptions:
* The auto mode is 0.1, bus mode is 0.15, subway mode is 0.65, rail mode is 0.1
* Make sure that there is NO commas in the numbers in the csv file. The commas can interfere with data types 
* Only types of transportation considered are: auto, bus, railway, and subway





Inputs:
* A csv file with the office space of buildings in the studied area in sq. ft. and the Number of Employees per 1,000 Sq. Ft. 
* The building space (sq. ft.) to estimate how many vehicle-trips can exist in office building.

Outputs:
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
Make sure you import the csv in any program that you are using so it can be called by read.csv.
Make sure none of these numbers have commas in it because it can interrupt with the datatypes.
Below is an example on how it should look:




![image](https://user-images.githubusercontent.com/73948055/101570758-13d44e80-39a5-11eb-8d5e-692d9cf89663.png)








When first running the code the code will prompt you:
csvname = input("Enter the name of the csv file, Example: filename.csv:")
Here you input Exactly including the .csv of the name of the csv that you made


Next, it will ask you to input the building space in (sq. ft.) to estimate vehicle-trips for that office building:
build_space_est = input("Enter the building space in (sq. ft.) to estimate vehicle-trips for that office building (DON'T ADD COMMAS):")
Make sure to add the number without any commas so it doesn't interrupt with the algorithm. 




Then to call the function made do this:
a=num_vehicletrip_office_build()
This will perform the calculations for the csv file that you entered to then calculate The Number of vehicle-trips for a planned office building of certain square feet. 











This program also graphs the data
Below is an example on how the graph may look: 



![image](https://user-images.githubusercontent.com/73948055/101584160-015d1380-39ab-11eb-858d-51aaccd56081.png)















