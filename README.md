# The goal was to help Tom with his analysis of a recent local congressional election on behalf of the Colorado Board of Elections.

## Resources
Source: election_results.csv<br>
Output: election_analysis.txt<br>
Written in: <i>Python 3.10.2 via VSCode 1.66.2</i><br>

## We gathered the following information:
- total number of votes in the election
- a list of all candidates who received votes in the election
- total number of votes per candidate
- total percentage of votes per candidate
- winner based on the popular vote

## Dependencies
In order to work with the supplied csv file we needed to import two modules. The <code>csv</code> module has a function called <code>reader</code> which will allow us to iterate over each row in the file and read each of those rows. The <code>os</code> module has a function called <code>path</code> that will allow us to both read from the locally stored csv file as well as write to a locally stored txt file for output.

```
import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("Analysis", "election_analysis.txt")
```

## Election-Audit Results
While one could of course simply determine the number of votes by counting the number of rows in the csv file, we utilized Python to create a script that looped through each of the rows. 

```
for row in reader:

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Get the county name from each row.
        county_name = row[1]
```
Then we extracted all the unique candidate names and counties involved in the election and stored them in a list.<br> 
<i>example shown for candidate names only but similar process was used for county names</i>

```
if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)
```

## Election-Audit Summary
While some indexes may need to be changed to accomodate differing layouts of csv files, this script is scalable and can be utilized for just about any election in Colorado or country wide for that matter regardless of the number of candidates and/or jurisdictions included.
One of the recommendations I have for the election commission would be to increase their outreach efforts in both Jefferson and Arapahoe Counties as their voter turnout are both below 7% while Denver was over 42%. 
![voter_turnout](https://user-images.githubusercontent.com/15967377/165414605-fb71cef7-03c8-4c63-a88d-06c7dca855f5.PNG)

