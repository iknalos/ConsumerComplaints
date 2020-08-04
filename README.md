

This GitHub repository contains my solution to the coding challenge for Insight Fellowship Program

Here i am using the same input csv file to generate and result.csv file

"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67 "credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100 debt collection,2019,1,1,100

In Short we are generating the output:
    productname,year,total number of complaints received for that product and year,total number of companies receiving at least one complaint for that product and year,highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

Steps to run:

To execute the script move to the main directory of the project and run the following in the terminal:

python3.8 ./src/consumer_complaints.py ./input/complaints.csv ./output/report.csv


