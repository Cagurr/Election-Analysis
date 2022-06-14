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


# Initialize the total vote counter (aka an accumulator) called total_votes

total_votes = 0


# Declare a new list for candidates & a dictionary for their respective votes

candidate_options = []
candidate_votes = {}

# Declare variables for winning_candidate, winning_count, and winning_percentage

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election_results file and read it

with open(file_to_load) as election_data:

    # Read the file object with the csv.reader function

    file_reader = csv.reader(election_data)


    # Read and print the header row
    
    headers = next(file_reader)
    

    # Print each row in the csv file

    for row in file_reader:

        # Add to the total vote count
        
        total_votes += 1

        # Print the candidate name from each row

        candidate_name = row[2]


        if candidate_name not in candidate_options:
        
            # Add the unique candidate names to the candidate list
            
            candidate_options.append(candidate_name)
            
            # Begin tracking each candidate's vote count by starting count at zero
            
            candidate_votes[candidate_name] = 0

        # Counts each candidate's vote    
        
        candidate_votes[candidate_name] += 1


    # Determine % of votes for each candidate
    # Iterate through the candidate names

    for candidate_name in candidate_votes:

        # Retrieve vote count for each candidate 
            
        votes = candidate_votes[candidate_name]

        # Calculate the % of each candidate's votes

        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate's name and candidate's votes usin fString

        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")


        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
        
            winning_count = votes
        
            winning_percentage = vote_percentage
        
            # 3. Set the winning_candidate equal to the candidate's name.
        
            winning_candidate = candidate_name


# Iterates through candidates to print more than one candidate name

candidate_votes[candidate_name] += 1


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)