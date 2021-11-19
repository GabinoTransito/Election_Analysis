# The data we need to retrieve
# 1. the total number of votes cast.
# 2. A complete list of candidates that received votes.
# 3. the percentage of votes each candidate won.
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote.
import csv
import os
# Assign a variable for the file to load and the path.
# Direct path to the file.
# Personally, i had to add the election_analysis to the relative path because i added it in an additional folder. That is why you cannot have just resources and the file name.
file_to_load = 'Election_Analysis/resources/election_results.csv'
# Create a filename variable to a direct or indirect path to the file
file_to_save = 'Election_Analysis/analysis/election_analysis.txt'
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze the data here.
     #print(election_data)
     file_reader = csv.reader(election_data)
    # Print each row in the CSV file. remember to indent or youll get an I/O error message. 
     #for row in file_reader:
          #print(row)
     # Read and print the header row.
     headers = next(file_reader)
     print(headers)
#Indirect path to the file using OS (operating system method)
# Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

#using open and close statements
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = 'Election_Analysis/analysis/election_analysis.txt'
# Using the open() function with the "w" mode we will write data to the file.
# original code is without the outfile, we add outfile on the second step; this is a variable.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

#using the with statement; much cleaner this way. 
# Create a filename variable to a direct or indirect path to the file; commenting this out and moving actual working code to line 13-14.
#file_to_save = 'Election_Analysis/analysis/election_analysis.txt'

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("-------------------------\n")
    
    #Adding more text to the file 
    # Write three counties to the file; this method will give a space in between each county name but they will appear on the same line. 
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    # Write three counties to the file; much faster and cleaner way to have the sme result from above.
    #txt_file.write("Arapahoe, Denver, Jefferson")

    # Write three counties to the file. adding the \n will continue the text on a new line.
    #txt_file.write("Arapahoe\nDenver\nJefferson")