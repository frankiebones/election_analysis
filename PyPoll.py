# The data we need to retrieve
# 1. the total number of votes 
# 2. complete list of candidates who received votes 
# 3. percentage of votes for each candidate 
# 4. total number of votes each candidate won 
# 5. the winner based on popular vote 
import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

with open(file_to_load) as election_data:

    # print(election_data)
    
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    # print(headers)

    for row in file_reader:

        print(row)

# with open(file_to_save, 'w') as txt_file:

    # txt_file.write("Arapahoe\nDenver\nJefferson")

