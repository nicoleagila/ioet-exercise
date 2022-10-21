# Ioet exercise

Developed by Nicole Agila Pinto

## Problem
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2

Example 2:

INPUT:
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
RENE-ASTRID: 3

## Solution
The proposed solution developen in **python** programing language is an algorithm that works with a dictionary, formed from the input file, where the keys are the names of the employees, and the value for each employee is a new dictionary with the office hours per day.

> {"Employee 1" : {"Mo" : [10,11] } }

The algorithm checks pairs of employees if they match in a period of time in the office, comparing the schedules day by day. After comparing an employee's schedule to all the others, this employee is removed from the list to avoid redundancy.

The **architecture** of the solution consists of:
- functions.py file where all functions are declared and implemented.
- main.py file where the functions created and the logic of the solution are called.
- test.py file where all the unit tests are implemented

### Other considerations:
Besides to the requested requirements, I included some validations to the solution such as:
- If input file does not exist.
- If there is no match between some employees, it only shows the ones that were matched.

## Instructions
To run the **program** locally you have to run the following command:
```
$ python main.py
  > Insert input filename: 
```

To run the **unit tests** locally you have to run the following command:
```
$ python test.py -v
```
