# Election-Analysis

## Overview of Election Audit

Tom, a Colorado Board of Elections employee, has tasked me to assist him complete an election audit of a recent local congressional election.  The objectives of the election audit include:

   1. Calculate the total number of votes cast.
   2. Get a complete list of candidates who received votes.
   3. Calculate the total number of votes each candidate received.
   4. Calculate the percentage of votes each candidate won.
   5. Determine the winner of the election based on popular vote.
   6. Calculate the voter turnout for each county.
   7. Calculate the percentage of votes from each county.
   8. Determine the county with the highest voter turnout.

While tasks like these are commonly completed using Excel, Tom and I would like to automate the election audit in Python.  Using Python successfully will allow the script to be used to audit other congressional districts, senatorial districts, and local elections. 

We will tally three different voting methods to complete the audit.  They are mail-in ballots, punch cards, and direct recording electronic ballots.  Although the methods for counting each type of ballot is different, the voting data will be consolidated into a single comma-seprated-value Excel file for our audit and certified report on the election results.

### Resources

* Data Source:  election_results.csv
* Softward:  Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results

The analysis of the election show that:

* There were 369,711 votes cast in the election.
* The candidates were:
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane

The image below illustrates the script used to tally the votes for each candidate:
![SS1-CandidateNamesVote.png](Resources/SS1-CandidatesNamesVotes.png)

* The candidate results were:
  * Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes.
  * Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane recieved 3.1% of the vote and 11,606 number of votes.
* The winner of the election was:
  * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

The image below shows the script used to print the results by candidate.
![SS2-PrintCandidateResults](Resources/SS2-PrintCandidateResults.png)

* The election results by county were:
  * Jefferson county represented 10.5% of the vote or 38,855 votes.
  * Denver county represented 82.8% of the vote or 306,055 votes.
  * Arapahoe county represented 6.7% of the vote or 24,801 votes.
*The largest voter turnout was seen in Denver county.

The image below shows the script to print the election results by county.
![SS3-PrintCountyVotes](Resources/SS3-PrintCountyVotes.png)

### Text File with Vote Results

![SS4-Election_Analysis_TextFile.png](Resources/SS4-Election_Analysis_TextFile.png)

### Terminal Output with Vote Results

![SS5-Election_Analysis_Terminal.png](Resources/SS5-Election_Analysis_Terminal.png)

## Election Audit Summary

With minor changes, this Python script can be used by the election commission to audit any congressional, senatorial, or local election.  This script will save many hours that would have been spent aggregating, analyzing, and formatting data.  

Few modifications required to reuse the code.  They are as follows:

* Update the folders and file names of the documents to read and write (see image below).  Line 9 includes a reference to the folder location of the raw data and the file name to read.  Line 11 includes a reference to the folder location to save the output analysis and the file name of the analysis.  These references must be updated when reusing the script. 

![SS6-Modify_LoadnSaveFile](Resources/SS6-Modify_LoadnSaveFile.png)

* Update the header and row indices if applicable (see image below).  If the raw data excludes a header row, then the "next" function must be omitted on line 40 to ensure we capture all of the data witing the file.  Similarly, if the raw data is presented in different rows, then the row indices on lines 49 and 52 must be updated to ensure we are capturing the candidate's names and county names respectively.

![SS7-Modify_HeaderCandidateCounty](Resources/SS7-Modify_HeaderCandidateCounty.png)

At a minimum, please consider using this code in parallel with your traditional analyses.  Once you feel comfortable that the script is reliably analyzing the data, you may want to decide to use this script for future analyses.

