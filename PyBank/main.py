# Data Analytics and Visualizations Bootcamp 
# Student Name: Thet Win
# Module 3 - Python
# Modified Date: May 10, 2024
#
# Part 1 - PyBank
# Python script that analyzes the records to calculate each of the following values:
# •	The total number of months included in the dataset
# •	The net total amount of "Profit/Losses" over the entire period
# •	The changes in "Profit/Losses" over the entire period, and then the average of those changes
# •	The greatest increase in profits (date and amount) over the entire period
# •	The greatest decrease in profits (date and amount) over the entire period
# •	Print the analysis to the terminal and export a text file with the results.

import os
import csv
import statistics

# Set up relative Paths
cwd = os.path.abspath(__file__)
dir_name=os.path.dirname(cwd)
csvpath=os.path.join(dir_name,'Resources','budget_data.csv')
outputpath=os.path.join(dir_name,'analysis','analysis_output.txt')

# Sum Profit/Loss Column
with open(csvpath,encoding='UTF-8') as csvfile:
    #Exclude the column header row in sum
    headerrow = next(csvfile)
    csvreader=csv.reader(csvfile, delimiter=",")

    #Initialize the variables and lists
    netTotalAmout=0
    ttlMonths=0
    maxValue=0
    minValue=0
    avgChange=0.0
    maxDate=""
    minDate=""

    dateArr=[]  
    changeRateArr=[]
    maxValueArr=[]
    minValueArr=[]

    # Populate Date list, Max Value list, Min Value list
    for row in csvreader:
        netTotalAmout += int(row[1])
        ttlMonths += 1
        dateArr.append(row[0])
        maxValueArr.append(float(row[1]))
        minValueArr.append(float(row[1]))

    # Calculate the differnce in Profits and Losses and store them in an array    
    for currRow, prevRow in zip(maxValueArr[::1], maxValueArr[1::1]):
        changeRateArr.append(float(prevRow-currRow))
    
# Calculate the average change
avgChange=round(statistics.mean(changeRateArr),2)
# Assign Max and Min values of the Change Rates
maxValue=int(max(changeRateArr))
minValue=int(min(changeRateArr))
# Search for the corresponding Dates of Max and Min values using their indexes - Need to plus one to offset the index
maxDate=dateArr[((changeRateArr.index(maxValue))+1)]
minDate=dateArr[((changeRateArr.index(minValue))+1)]

# Print the final results to validate       
print("Financial Analysis")
print("---------------------------")
print("Total Months: ", ttlMonths)
print("Total: $", netTotalAmout)
print("Average Change: $", avgChange)
print("Greatest Increase in Profits: ", maxDate +" ($" + str(maxValue) + ")")
print("Greatest Decrease in Profits: ", minDate +" ($" + str(minValue) + ")")

# Write the results to a txt file
outputfile = open(outputpath,'w') 
outputfile.write("Financial Analysis \n")
outputfile.write("--------------------------- \n")
outputfile.write("Total Months: " + str(ttlMonths) + "\n")
outputfile.write("Total: $" + str(netTotalAmout) + "\n")
outputfile.write("Average Change: $" + str(avgChange) + "\n")
outputfile.write("Greatest Increase in Profits: " + str(maxDate) +" ($" + str(maxValue) + ")\n")
outputfile.write("Greatest Decrease in Profits: " + str(minDate) +" ($" + str(minValue) + ")\n")
outputfile.close()
