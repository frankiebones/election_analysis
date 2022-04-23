# add dependencies (csv needed to read csv file, os need to utilize path)
import csv
import os

# assign variable to load file from a path
file_to_load = os.path.join('Resources', 'election_results.csv')
# assign variable to save file to a path
file_to_save = os.path.join('Analysis', 'election_analysis.txt')

# initialize vote counter
total_votes = 0
# create empty candidate list
candidate_options = []
# create empty candidate/votes dictionary
candidate_votes = {}
# create empty string for winning candidate name
winning_candidate = ""
# initialize winning count and percentage
winning_count = 0
winning_percentage = 0

# open & read the election results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:

        # add to the total vote count
        total_votes += 1
        # get candidate name from each row
        candidate_name = row[2]

        # check is candidate name already in list
        if candidate_name not in candidate_options:

            # add candidate name to the  candidate list
            candidate_options.append(candidate_name)

            # initialize individual candidate vote count
            candidate_votes[candidate_name] = 0

        # add vote to individual candidate vote count
        candidate_votes[candidate_name] += 1

with open(file_to_save, 'w') as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-----------------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_options:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        # determine if votes/percentage are greater than the winning count/percentage
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
#print(candidate_votes)        
#print(total_votes)


# with open(file_to_save, 'w') as txt_file:

    # txt_file.write("Arapahoe\nDenver\nJefferson")

