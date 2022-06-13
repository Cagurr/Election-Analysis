# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv

import os

# Assign a variable for the file to load and the path

file_to_load = os.path.join('Resources','election_results.csv')

# Assign a variable for the file to be created 

file_to_save = os.path.join('Analysis','election_output.txt')

# Open the election_results file and read it

with open(file_to_load) as election_data:

    # Read the file object with the csv.reader function

    file_reader = csv.reader(election_data)

    # Read and print the header row
    
    headers = next(file_reader)
    
    print(headers)

    # Print each row in the csv file

    ####for row in file_reader:

        ####print(row)

####with open(file_to_save,'w') as txt_file:

    ####txt_file.write()