

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies. Does the sequence matter here?
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
# Assign a variable to save the file to a path.
file_to_save = os.path.join('Analysis','election_analysis.txt')
# 1. Initialize the total vote counter to 0
total_votes = 0
# Candidate options
candidate_options = []
# Dictionary of candidates
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:    
    # read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    # Print each row in the csv file
    for row in file_reader:
        # 2. Add to the total vote count total_votes = total_votes + 1
        total_votes += 1

# # 3. Print the total votes.
# print(total_votes)

        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f'\nElection Results\n'
        f'---------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'---------------------\n')
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percent = float(votes) / float(total_votes) * 100
        # 4. Print each candidate name, vote count, and percentage of votes.
        candidate_results = (f'{candidate_name}: received {vote_percent:.1f}% ({votes:,})\n')
        # Print each candidate, vote count, and vote percent to the terminal
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percent > winning_percentage):
            # 2. If true then set winning_vount = votes and winning_percentage = vote_percent.
            winning_count = votes
            winning_percentage = vote_percent
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # Print out the winning candidate, vote count, and percentage
    winning_candidate_summary = (
        f'--------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'--------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    
            
    # # Print the candidate list.
    # print(candidate_options)


    # # Print the candidate vote dictionary
    # print(candidate_votes)







