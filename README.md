# H1B Analysis
Analysis of numbers of certified H1B applications by occupations and states

## Problem
The US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis) publish data on H1B(H-1B, H-1B1, E-3) visa application processing each year. 
This project is to create a mechanism to analyze H1B data from past years and future years with two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. This mechanism is designed to read data in the `input` folder and produce the results in the `output` folder.

## Aproach
My code is written in Python with built-in standard libraries only. Three positional arguments need to be specified: one input file and two output files (top 10 occupations and top 10 states). The program reads the data line by line and update numbers of certified applications for each occupation or each state accordingly to generate two dictionaries. Then, the dictionaries are further updated with percentage of certified applications for each occupation or state in all certified applications. The two dictionaries are sorted by number of certified applications in descending order and then by occupations or states alphabetically. Finally, two txt files are saved to store the top 10 occupations and top 10 states with certified H1B applications.

## Run Instructions
By running the `run.sh` script, the input data file in the `input` folder should be read and the results should be saved to two txt files in the `output` folder. Before running this script, one just needs to change the input file name in the script.
